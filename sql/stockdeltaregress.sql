select a.createDate
    ,a.settleDate
    ,a.TradingDay
    ,a.SecuCode
	,a.SecuAbbr
    ,a.IndustrySecuCode_I
    ,convert(float, a. ClosePrice) as ClosePrice
    ,convert(float, a.OpenPrice) as OpenPrice
    ,convert(float, a.HighPrice) as HighPrice
    ,convert(float, a.LowPrice) as LowPrice
    ,convert(float, a.ExeClosePrice) as ExeClosePrice
    ,convert(float, a.ExeOpenPrice) as ExeOpenPrice
    ,convert(float, a.ExeHighPrice) as ExeHighPrice
    ,convert(float, a.ExeLowPrice) as ExeLowPrice
    ,convert(float, a.NonRestrictedShares) as NonRestrictedShares
    ,convert(float, a.AFloats) as AFloats
    ,convert(float, a.TotalShares) as TotalShares
    ,convert(float, a.TurnoverVolume) as TurnoverVolume
    ,convert(float, a.NonRestrictedCap) as NonRestrictedCap
    ,convert(float, a.AFloatsCap) as AFloatsCap
    ,convert(float, a.TotalCap) as TotalCap
    ,convert(float, a.PE) as PE
    ,convert(float, a.PB) as PB
    ,convert(float, a.PS) as PS
    ,convert(float, a.PCF) as PCF
    ,convert(float, a.DividendYield) as DividendYield
    ,convert(float, a.DividendRatio) as DividendRatio
    ,convert(float, a.TTMIncome) as TTMIncome
    ,convert(float, a.GP_Margin) as GP_Margin
    ,convert(float, a.NP_Margin) as NP_Margin
    ,convert(float, a.ROA) as ROA
    ,convert(float, a.ROE) as ROE
    ,convert(float, a.AssetsTurnover) as AssetsTurnover
    ,convert(float, a.EquityTurnover) as EquityTurnover
    ,convert(float, a.Cash_to_Assets) as Cash_to_Assets
    ,convert(float, a.Liability_to_Assets) as Liability_to_Assets
    ,convert(float, a.EquityMultiplier) as EquityMultiplier
    ,convert(float, a.CurrentRatio) as CurrentRatio
    ,convert(float, a.Income_Growth_YOY_Comparable) as Income_Growth_YOY_Comparable
    ,convert(float, a.NPPC_Growth_YOY_Comparable) as NPPC_Growth_YOY_Comparable
    ,convert(float, a.GP_Margin_Comparable) as GP_Margin_Comparable
    ,convert(float, a.GP_Margin_Growth_YOY_Comparable) as GP_Margin_Growth_YOY_Comparable
    ,convert(float, a.NP_Margin_Comparable) as NP_Margin_Comparable
    ,convert(float, a.NP_Margin_Growth_YOY_Comparable) as NP_Margin_Growth_YOY_Comparable
    ,convert(float, a.Income_Growth_Pre_Comparable) as Income_Growth_Pre_Comparable
    ,convert(float, a.NPPC_Growth_Pre_Comparable) as NPPC_Growth_Pre_Comparable
    ,convert(float, a.GP_Margin_Growth_Pre_Comparable) as GP_Margin_Growth_Pre_Comparable
    ,convert(float, a.NP_Margin_Growth_Pre_Comparable) as NP_Margin_Growth_Pre_Comparable
    ,convert(float, a.NPPC_Growth_Pre_Season) as NPPC_Growth_Pre_Season
    ,convert(float, a.NPPC_Growth_YOY_Season) as NPPC_Growth_YOY_Season
    ,convert(float, a.NPLNRP_Growth_Pre_Season) as NPLNRP_Growth_Pre_Season
    ,convert(float, a.NPLNRP_Growth_YOY_Season) as NPLNRP_Growth_YOY_Season
    ,convert(float, a.Income_Growth_Pre_Season) as Income_Growth_Pre_Season
    ,convert(float, a.Income_Growth_YOY_Season) as Income_Growth_YOY_Season
    ,convert(float, a.Income_Growth_Qtr_Comparable) as Income_Growth_Qtr_Comparable
    ,convert(float, a.NPPC_Growth_Qtr_Comparable) as NPPC_Growth_Qtr_Comparable
    ,convert(float, a.GP_Margin_Qtr) as GP_Margin_Qtr
    ,convert(float, a.GP_Margin_Growth_Qtr_Comparable) as GP_Margin_Growth_Qtr_Comparable
    ,convert(float, a.IPS_Qtr) as IPS_Qtr
    ,convert(float, a.EPS_Qtr) as EPS_Qtr
    ,convert(float, a.ROE_Qtr) as ROE_Qtr
    ,convert(float, a.Income_Growth_Pre) as Income_Growth_Pre
    ,convert(float, a.NPPC_Growth_Pre) as NPPC_Growth_Pre
    ,convert(float, a.NPLNRP_Growth_Pre) as NPLNRP_Growth_Pre
    ,convert(float, a.GP_Margin_Growth_Pre) as GP_Margin_Growth_Pre
    ,convert(float, a.NP_Margin_Growth_Pre) as NP_Margin_Growth_Pre
    ,convert(float, a.Income_Growth_YOY) as Income_Growth_YOY
    ,convert(float, a.NPPC_Growth_YOY) as NPPC_Growth_YOY
    ,convert(float, a.NPLNRP_Growth_YOY) as NPLNRP_Growth_YOY
    ,convert(float, a.GP_Margin_Growth_YOY) as GP_Margin_Growth_YOY
    ,convert(float, a.NP_Margin_Growth_YOY) as NP_Margin_Growth_YOY
    ,convert(float, a.IPS) as IPS
    ,convert(float, a.EPS) as EPS
    ,convert(float, a.CFPS) as CFPS
    ,convert(float, a.Pre_IPS) as Pre_IPS
    ,convert(float, a.Pre_EPS) as Pre_EPS
    ,convert(float, a.Pre_CFPS) as Pre_CFPS
    ,convert(float, a.YOY_IPS) as YOY_IPS
    ,convert(float, a.YOY_EPS) as YOY_EPS
    ,convert(float, a.YOY_CFPS) as YOY_CFPS
    ,convert(float, a.rPE) as rPE
    ,convert(float, a.rPB) as rPB
    ,convert(float, a.rPS) as rPS
    ,convert(float, a.rPCF) as rPCF
    ,convert(float, a.SettlePrice) as SettlePrice
    ,convert(float, a.IndusInnerCode) as IndusInnerCode
    ,convert(float, a.IndusCreatePrice) as IndusCreatePrice
    ,convert(float, a.IndusSettlePrice) as IndusSettlePrice
    ,convert(float, a.ExecutivesProp) as ExecutivesProp
    ,convert(float, a.InstitutionNum) as InstitutionNum
    ,convert(float, a.InstitutionProp) as InstitutionProp
    ,convert(float, a.RegionScore) as RegionScore
    ,convert(float, a.ExeClosePrice_CreateDate_Wind) as ExeClosePrice_CreateDate_Wind
    ,convert(float, a.ExeClosePrice_SettleDate_Wind) as ExeClosePrice_SettleDate_Wind
    ,convert(float, a.Momentum20Day) as Momentum20Day
    ,convert(float, a.Momentum40Day) as Momentum40Day
    ,convert(float, a.Momentum60Day) as Momentum60Day
    ,convert(float, a.Momentum120Day) as Momentum120Day
    ,convert(float, a.Momentum180Day) as Momentum180Day
    ,convert(float, a.Momentum240Day) as Momentum240Day
    ,convert(float, a.PriceDiff) as PriceDiff
    ,convert(float, a.DayDiff) as DayDiff
    ,convert(float, a.TurnoverRatio) as TurnoverRatio
    ,convert(float, a.AvgTurnoverPrice) as AvgTurnoverPrice
    ,convert(float, a.AvgTurnoverPriceFactor) as AvgTurnoverPriceFactor
    ,convert(float, a.AvgTurnoverRatio5Day) as AvgTurnoverRatio5Day
    ,convert(float, a.AvgTurnoverRatio10Day) as AvgTurnoverRatio10Day
    ,convert(float, a.AvgTurnoverRatio20Day) as AvgTurnoverRatio20Day
    ,convert(float, a.AvgTurnoverRatio40Day) as AvgTurnoverRatio40Day
    ,convert(float, a.AvgTurnoverRatio60Day) as AvgTurnoverRatio60Day
    ,convert(float, a.AvgTurnoverRatio120Day) as AvgTurnoverRatio120Day
    ,convert(float, a.E_EPS) as E_EPS
    ,convert(float, a.E_growth) as E_growth
    ,convert(float, a.FreeFloat_Total) as FreeFloat_Total
    ,convert(float, a.EPS_CFPS) as EPS_CFPS
    ,convert(float, a.AvgTurnoverValue) as AvgTurnoverValue
	,convert(float, b. ClosePrice) as ClosePrice_delta
	,convert(float, b.OpenPrice) as OpenPrice_delta
	,convert(float, b.HighPrice) as HighPrice_delta
	,convert(float, b.LowPrice) as LowPrice_delta
	,convert(float, b.ExeClosePrice) as ExeClosePrice_delta
	,convert(float, b.ExeOpenPrice) as ExeOpenPrice_delta
	,convert(float, b.ExeHighPrice) as ExeHighPrice_delta
	,convert(float, b.ExeLowPrice) as ExeLowPrice_delta
	,convert(float, b.NonRestrictedShares) as NonRestrictedShares_delta
	,convert(float, b.AFloats) as AFloats_delta
	,convert(float, b.TotalShares) as TotalShares_delta
	,convert(float, b.TurnoverVolume) as TurnoverVolume_delta
	,convert(float, b.NonRestrictedCap) as NonRestrictedCap_delta
	,convert(float, b.AFloatsCap) as AFloatsCap_delta
	,convert(float, b.TotalCap) as TotalCap_delta
	,convert(float, b.PE) as PE_delta
	,convert(float, b.PB) as PB_delta
	,convert(float, b.PS) as PS_delta
	,convert(float, b.PCF) as PCF_delta
	,convert(float, b.DividendYield) as DividendYield_delta
	,convert(float, b.DividendRatio) as DividendRatio_delta
	,convert(float, b.TTMIncome) as TTMIncome_delta
	,convert(float, b.GP_Margin) as GP_Margin_delta
	,convert(float, b.NP_Margin) as NP_Margin_delta
	,convert(float, b.ROA) as ROA_delta
	,convert(float, b.ROE) as ROE_delta
	,convert(float, b.AssetsTurnover) as AssetsTurnover_delta
	,convert(float, b.EquityTurnover) as EquityTurnover_delta
	,convert(float, b.Cash_to_Assets) as Cash_to_Assets_delta
	,convert(float, b.Liability_to_Assets) as Liability_to_Assets_delta
	,convert(float, b.EquityMultiplier) as EquityMultiplier_delta
	,convert(float, b.CurrentRatio) as CurrentRatio_delta
	,convert(float, b.Income_Growth_YOY_Comparable) as Income_Growth_YOY_Comparable_delta
	,convert(float, b.NPPC_Growth_YOY_Comparable) as NPPC_Growth_YOY_Comparable_delta
	,convert(float, b.GP_Margin_Comparable) as GP_Margin_Comparable_delta
	,convert(float, b.GP_Margin_Growth_YOY_Comparable) as GP_Margin_Growth_YOY_Comparable_delta
	,convert(float, b.NP_Margin_Comparable) as NP_Margin_Comparable_delta
	,convert(float, b.NP_Margin_Growth_YOY_Comparable) as NP_Margin_Growth_YOY_Comparable_delta
	,convert(float, b.Income_Growth_Pre_Comparable) as Income_Growth_Pre_Comparable_delta
	,convert(float, b.NPPC_Growth_Pre_Comparable) as NPPC_Growth_Pre_Comparable_delta
	,convert(float, b.GP_Margin_Growth_Pre_Comparable) as GP_Margin_Growth_Pre_Comparable_delta
	,convert(float, b.NP_Margin_Growth_Pre_Comparable) as NP_Margin_Growth_Pre_Comparable_delta
	,convert(float, b.NPPC_Growth_Pre_Season) as NPPC_Growth_Pre_Season_delta
	,convert(float, b.NPPC_Growth_YOY_Season) as NPPC_Growth_YOY_Season_delta
	,convert(float, b.NPLNRP_Growth_Pre_Season) as NPLNRP_Growth_Pre_Season_delta
	,convert(float, b.NPLNRP_Growth_YOY_Season) as NPLNRP_Growth_YOY_Season_delta
	,convert(float, b.Income_Growth_Pre_Season) as Income_Growth_Pre_Season_delta
	,convert(float, b.Income_Growth_YOY_Season) as Income_Growth_YOY_Season_delta
	,convert(float, b.Income_Growth_Qtr_Comparable) as Income_Growth_Qtr_Comparable_delta
	,convert(float, b.NPPC_Growth_Qtr_Comparable) as NPPC_Growth_Qtr_Comparable_delta
	,convert(float, b.GP_Margin_Qtr) as GP_Margin_Qtr_delta
	,convert(float, b.GP_Margin_Growth_Qtr_Comparable) as GP_Margin_Growth_Qtr_Comparable_delta
	,convert(float, b.IPS_Qtr) as IPS_Qtr_delta
	,convert(float, b.EPS_Qtr) as EPS_Qtr_delta
	,convert(float, b.ROE_Qtr) as ROE_Qtr_delta
	,convert(float, b.Income_Growth_Pre) as Income_Growth_Pre_delta
	,convert(float, b.NPPC_Growth_Pre) as NPPC_Growth_Pre_delta
	,convert(float, b.NPLNRP_Growth_Pre) as NPLNRP_Growth_Pre_delta
	,convert(float, b.GP_Margin_Growth_Pre) as GP_Margin_Growth_Pre_delta
	,convert(float, b.NP_Margin_Growth_Pre) as NP_Margin_Growth_Pre_delta
	,convert(float, b.Income_Growth_YOY) as Income_Growth_YOY_delta
	,convert(float, b.NPPC_Growth_YOY) as NPPC_Growth_YOY_delta
	,convert(float, b.NPLNRP_Growth_YOY) as NPLNRP_Growth_YOY_delta
	,convert(float, b.GP_Margin_Growth_YOY) as GP_Margin_Growth_YOY_delta
	,convert(float, b.NP_Margin_Growth_YOY) as NP_Margin_Growth_YOY_delta
	,convert(float, b.IPS) as IPS_delta
	,convert(float, b.EPS) as EPS_delta
	,convert(float, b.CFPS) as CFPS_delta
	,convert(float, b.Pre_IPS) as Pre_IPS_delta
	,convert(float, b.Pre_EPS) as Pre_EPS_delta
	,convert(float, b.Pre_CFPS) as Pre_CFPS_delta
	,convert(float, b.YOY_IPS) as YOY_IPS_delta
	,convert(float, b.YOY_EPS) as YOY_EPS_delta
	,convert(float, b.YOY_CFPS) as YOY_CFPS_delta
	,convert(float, b.rPE) as rPE_delta
	,convert(float, b.rPB) as rPB_delta
	,convert(float, b.rPS) as rPS_delta
	,convert(float, b.rPCF) as rPCF_delta
	,convert(float, b.SettlePrice) as SettlePrice_delta
	,convert(float, b.ExecutivesProp) as ExecutivesProp_delta
	,convert(float, b.InstitutionNum) as InstitutionNum_delta
	,convert(float, b.InstitutionProp) as InstitutionProp_delta
	,convert(float, b.RegionScore) as RegionScore_delta
	,convert(float, b.Momentum20Day) as Momentum20Day_delta
	,convert(float, b.Momentum40Day) as Momentum40Day_delta
	,convert(float, b.Momentum60Day) as Momentum60Day_delta
	,convert(float, b.Momentum120Day) as Momentum120Day_delta
	,convert(float, b.Momentum180Day) as Momentum180Day_delta
	,convert(float, b.Momentum240Day) as Momentum240Day_delta
	,convert(float, b.PriceDiff) as PriceDiff_delta
	,convert(float, b.DayDiff) as DayDiff_delta
	,convert(float, b.TurnoverRatio) as TurnoverRatio_delta
	,convert(float, b.AvgTurnoverPrice) as AvgTurnoverPrice_delta
	,convert(float, b.AvgTurnoverPriceFactor) as AvgTurnoverPriceFactor_delta
	,convert(float, b.AvgTurnoverRatio5Day) as AvgTurnoverRatio5Day_delta
	,convert(float, b.AvgTurnoverRatio10Day) as AvgTurnoverRatio10Day_delta
	,convert(float, b.AvgTurnoverRatio20Day) as AvgTurnoverRatio20Day_delta
	,convert(float, b.AvgTurnoverRatio40Day) as AvgTurnoverRatio40Day_delta
	,convert(float, b.AvgTurnoverRatio60Day) as AvgTurnoverRatio60Day_delta
	,convert(float, b.AvgTurnoverRatio120Day) as AvgTurnoverRatio120Day_delta
	,convert(float, b.E_EPS) as E_EPS_delta
	,convert(float, b.E_growth) as E_growth_delta
	,convert(float, b.FreeFloat_Total) as FreeFloat_Total_delta
	,convert(float, b.EPS_CFPS) as EPS_CFPS_delta
	,convert(float, b.AvgTurnoverValue) as AvgTurnoverValue_delta
from advancedb.dbo.FactorMonthlyIndustryStd a
,advancedb.dbo.FactorMonthlyTopBottomDelta b
where a.SecuCode='{0}'
and a.TradingDay=b.TradingDay
and a.createDate=b.createDate
and a.settleDate=b.settleDate
order by a.TradingDay desc


