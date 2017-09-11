#coding=utf-8

import os
import sys
import datasql
import pandas as pd
import numpy as np

class Price:
	def __init__(self, td, price):
		self.td = td
		self.price = price
		
	def __repr__(self):
		return repr((self.td, self.price))
	
def getIndexData():
	sqlfile = "query_indexcloseprice_monthly.sql"
	curpath = os.getcwd()
	
	df = datasql.getGeneralData(sqlfile, curpath)
	return df

def getListData(df):
	listvalues = []
	for i, row in df.iterrows():
		#listvalues.append((row['TradingDay'], row['ClosePrice']))
		p = Price(row['TradingDay'], float(row['ClosePrice']))
		listvalues.append(p)
		
	return listvalues
	
if __name__ == "__main__":
	df = getIndexData()
	datas = getListData(df)
