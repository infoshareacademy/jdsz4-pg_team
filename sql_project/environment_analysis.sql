create view indicators_countries_years as
select C.Region, I.CountryName, S.Topic, S.IndicatorName, I.Year, I.Value from Indicators I
join Series S on I.IndicatorName = S.IndicatorName
join Country C on I.CountryCode = C.CountryCode
where S.Topic like 'Environment%'
order by C.Region, I.CountryName;

select Topic from indicators_countries_years


