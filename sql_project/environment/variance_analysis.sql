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

select countryname, IndicatorName,
       avg(Value),
       min(Value) ,
       max(Value) ,
        ( max(Value) -min(Value) ) difference,
       stddev(Value),
       variance(value)
from environment_selection
--where IndicatorName ilike 'Electricity production from renewable sources, excluding hydroelectric (kWh)'
group by 1, 2
order by 5 desc