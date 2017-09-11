#coding=utf-8

import os
import sys
import datasql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fetchindex

class IndexValue:
	def __init__(self, td, value, divisor, point, newvalue):
		self.td = td
		self.value = value
		self.divisor = divisor
		self.point = point
		self.newvalue = newvalue
	def __repr__(self):
		return repr((self.td, self.value, self.divisor, self.point, self.newvalue))
	
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
	#由于本期可能有些股票已近退市，如果直接这样处理，会导致这些退市股票消失掉，市值减少
	#多期累积之后，这部分损失会很大
	#这里先把该股票使用上期替代
	tempdf = olddf.loc[:, ['SecuCode', 'ClosePrice', 'Shares']]
	df = pd.merge(newdf, tempdf, on='SecuCode', how='outer', suffixes=('_left', '_right'))
	#使用上期收盘价填充本期消失的股票
	df['ClosePrice_left'] = df['ClosePrice_left'].fillna(df['ClosePrice_right'])
	#本期新股设置股数为0
	df['Shares'] = df['Shares'].fillna(0)
	df.rename(columns={'ClosePrice_left': 'ClosePrice'}, inplace=True)
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
	df.loc[:, lblmktcap] = df.apply(lambda x: float(x[lblprice])*float(x[lblshare]), axis=1)
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
			poldval = pval
			period = getShares(tempdf, mktcap)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = base
			divisor = pval / base
		else:
			poldval = pval
			period = setShares(tempdf, predf)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = pval/divisor
			
			size = len(period)
			eachcap = pval/size
			#重新等权所有股票
			period = tempdf
			period.loc[:, 'Shares'] = period.apply(lambda x:eachcap/float(x['ClosePrice']), axis=1)	
		
		#由于使用新市值等权处理，两期市值相等
		predf = period
		iv = IndexValue(td, pval, divisor, point, pval)
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
	poldval = 0.0
	
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
			#由于新股的加入，导致重新分配股数出现变化
			totalprice = float(period['ClosePrice'].sum())
			shares = pval / totalprice
			#print(td, pval, totalprice, shares, "\n")
			period = tempdf
			period.loc[:, "Shares"] = shares
			
		#重新分配股数时，使用总市值除以总价格，也就是说两期总市值不变
		predf = period
		iv = IndexValue(td, pval, divisor, point, shares)
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
		pnewval = 0.0
		if i == 0:
			period = tempdf
			period.loc[:, "Shares"] = period.loc[:, "AFloats"]
			#period = getShares(tempdf, mktcap)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = base
			divisor = pval / base
			pnewval = pval
		else:
			period = setShares(tempdf, predf)
			pval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='Shares', lblmktcap='mktcap')
			point = pval/divisor
				
			#重新调整股数，使用流通股在平衡，此时需要调整除数divisor
			period = tempdf
			pnewval = getIndexPrice(df=period, lblprice='ClosePrice', lblshare='AFloats', lblmktcap='nmktcap')
			divisor = pnewval / point
			period.loc[:, "Shares"] = period.loc[:, "AFloats"]
		
		#这种方式存在一定问题，理论上投资不应该需要追加投资，而仅仅涉及到资金的重新分配
		#但是这种方式需要撤回或者追加资金
		predf = period
		iv = IndexValue(td, pval, divisor, point, pnewval)
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

def drawboth(idxvalues, idxdatas):
	ordervalues_new = sorted(idxvalues, key=lambda d:d.td)
	ordervalues_orig = sorted(idxdatas, key=lambda d:d.td)
	#横坐标数据
	x = []
	#新的指数数据
	y1 = []
	#原始指数数据
	y2 = []
	#横坐标标签
	xlabel = []
	size = len(ordervalues_new)
	if size > len(ordervalues_orig):
		size = len(ordervalues_orig)
		td = ordervalues_orig[0].td
		for i in range(len(ordervalues_new)):
			if td == ordervalues_new[i].td:
				break
		if i < len(ordervalues_new):
			ordervalues_new = ordervalues_new[i:]
	else
		size = len(ordervalues_orig)
		td = ordervalues_orig[0].td
		for i in range(len(ordervalues_orig)):
			if td == ordervalues_orig[i].td:
				break
		if i < len(ordervalues_orig):
			ordervalues_orig = ordervalues_orig[i:]
	
	for i in range(size):
		x.append(i+1)
		y1.append(ordervalues_new[i].point)
		y2.append(ordervalues_orig[i].price)
		xlabel.append(ordervalues_new[i].td)
	
	fig,ax = plt.subplots()
	#设置横坐标
	ax.set_xticks(x)
	ax.set_xticklabels(xlabel, rotation=40)
	#plt.xticks(x, xlabel)
	plt.plot(x, y1)
	plt.plot(x, y2)
	plt.show()
	
def output(idxvalues, filename='./data/idxvaluex.csv'):
	header = "TradingDay,Value,Divisor,Point,Option\n"
	fmt = "{0},{1},{2},{3},{4}\n"
	#打开可读写文件，并写入新内容
	fileobj = open(filename, 'w+')
	try:
		fileobj.write(header)
		ordervalues = sorted(idxvalues, key=lambda d:d.td)
		for idx in ordervalues:
			line = fmt.format(idx.td, idx.value, idx.divisor, idx.point, idx.newvalue)
			fileobj.write(line)
	except Exception:
		print("Error: exception to write file.\n")
	finally:
		fileobj.close()
	
if __name__ == "__main__":
	#获得指数原始数据
	idxdf = fetchindex.getIndexData()
	idxdatas = fetchindex.getListData(idxdf)

	#获得月度数据
	#filename = './data/monthlydata.csv'
	filename = './data/monthlydata.pkl'
	#df = getMonthlyData()
	#df.to_csv("./data/monthlydata.csv", encoding='utf8')
	#df = pd.read_csv("./data/monthlydata.csv")
	
	#存为pickle格式
	#df.to_pickle(filename)
	df = pd.read_pickle(filename)
	#计算指数
	#等权重
	idxvalues = equalWeightByTradingDay(df)
	#等股份
	#idxvalues = equalShareByTradingDay(df)
	#等市值
	#idxvalues = mktcapByTradingDay(df)
	#print(idxvalues)
	output(idxvalues)
	#画图
	draw(idxvalues)