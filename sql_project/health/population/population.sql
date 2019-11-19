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