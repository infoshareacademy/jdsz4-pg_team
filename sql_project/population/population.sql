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


select p.CountryName, p.Year, corr(p.value, abc.value) over (partition by p.CountryName order by p.Year)
from population_over_65 p
join (SELECT CountryName, year, value
    FROM   first_selection
    WHERE IndicatorName = 'GDP per capita (current US$)'
        and Value notnull
    ) as abc on p.CountryName = abc.CountryName
order by 3 desc
