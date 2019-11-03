---------------------------------------------------------------------

select CountryName, IndicatorName, variance(value) as wariancja, stddev(value)/avg(Value), stddev(value), count(1)
from environment_selection
where value != 0
    and topic not like 'Environment: Fres%'
    and topic not like 'Environment: Land%'
    and Topic not like 'Environment: Density%'
    and Topic not ilike 'Environment: Agricul%'
group by CountryName, IndicatorName
having stddev(value) is not null and count(1)>10
order by 3 desc;

--Electricity production from renewable sources, excluding hydroelectric (kWh)
-- jest to wskaznik dla ktorego wariancja jest najwyzsza, czyli wystapila najwieksza ilosciowa zmiana

select CountryName, IndicatorName, variance(value) as wariancja, stddev(value)/avg(Value), stddev(value), count(1)
from environment_selection
where value != 0
    and topic not like 'Environment: Fres%'
    and topic not like 'Environment: Land%'
    and Topic not like 'Environment: Density%'
    and Topic not ilike 'Environment: Agricul%'
group by CountryName, IndicatorName
having stddev(value) is not null and count(1)>10
order by 4 desc;

-- Po sprawdzeniu kolejnosci wedlug stosunku odchylenia do sredniej, wciaz jest to jeden z czynnikow o najwyzszym wskazniku.

-- kwartyle dla wskaznika 'Electricity production from renewable sources, excluding hydroelectric (kWh)'
select CountryName, IndicatorName,
       percentile_disc(array[0.25, 0.5, 0.75])
           within group (order by Value) as kwartyle
from environment_selection
where CountryName = 'China' -- country
  and IndicatorName like 'Electricity production from renewable sources, excluding hydroelectric (kWh)' --indicator
group by 1, 2

--jest to rozklad lewostronny
----------------------