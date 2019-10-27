-- Table Country data exploration:

pragma table_info(Country);
-- 31 columns, 27 of text type, last 3 numeric

select * from Country;
-- showing all columns

select count(1), count(*) from Country;
-- checking for null rows (247/247)

select DISTINCT ShortName from Country;
-- list of Distinct countries - 247 unique countries
-- No purpose for using Distinct on ShortName in next queries.

select DISTINCT Region from Country;
-- 7 different regions and empty string

-- Countries in 'empty string' region:
select ShortName, LongName from Country
where Region is '';

-- These aren't countries but different aggregations based on income,
-- political connections etc.

select count(case when Region ='' then 1 end) only_aggregations,
       count(case when Region <>'' then 1 end) only_countries,
       count(*) = count(case when Region ='' then 1 end) + count(case when Region <>'' then 1 end) total_rows
from Country;
-- 33 aggregations
-- 214 real countries
-- Total rows: 214+33=247 : True(1) Ok!

--To Be Discussed: Will we drop rows without countries?

-- Number of countries in different regions:
select Region,count(*) no_countries from Country
where Region <> ''
group by Region
order by no_countries desc;

-- Most countries in Europe and Central Asia (57),
-- least countries in North America (3).

-- Currency unit checking, most used:

select count(*) no_coutries, CurrencyUnit from Country
where Region <> '' --remove false coutries
group by CurrencyUnit
order by count(*) desc
limit 10;
--Top 3: euro, dollar, franc.

-- The most used currency name?
select count(case when lower(CurrencyUnit) like '%dollar%' then 1 end) dollar_coutries,
       count(case when lower(CurrencyUnit) like '%euro%' then 1 end) euro_coutries,
       count(case when lower(CurrencyUnit) like '%franc%' then 1 end) franc_coutries
from Country
where Region <> ''; --remove false countries
-- Dollar using countries: 41
-- Number of franc countries vs euro (24-25)

-- Income groups:
select count(1) no_countries, IncomeGroup from Country
where Region <>''
group by IncomeGroup
order by no_countries desc;
-- 5 income groups

-- Lending categories:
select count(1) no_countries, LendingCategory from Country
where Region <>''
group by LendingCategory
order by no_countries desc;
-- none, IBRD, IDA, Blend.

--Government accounting:
select count(1) no_countries, GovernmentAccountingConcept from Country
where Region <>''
group by GovernmentAccountingConcept
order by no_countries desc;
-- Consolidated (95), budgetary(66), unknown (53).

















