---checking which indicators have something to do wiht GDP
select distinct IndicatorName
from first_selection
where (IndicatorName ilike '%gdp%') and (topic like 'Econ%')
order by 1;
---

---table for GDP per capita (current US$) - Maciek's method
CREATE EXTENSION IF NOT EXISTS tablefunc;
create table economy_gdp as -- tutaj nazwa tworzonej tabeli XXX
SELECT *
FROM   crosstab(
   'SELECT CountryName, year, value
    FROM   first_selection
    WHERE IndicatorName = ''GDP per capita (current US$)'' -- nazwa indykatora w podwójnym ''
    ORDER  BY 1,2'

    ,$$SELECT unnest('{1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010}'::text[])$$
   ) AS ct ("CountryName" text, "1990" numeric, "1991" numeric, "1992" numeric, "1993" numeric,
            "1994" numeric, "1995" numeric, "1996" numeric, "1997" numeric, "1998" numeric, "1999" numeric, "2000" numeric,
            "2001" numeric, "2002" numeric, "2003" numeric, "2004" numeric, "2005" numeric,
            "2006" numeric, "2007" numeric, "2008" numeric, "2009" numeric, "2010" numeric);


---stddev for GDP per capita (current US$)
select CountryName, stddev(Value)
from economy_draft2
where (Value is not null) and (IndicatorName like '%GDP per capita (current US%')
group by 1
having stddev(Value) is not null
order by 2 desc;
