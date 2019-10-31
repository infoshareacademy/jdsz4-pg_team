--Wskazówka do tworzenia tabel z indykatorem:

-- 1. Wywołujecie komendę, która daje wam dostęp do modułu tablefunc
CREATE EXTENSION IF NOT EXISTS tablefunc;

-- 2. Następnie tworzycie tabelę z interesujacym Was indykatorem:
create table health_expenditure as -- tutaj nazwa tworzonej tabeli XXX
SELECT *
FROM   crosstab(
   'SELECT CountryName, year, value
    FROM   first_selection
    WHERE IndicatorName = ''Health expenditure, total (% of GDP)'' -- nazwa indykatora w podwójnym ''
    ORDER  BY 1,2'

    ,$$SELECT unnest('{1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010}'::text[])$$
   ) AS ct ("CountryName" text, "1990" numeric, "1991" numeric, "1992" numeric, "1993" numeric,
            "1994" numeric, "1995" numeric, "1996" numeric, "1997" numeric, "1998" numeric, "1999" numeric, "2000" numeric,
            "2001" numeric, "2002" numeric, "2003" numeric, "2004" numeric, "2005" numeric,
            "2006" numeric, "2007" numeric, "2008" numeric, "2009" numeric, "2010" numeric);
