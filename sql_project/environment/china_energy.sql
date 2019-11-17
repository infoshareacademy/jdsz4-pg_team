select *
from environment_selection
where IndicatorName = 'Electric power consumption (kWh per capita)'
    and CountryName = 'China'
order by Year;

select CountryName, IndicatorName,
       percentile_disc(array[0.25, 0.5, 0.75])
           within group (order by Value) as kwartyle
from environment_selection
where CountryName = 'China' -- country
  and IndicatorName like 'Electric power consumption (kWh per capita)' --indicator
group by 1, 2;

select *
from environment_selection
where IndicatorName = 'Renewable energy consumption (% of total final energy consumption)'
    and CountryName = 'China'
    order by Year

select *
from environment_selection
where IndicatorName = 'Renewable electricity output (% of total electricity output)'
    and CountryName = 'China'
    order by Year

