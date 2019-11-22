select distinct IndicatorName
from first_selection
where Topic ilike '%population%'

create table  population_over_65 as
select *
from first_selection
where IndicatorName ilike '%ages 65 and above%'

create table  population_growth as
select *
from first_selection
where IndicatorName ilike '%population growth%'

create table  population_total as
select *
from first_selection
where IndicatorName ilike '%population, total%'

select rank() over (order by Value desc), countryname, year, value
from population_total

--china, india, indonesia, pakistan, bangladesh

create table population_growth_ as
select distinct countryname as Kraj, avg(value) over (partition by countryname) as Sredni_wzrost
from population_growth

create table population_diff_2010_1990 as
select A.year, A. countryname, (A.value - B.value)
from (
     select year, countryname, value
     from population_total
     where year = '2010'
     order by value desc
     ) as A
join (
     select year, countryname, value
     from population_total
     where year = '1990'
     order by value desc
     ) as B on A.countryname = B.countryname
order by 3 desc;