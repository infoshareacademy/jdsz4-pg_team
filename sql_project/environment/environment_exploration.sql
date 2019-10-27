--looking through topics and indicators

select distinct topic,indicatorname
from first_selection
where Topic ilike 'environm%'
order by 1;


--created derivative table from first_selection including only Environment topics

create table environment_selection as
    select *
    from first_selection
    where Topic ilike 'environm%'

-----
select *
from environment_selection
where topic not like 'Environment: Fres%'
    and topic not like 'Environment: Land%'
    and Topic not like 'Environment: Density%';
-----



--looking for biggest discrepancies in record using stddev()

select CountryName, Topic, IndicatorName, stddev(value), count(1)
from environment_selection
group by CountryName, Topic, IndicatorName
having stddev(value) is not null
order by 4 desc;

--checking first record :)

select *
from environment_selection
where CountryName = 'China'
  and IndicatorName like 'Electricity production from renewable sources, excluding hydroelectric (k%'
order by Year;

--adding % change colum -> stddev(value)/avg(Value)

select CountryName, IndicatorName, stddev(value)/avg(Value), stddev(value), count(1)
from environment_selection
where value != 0
group by CountryName, Topic, IndicatorName
having stddev(value) is not null and count(1)>10
order by 3 desc;
