select CountryName, IndicatorName, variance(value) as wariancja, stddev(value)/avg(Value), stddev(value), count(1)
from environment_selection
where value != 0
    and topic not like 'Environment: Fres%'
    and topic not like 'Environment: Land%'
    and Topic not like 'Environment: Density%'
    and Topic not ilike 'Environment: Agricul%'
group by IndicatorName, CountryName
having stddev(value) is not null and count(1)>10
order by 3 desc;

--Electricity production from renewable sources, excluding hydroelectric (kWh)
-- variance for this indicator is the highest

select CountryName, IndicatorName, variance(value) as wariancja, stddev(value)/avg(Value), topic, stddev(value), count(1)
from environment_selection
where value != 0
    and topic not like 'Environment: Fres%'
    and topic not like 'Environment: Land%'
    and Topic not like 'Environment: Density%'
    and Topic not ilike 'Environment: Agricul%'
    and Topic not ilike 'Environment: Biodiv%'
group by topic, CountryName, IndicatorName
having stddev(value) is not null and count(1)>10
order by 4 desc;

-- after checking the stddev(value)/avg(Value) this is still one of highest indicators - definitely worth looking at

-- quartills for indicators  'Electricity production from renewable sources, excluding hydroelectric (kWh)'
select CountryName, IndicatorName,
       percentile_disc(array[0.25, 0.5, 0.75])
           within group (order by Value) as kwartyle
from environment_selection
where CountryName = 'China' -- country
  and IndicatorName like 'Electricity production from renewable sources, excluding hydroelectric (kWh)' --indicator
group by 1, 2
----------------------

--created more complex and I believe more informative select

select countryname, IndicatorName,
    avg(Value),
    min(Value) ,
    max(Value) ,
    ( max(Value) - min(Value) ) as difference,
    ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end),
                                                --used case not to have situations with division by zero
    stddev(Value),
    variance(value)
from environment_selection
--where IndicatorName ilike 'Electricity production from renewable sources, excluding hydroelectric (kWh)'
group by 1, 2
order by 6 desc

--difference between min and max divided by max, shows the percentage change,
-- as we can see, nearly whole region had huge boom of electricity production from renewable soursec

select countryname, IndicatorName,
    avg(Value),
    min(Value) ,
    max(Value) ,
    ( max(Value) - min(Value) ) as difference,
    ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end),
                                                --used case not to have situations with division by zero
    stddev(Value),
    variance(value)
from environment_selection
where IndicatorName ilike 'Electricity production from renewable sources, excluding hydroelectric (kWh)'
group by 1, 2
order by 6 desc
--------------------

--change of urban population also is one of indicators that have biggest growth
-- let's check if it matters by creatign corelation with general population growth

select countryname, IndicatorName,
    avg(Value),
    min(Value) ,
    max(Value) ,
    ( max(Value) - min(Value) ) as difference,
    ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end),
                                                --used case not to have situations with division by zero
    stddev(Value),
    variance(value)
from environment_selection
where IndicatorName = 'Urban population'
group by 1, 2
order by 6 desc

--------------------

--CO2 emissions are growing rapidly for the Asian countries

select countryname, IndicatorName,
    avg(Value),
    min(Value) ,
    max(Value) ,
    ( max(Value) - min(Value) ) as difference,
    ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end),
                                                --used case not to have situations with division by zero
    stddev(Value),
    variance(value)
from environment_selection
where IndicatorName ilike 'CO2%'
group by 2,1
having ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end) notnull
order by 7 desc

--the emissions grew over 70% for 113 of records, that is 'country - indicator' pairs

select count(*)
    from
        (select countryname, IndicatorName,
            avg(Value),
            min(Value) ,
            max(Value) ,
            ( max(Value) - min(Value) ) as difference,
            ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end),
                                                --used case not to have situations with division by zero
            stddev(Value),
            variance(value)
        from environment_selection
        where IndicatorName ilike 'CO2%'
        group by 2,1
        having ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end) notnull
           and ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end) > 0.7
        order by 7 desc) as CO2

----------------------------
create table support1 as
select countryname, IndicatorName,
            avg(Value),
            min(Value) ,
            max(Value) ,
            ( max(Value) - min(Value) ) as difference,
            ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end),
                                                --used case not to have situations with division by zero
            stddev(Value),
            variance(value)
        from environment_selection
        where IndicatorName ilike 'CO2%'
        group by 2,1
        having ( max(Value) - min(Value) ) / max(case when Value != 0 then Value end) notnull
        order by 7 desc

--created supporting table
git sta