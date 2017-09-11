select distinct convert(varchar, TradingDay, 112) as TradingDay
from zhenggq.dbo.FactorDaily_Comparable
where TradingDay is not null
order by TradingDay desc