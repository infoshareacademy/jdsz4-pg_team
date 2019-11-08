-- HEALTH related topics exploration

-- Number of different topics related to health:
select count(distinct Topic) from first_selection
where topic like '%Health%';
-- 8

--List of distinct topics:
select distinct Topic from first_selection
where Topic like '%Health%';

-- Number of different indicators related to health:
select count(distinct IndicatorName) from first_selection
where topic like '%Health%';
-- 119

-- list of indicators connected to health:
select distinct IndicatorName from first_selection
where topic like '%Health%';

-- Checking top 50 indicator names based on their count:
select count(IndicatorName) ilosc, IndicatorName, Topic from first_selection
where lower(Topic) like '%health%'
group by Topic, IndicatorName
order by ilosc desc
limit 50;

-- 50 most popular indicators transferred to csv.

--Interesting indicators [no_records]:
-- 1 Population, total [903]
-- 2 Population growth (annual %) [902]
-- 3 Birth rate, crude (per 1,000 people) [826]
-- 4 Death rate, crude (per 1,000 people) [822]
-- 5 Improved water source, urban (% of urban population with access) [812]
-- 6 Improved water source (% of population with access) [811]
-- 7 Life expectancy at birth, female (years) [804]
-- 8 Life expectancy at birth, male (years) [804]
-- 9 Health expenditure, total (% of GDP) [548]
-- 10 Health expenditure per capita (current US$) [548]
-- 11 Number of infant deaths [756]
-- 12 Number of under-five deaths [756]
-- 13 Fertility rate, total (births per woman) [804]

--===========================================================
/* Questions to be answered:
   1. How population growth impacts health expenditure?
   2. Which countries expend most/least money amount on their inhabitants?
   3. If water source improvement prevents children and infants from death?
   4. How life expectancy for men and female corresponds to health expenditure?
 */

-- Population, total [903] exploration

select count(case when IndicatorName like 'Population, total' then 1 end) liczba, countryname from first_selection
group by countryname
order by liczba desc;
--21 points for all countries (full dataset)

-- avg, min, max, std_dev for indicator ordered by biggest country descending

select countryname,
       avg(case when indicatorname like 'Population, total' then Value end)::int avg_pop,
       min(case when indicatorname like 'Population, total' then Value end) min_pop,
       max(case when indicatorname like 'Population, total' then Value end) max_pop,
       stddev(case when indicatorname like 'Population, total' then Value end)::int std_dev,
       stddev(case when indicatorname like 'Population, total' then Value end)::numeric /
       avg(case when indicatorname like 'Population, total' then Value end) stddev_to_avg_population from first_selection
group by countryname
order by avg_pop desc;


--Adding info for different countries and chosen indicators
/*
To add basic statistics to indicator table, include following script to join properties
extracted from first_selection.
 */

-- Checking % diffrence in population amount

select * from population_years_full
left join
(select countryname,
       avg(case when indicatorname like 'Population, total' then Value end)::int avg_pop,
       min(case when indicatorname like 'Population, total' then Value end) min_pop,
       max(case when indicatorname like 'Population, total' then Value end) max_pop,
       (max(case when indicatorname like 'Population, total' then Value end) -
       min(case when indicatorname like 'Population, total' then Value end))
           / max(case when indicatorname like 'Population, total' then Value end) *100
       pop_diff_procent,
       stddev(case when indicatorname like 'Population, total' then Value end)::int std_dev,
       stddev(case when indicatorname like 'Population, total' then Value end)::numeric /
       avg(case when indicatorname like 'Population, total' then Value end) stddev_to_avg_population from first_selection
group by countryname) additional_info on countryname = "CountryName"
order by pop_diff_procent desc ;

/*
Population % biggest rise top 5:
- Afganistan (57%)
- Solomon Islands (41%)
- Maldives (40.5%)
- Singapore (40%)
- Papua New Guinea (39%)

Smallest % rise:
- Japan (3.5%)
- Small islands (Tovalu, Tonga, Marshall Islands, Micronesia, Samoa)
- Korea (South) 13%
- China (15%)
- Thailand (15%)

Conclusions:
- Japan has big population problem despite high GDP
- Small islands are having problems to keep their inhabitants.
- China is controlling their population with taxes.
- Afghanistan has the biggest rise thanks to their culture?
- Solomon Islands, Maldives and rising - why are their in opposite to small islands?
- Singapore is expanding fast due to high tech evolution.
- India's % rise is only about 30%, but so much different when we are looking at numbers. :)

*/

-- Checking raw numbers for population difference
select * from population_years_full
left join
(select countryname,
       avg(case when indicatorname like 'Population, total' then Value end)::int avg_pop,
       min(case when indicatorname like 'Population, total' then Value end) min_pop,
       max(case when indicatorname like 'Population, total' then Value end) max_pop,
       (max(case when indicatorname like 'Population, total' then Value end) -
       min(case when indicatorname like 'Population, total' then Value end))
       pop_diff_raw,
       stddev(case when indicatorname like 'Population, total' then Value end)::int std_dev,
       stddev(case when indicatorname like 'Population, total' then Value end)::numeric /
       avg(case when indicatorname like 'Population, total' then Value end) stddev_to_avg_population from first_selection
group by countryname) additional_info on countryname = "CountryName"
order by pop_diff_raw desc ;

/*
 Top 5 biggest rise:
 - India
 - China
 - Pakistan
 - Indonesia
 - Bangladesh

 Top 5 lowest:
 - Tuvalu
 - Marshall Islands
 - Palau
 - Tonga
 - Micronesia

 Sounds familiar?
 */

--Health expenditure for year and countries with basics statistics info
select * from health_expenditure
right join
(select countryname,
avg(case when IndicatorName like 'Health expenditure, total (% of GDP)' then Value end) avg,
       min(case when IndicatorName like 'Health expenditure, total (% of GDP)' then Value end) min,
       max(case when IndicatorName like 'Health expenditure, total (% of GDP)' then Value end) max,
       (max(case when indicatorname like 'Health expenditure, total (% of GDP)' then Value end) -
       min(case when indicatorname like 'Health expenditure, total (% of GDP)' then Value end))
       diff_raw,
       stddev(case when indicatorname like 'Health expenditure, total (% of GDP)' then Value end)::int std_dev,
       stddev(case when indicatorname like 'Health expenditure, total (% of GDP)' then Value end)::numeric /
       avg(case when indicatorname like 'Health expenditure, total (% of GDP)' then Value end) stddev_to_avg from first_selection
group by countryname) additional_info on countryname = "CountryName"
order by avg desc ;

--Comment: Smallest countries spend big part of GDP on health care.

-- Raw numbers:
-- As above but incicator showing expediture in US dollars.

select * from health_expenditure
right join
(select countryname,
avg(case when IndicatorName like 'Health expenditure per capita (current US$)' then Value end) avg,
       min(case when IndicatorName like 'Health expenditure per capita (current US$)' then Value end) min,
       max(case when IndicatorName like 'Health expenditure per capita (current US$)' then Value end) max,
       (max(case when indicatorname like 'Health expenditure per capita (current US$)' then Value end) -
       min(case when indicatorname like 'Health expenditure per capita (current US$)' then Value end))
       diff_raw,
       stddev(case when indicatorname like 'Health expenditure per capita (current US$)' then Value end)::int std_dev,
       stddev(case when indicatorname like 'Health expenditure per capita (current US$)' then Value end)::numeric /
       avg(case when indicatorname like 'Health expenditure per capita (current US$)' then Value end) stddev_to_avg from first_selection
group by countryname) additional_info on countryname = "CountryName"
order by avg desc ;

-- COMMENTS:
-- The most developed countries spend the most amount of US $ on healthcare
-- Better not get sick in countries like Bangladesh, Nepal, Pakistan, Cambodia, India, Myanmar.

-- Questions to be answered:
--    1. How population change impacts health expenditure?

-- Exploring correlations
-- between 'Population growth (annual %)' and 'Health expenditure, total (% of GDP)' for different countries and pop_growth total for different countries in region.

select distinct * from (
select fs.countryname,
        round(sum(fs.Value) over (partition by fs.countryname),5) pop_growth_total,
       corr(fs.Value, health.val) over (partition by fs.countryname) corr_between_pop_growth_and_health_exp
from first_selection fs
left join (select countryname, Year, Value val
    from first_selection
    where IndicatorName = 'Health expenditure, total (% of GDP)') health
    on (health.countryname = fs.countryname and health.Year = fs.Year)
where fs.IndicatorName = 'Population growth (annual %)') corr_val
order by pop_growth_total desc ;

-- Comment: This says nothing interesting, Lets check raw numbers.

-- Exploring correlations between value of 'Population, total' and 'Health expenditure, total (% of GDP)' in reference to avg_population for different countries in region.
select distinct * from (
select fs.countryname,
        round(avg(fs.Value) over (partition by fs.countryname),5) avg_pop,
       corr(fs.Value, health.val) over (partition by fs.countryname) corr_between_total_population_and_health_exp
from first_selection fs
left join (select countryname, Year, Value val
    from first_selection
    where IndicatorName = 'Health expenditure, total (% of GDP)') health
    on (health.countryname = fs.countryname and health.Year = fs.Year)
where fs.IndicatorName = 'Population, total') corr_val
        --order by max_pop_total desc
order by avg_pop desc
;
--Comment:
-- Overall strong positive correlation for bigger countries (also for most countries if data is available)

/* Questions to be answered:
   ..
   2. Which countries expend most/least money amount on their inhabitants?

   Indicator involved:
   - Health expenditure per capita (current US$)
   - Population, total
*/

-- Exploring correlations between value of 'Population, total' and 'Health expenditure per capita (current US$)' in reference to avg_pop for different countries in region.

select distinct * from (
select fs.countryname,
        avg(fs.Value) over (partition by fs.countryname)::integer avg_pop,
       corr(fs.Value, health.val) over (partition by fs.countryname) corr_total_pop_and_health_exp_per_capita_in_US_dol
from first_selection fs
left join (select countryname, Year, Value val
    from first_selection
    where IndicatorName = 'Health expenditure per capita (current US$)') health
    on (health.countryname = fs.countryname and health.Year = fs.Year)
where fs.IndicatorName = 'Population, total') corr_val
order by avg_pop desc;

-- Strong correlation for all countries, so all countries spend more US $ on health for citizens year by year. :)

-- Exploring correlations between value of 'Population, total' and 'Health expenditure per capita (current US$)' in reference to avg_health_exp_per_capita for different countries in region.
select distinct * from (
select fs.countryname,
        avg(health.val) over (partition by fs.countryname)::integer avg_health_exp_per_capita,
       corr(fs.Value, health.val) over (partition by fs.countryname) corr_total_pop_and_health_exp_per_capita_in_US_dol
from first_selection fs
left join (select countryname, Year, Value val
    from first_selection
    where IndicatorName = 'Health expenditure per capita (current US$)') health
    on (health.countryname = fs.countryname and health.Year = fs.Year)
where fs.IndicatorName = 'Population, total') corr_val
order by avg_health_exp_per_capita desc;

-- Similar as in last selection.