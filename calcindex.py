#coding=utf-8

import os
import sys
import datasql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class IndexValue:
	def __init__(self, td, value, divisor, point):
		self.td = td
		self.value = value
		self.divisor = divisor
		self.point = point
	def __repr__(self):
		return repr((self.td, self.value, self.divisor, self.point))
	
#获得月度数据
def getMonthlyData():
	sqlfile = "query_closeprice_monthly.sql"
	curpath = os.getcwd()
	
	df = datasql.getGeneralData(sqlfile, curpath)
	return df

#获得交易日
def getTradingDays(df):
	tdarray = df['TradingDay'].unique()
	return tdarray.tolist()

#获得个股股数，在重新调整前，该股数保持不变	
def getShares(df, mktcap=10000.0):
	df.loc[:,'Shares'] = df['ClosePrice'].astype(float).apply(lambda x:mktcap/x)
	return df

#使用上期个股数量更新本期
def setShares(newdf, olddf):
	tempdf = olddf.loc[:, ['SecuCode', 'Shares']]
	df = pd.merge(newdf, tempdf, on='SecuCode', how='left')
	return df
	
def getIndexPrice(df, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap'):
	"""	#获得价格总额
		#df - 当期所有股票
		#lblprice - 价格列名称
		#lblshare - 股数列名称
		#lblmktcap - 新列 市值列名称
		#return - 价格总额
	"""
	#shares = df['Shares'].values.tolist()
	#prices = df['ClosePrice'].values.tolist()
	#df['mktcap'] = df.apply(lambda x: float(x['ClosePrice'])*x['Shares'], axis=1)
	df.loc[:, lblmktcap] = df.apply(lambda x: float(x[lblprice])*x[lblshare], axis=1)
	total = df[lblmktcap].sum()
	return float(total)

def equalWeightByTradingDay(df, mktcap=10000.0, base=1000):
	#tds - 交易日列表，需要排序在从小到大处理
	#df - 月度数据
	#mktcap - 基期每只股票持有市值
	#base - 指数基点
	#tds = tds.sort()
	tdarray = df['TradingDay'].unique()
	tds = sorted(tdarray.tolist())
	
	idxvalues = []
	predf = None
	divisor = 0.0
	point = 0.0
	for i in range(len(tds)):
		td = tds[i]
		tempdf = df[df['TradingDay'] == td]
		period = None
		pval = 0.0
		
		if i == 0:
			period = getShares(tempdf, mktcap)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = base
			divisor = pval / base
		else:
			period = setShares(tempdf, predf)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = pval/divisor
			
			size = len(period)
			eachcap = pval/size
			#重新等权所有股票
			period.loc[:, 'Shares'] = period.apply(lambda x:eachcap/float(x['ClosePrice']), axis=1)	

		predf = period
		iv = IndexValue(td, pval, divisor, point)
		idxvalues.append(iv)
		
	return idxvalues

def equalShareByTradingDay(df, shares=1000, base=1000):	
	#df - 月度数据
	#shares - 基期每只股票持有股数
	#base - 指数基点
	tdarray = df['TradingDay'].unique()
	tds = sorted(tdarray.tolist())
	
	idxvalues = []
	predf = None
	divisor = 0.0
	point = 0.0
	for i in range(len(tds)):
		td = tds[i]
		tempdf = df[df['TradingDay'] == td]
		period = None
		pval = 0.0
		
		if i == 0:
			period = tempdf
			period.loc[:, "Shares"] = shares
			#period = getShares(tempdf, mktcap)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = base
			divisor = pval / base
		else:
			period = setShares(tempdf, predf)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = pval/divisor
				
			#重新分配股数-每支股票持有相同股数
			totalprice = float(period['ClosePrice'].sum())
			eachshare = pval / totalprice
			period.loc[:, "Shares"] = eachshare
			
		predf = period
		iv = IndexValue(td, pval, divisor, point)
		idxvalues.append(iv)
		
	return idxvalues

def mktcapByTradingDay(df, base=1000):	
	#df - 月度数据
	#base - 指数基点
	tdarray = df['TradingDay'].unique()
	tds = sorted(tdarray.tolist())
	
	idxvalues = []
	predf = None
	divisor = 0.0
	point = 0.0
	for i in range(len(tds)):
		td = tds[i]
		tempdf = df[df['TradingDay'] == td]
		period = None
		pval = 0.0
		
		if i == 0:
			period = tempdf
			period.loc[:, "Shares"] = period.loc[:, "AFloats"]
			#period = getShares(tempdf, mktcap)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = base
			divisor = pval / base
		else:
			period = setShares(tempdf, predf)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = pval/divisor
				
			#重新调整股数，使用流通股在平衡，此时需要调整除数divisor
			#newpval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='AFloats', lblmktcap='nmktcap')
			#divisor = newpval / point
			#period.loc[:, "Shares"] = period.loc[:, "AFloats"]
			
		predf = period
		iv = IndexValue(td, pval, divisor, point)
		idxvalues.append(iv)
		
	return idxvalues
	
def draw(idxvalues):
	ordervalues = sorted(idxvalues, key=lambda d:d.td)
	x = []
	y = []
	xlabel = []
	size = len(ordervalues)
	for i in range(size):
		current = ordervalues[i]
		x.append(i+1)
		y.append(current.point)
		xlabel.append(current.td)
	
	fig,ax = plt.subplots()
	#设置横坐标
	ax.set_xticks(x)
	ax.set_xticklabels(xlabel, rotation=40)
	#plt.xticks(x, xlabel)
	plt.plot(x, y)
	plt.show()
	
if __name__ == "__main__":
	#获得月度数据
	#df = getMonthlyData()
	#df.to_csv("./data/monthlydata.csv", encoding='utf8')
	df = pd.read_csv("./data/monthlydata.csv")
	#计算指数
	#等权重
	#idxvalues = equalWeightByTradingDay(df)
	#等股份
	#idxvalues = equalShareByTradingDay(df)
	#等市值
	idxvalues = mktcapByTradingDay(df)
	print(idxvalues)
	#画图
	draw(idxvalues)