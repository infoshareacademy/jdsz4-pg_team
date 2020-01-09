--creating view consisting of environment-related topics for later usage
create view indicators_countries_years as
    select C.Region, I.CountryName, S.Topic, S.IndicatorName, I.Year, I.Value
    from Indicators I
        join Series S on I.IndicatorName = S.IndicatorName
        join Country C on I.CountryCode = C.CountryCode
    where S.Topic like 'Environment%'
    order by C.Region, I.CountryName;

--checking ammount of topics and distinctive indicators
select count(distinct Topic) from indicators_countries_years;
select count(distinct IndicatorName) from indicators_countries_years;

--creating view for YoY values for all indicators after 1980
create view YoY as
    select CountryName, IndicatorName, year, value,
       (
            (
                Value - (lag(Value) over (partition by CountryName, IndicatorName order by Year))
            )
                /
            (
                lag(Value) over (partition by CountryName, IndicatorName order by Year)
            )
        ) YoY
    from indicators_countries_years
    where year > '1980'
    order by CountryName, IndicatorName, Year;

-- creating view of value change dynamics for all indicators after 1980
create view dynamics as
    select CountryName, IndicatorName, year, value,
        lag(Value) over (partition by CountryName, IndicatorName order by CountryName),
       (Value  / (lag(Value) over (partition by CountryName, IndicatorName order by CountryName))) dynamics
    from indicators_countries_years
    where year > '1980'
    order by CountryName, IndicatorName, Year;
