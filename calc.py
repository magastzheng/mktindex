#encoding=utf-8

def getValue(shares, prices):
	"""calculate the sum of shares[i]*prices[i]
	"""
	multiplies = [a*b for a,b in zip(shares, prices)]
	return sum(multiplies)

def getDivisor(value, base):
	"""Get the divisor by composite value and its defined base point
	"""
	return float(value)/base

def getAdjustedDivisor(newValue, oldIndex):
	"""	Get new divisor
		It is the result of the new market value divided by the old index value.
		newValue - the index price value after the composite adjusted
		oldIndex - the last day of the index point before composite adjusted
		return - a new divisor(factor)
	"""
	
	return newValue/oldIndex

def getIndexPrice(value, divisor):
	"""	Get the index price point
		value - the index price value, it is the sum of shares[i]*prices[i]
		divisor - a factor of the index price value
		return - the index price point
	"""
	
	return float(value) / divisor
	
def getShares(mktcap, price):
	"""	Get the # of shares by the market capital and price
	"""
	
	return mktcap/price
	
def getSharesByArray(mktcaps, prices):
	"""	Get the # of shares array by the market capitals and prices array
		mktcaps - the market array
		prices - the prices array
	"""
	
	shares = [a/b for a, b in zip(mktcaps, prices)]
	return shares

def getSharesByMktCap(mktcap, prices):
	"""	Get the # of shares array by the given market capital. It will 
		calculate the equal weighted
	"""
	
	shares = [mktcap/a for a in prices]
	return shares
	
if __name__ == '__main__':
	#test the getValue
	shares = [10, 20, 30]
	prices = [1.5, 2.5, 3.5]
	val = getValue(shares, prices)
	print("price value: {0}".format(val))

	#test the getDivisor
	val = 50000
	base = 100
	divisor = getDivisor(val, base)
	print("divisor: {0}".format(divisor))
	
	
	


	
	