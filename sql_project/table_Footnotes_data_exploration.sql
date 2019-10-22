/*======================================================================================*/

-- Table Footnotes data exploration:

pragma table_info(Footnotes);
-- 4 columns, 4 of text type
-- column 'Year' also in text type - to be checked

select * from(Footnotes);
-- displaying all columns

select count(1), count(*) from(Footnotes);
-- checking for null rows (532 415/532 415)

select count(1) year_count, Year
from Footnotes
group by Year
order by year_count desc;
-- Strange and inconsistent year description.
-- If we want to use Footnotes.Year col,
-- data cleaning/data wrangling to year/integer type is suggested.

select count(1) desc_count, Description
from Footnotes
group by Description
order by desc_count desc;
-- Description column describes data sources, estimations, interpolations etc.
-- Col probably refers to different indicators instead of countries.

