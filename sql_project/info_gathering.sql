/*INFO GATHERING FILE*/

/* FIRST SELECTION

We decided to check changes in different indicators for two regions:
- 'South Asia' and 'East Asia & Pacific'
- in period from 1990 to 2010 (since number of indicators below 1990 drops fast)
- for topics related to economy, health, environment and infrastructure.
*/

/*GENERAL INFO:
- 43 countries x 21 years for complete indicator info == 903 points */

/*TOPICS RELATED TO Environment

  Interesting indicators:
--1 Electricity production from renewable sources, excluding hydroelectric (kWh)
--2 change of urban population
--3 CO2 emissions
--4 Electric power consumption (kWh per capita)

--nearly whole region had huge boom of electricity production from renewable sources
--CO2 emission is growing rapidly for the Asian countries
  it grew over 70% for 113 of records, that is 'country - indicator' pairs
--change of urban population also is one of indicators that have biggest growth

 */

/*TOPICS RELATED TO HEALTH:

Interesting indicators [no_records]:
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

Conclusions for: 
-- 1 Population, total [903]
-- 2 Population growth (annual %) [902]

Final:
- Japan has big population problem despite high GDP
- Small islands are having problems to keep their inhabitants.
- China is controlling their population with taxes.
- Afghanistan has the biggest rise thanks to their culture?
- Solomon Islands, Maldives and rising - why are their in opposite to small islands?
- Singapore is expanding fast due to high tech evolution.
- India's % rise is only about 30%, but so much different when we are looking at numbers. :)

Conclusions for: 
-- 9 Health expenditure, total (% of GDP) [548]
-- 10 Health expenditure per capita (current US$) [548]

Final:
- Smallest countries spend big part of GDP on health care.
- More developed countries spend the most amount of US $ on healthcare
- Better not get sick in countries like Bangladesh, Nepal, Pakistan, Cambodia, India, Myanmar (spending very small US dollars per citizen).

=========================================================== 

Questions to be answered:
   1. How population growth impacts health expenditure?

Explored correlation between value of 'Population, total' and 'Health expenditure, total (% of GDP)' in reference to avg_population.
Overall strong positive correlation for bigger countries (also for most countries if data is available).

   2. Which countries expend most/least money amount on their inhabitants?

Strong correlation between value of 'Population, total' and 'Health expenditure per capita (current US$)' in reference to avg_pop for 
all countries spend more US $ on health for citizens year by year. The winner is Japan, with mo other countries even close.

   3. If water source improvement prevents children and infants from death?

Strong negative correlation between value of 'Improved water source' and 'Number of infant deaths' in reference to avg_num_infants_dead for most countries.
If water is accessible in different areas, the risk of infant death goes down.
Positive correlation can be seen in war zones (Afghanistan), isolated countries (North Korea), and in small countries (lack of good health care?).

   4. How life expectancy for men and female corresponds to health expenditure?

Explored correlation between value of 'Health expenditure per capita (current US$)' and 'Life expectancy at birth, female / male (years)' 
in reference to avg_life_exp_fem for different countries in region:
-- Strong correlation - the longer citizens are expected to live, the higher health expenditure per capita.
-- This correlation for male is not as strong as for female citizens (about 0.7 vs 0.8)
*/

/*TOPICS RELATED TO INFRASTRUCTURE

  Interesting indicators [no_records]:
--1 Air transport, freight (million ton-km) [618]
--2 Air transport, passengers carried [651] 
--3 Container port traffic (TEU: 20 foot equivalent units) [189] 
--4 Fixed broadband subscriptions (per 100 people) [294]
--5 Fixed telephone subscriptions (per 100 people) [860]
--6 Internet users (per 100 people) [675]
--7 Liner shipping connectivity index (maximum value in 2004 = 100) [238]
--8 Mobile cellular subscriptions (per 100 people) [848]
--9 Pump price for diesel fuel (US$ per liter) [205]
--10 Pump price for gasoline (US$ per liter) [206]
--11 Quality of port infrastructure, WEF (1=extremely underdeveloped to 7=well developed and efficient by international standards) [78]
--12 Rail lines (total route-km) [256]
--13 Railways, goods transported (million ton-km) [263]
--14 Railways, passengers carried (million passenger-km) [269]

Conclusions:
- About half of interesting indicators don't have enough records.

=========================================================== 

Questions to be answered:
   1. Passengers and freight in air transport, container port traffic and railways.
   2. Length of rail lines.
   3. Liner shipping connectivity vs quality of port infrastructure.
   4. Gasoline vs diesel price.
   5. Number of internet, phone and mobile phone users.
   6. Other indicators (R&D, high-tech and ICT goods import/export)?
 */
