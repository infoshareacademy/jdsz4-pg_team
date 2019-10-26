create table first_selection as
select C.Region, I.CountryName, S.Topic, S.IndicatorName, I.Year, I.Value
    from Indicators I
        join Series S on I.IndicatorName = S.IndicatorName
        join Country C on I.CountryCode = C.CountryCode
     where year >= '1990'
               and year <= '2010'
        and (region is 'South Asia'
            or region is 'East Asia & Pacific')
               and (topic like 'Economic Policy & Debt:%'
                or topic like 'Environ%'
                or Topic like 'Health%'
                or topic like 'Infrastructure%')
    order by C.Region, I.CountryName, year desc;

