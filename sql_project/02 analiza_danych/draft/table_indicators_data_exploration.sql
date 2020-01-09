/*======================================================================================*/

-- Table Indicators data exploration:

pragma table_info(Indicators);
-- 6 columns, 4 of text type, year in integer, indicator value in numeric

select * from(Indicators);
-- displaying all columns

select count(1), count(*) from(Indicators);
-- checking for null rows (5 656 458/5 656 458)

select count(IndicatorCode) indi_code,
       count(IndicatorCode) = count(IndicatorName) is_equal_to_name,
       IndicatorName
from Indicators
group by IndicatorName
order by indi_code desc;

-- Checking 500 most used indicators,
-- code and name are equal (no typos apparently).
-- Most popular indicators are connected to (e.g.):
-- * population, land area, mortality, merchandise exports, CO2 emissions
-- * GDP per capita, GNI, Inflation, Trade, Imports ...

select count(Year) no_years, Year from Indicators
group by Year
order by no_years desc;

-- Most data from year 2010, the least data from 2015 (added later)?
-- Overall strong correlation: the earlier year, the less data we have.
