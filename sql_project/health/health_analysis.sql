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
group by countryname
order by countryname) additional_info on countryname = "CountryName";
