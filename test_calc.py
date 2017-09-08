#encoding=utf-8

import unittest
import calc

def func(x):
	return x+1

class CalcTest(unittest.TestCase):
	def test(self):
		self.assertEqual(func(3), 4)
	
	def test_getValue(self):
		shares = [1, 2, 3]
		prices = [1.5, 2.5, 3.5]
		self.assertEqual(calc.getValue(shares, prices), 17)
	
	def test_getDivisor(self):
		value = 50000
		base = 100
		self.assertEqual(calc.getDivisor(value, base), 500)
	
	def test_getAdjustedDivisor(self):
		newValue = 512010
		oldIndex = 123
		self.assertEqual(calc.getAdjustedDivisor(newValue, oldIndex), 4162)
	
	def test_getIndexPrice(self):
		value = 51200
		divisor = 500
		actual = calc.getIndexPrice(value, divisor)
		self.assertAlmostEqual(actual, 102.4, 1)
	
	def test_getShares(self):
		mktcap = 10000
		price = 25.5
		actual = calc.getShares(mktcap, price)
		self.assertAlmostEqual(actual, float(392.156862), 5)
	
	def test_getSharesByArray(self):
		mktcaps = [10000, 10000, 10000]
		prices = [100, 200, 400]
		actual = calc.getSharesByArray(mktcaps, prices)
		expect = [100, 50, 25]
		self.assertListEqual(actual, expect)
	
	def test_getSharesByMktCap(self):
		mktcap = 10000
		prices = [100, 200, 400]
		actual = calc.getSharesByMktCap(mktcap, prices)
		expect = [100, 50, 25]
		self.assertListEqual(actual, expect) 
	
if __name__ == '__main__':
	unittest.main()