select convert(varchar,TradingDay, 112) as TradingDay
,SecuCode
,ClosePrice
,AFloats
,TotalCap
,TurnoverVolume
from winddb.dbo.FactorMonthly_Comparable