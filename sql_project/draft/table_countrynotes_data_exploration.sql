/*======================================================================================*/

-- Table CountryNotes data exploration:

pragma table_info(CountryNotes);
-- 3 columns, 3 of text type

select * from CountryNotes;
-- showing all columns

select count(1), count(*) from CountryNotes;
-- checking for null rows (4857/4857)

select count(*) desc_amount, Description
from SeriesNotes
group by Description
order by desc_amount desc ;

-- Table CountryNotes is kind of information table and contains:
-- * Countrycode the same as CountryCode in Country table
-- * Seriescode the same as SeriesCode in different tables (to be checked which ones)
-- * Description column describes data sources, performed estimations, interpolations etc.

-- GENERAL NOTE:
-- CountryCode nad SeriesCode names are written in inconsistent notations in tables,
-- probably due to different people working on DB.
-- Table Footnotes also in different notation.
-- Want to change it?

