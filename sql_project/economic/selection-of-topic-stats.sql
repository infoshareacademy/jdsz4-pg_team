---counting distinct indictors corresponding economic topic in first selection table
select distinct count(IndicatorName)
from first_selection
where topic like 'Econ%'
---237622 indicators


---preparing the list of distinc subtopics within economy topics
select distinct count(IndicatorName)s
from economy_draft2
where topic like 'Econ%'
---


---deleting the subtopics that appear to be less intresting
create table economy_draft2 as
select *
from first_selection
where topic like 'Econ%' and
      topic != 'Economic Policy & Debt: External debt: Net transfers' and
      topic != 'Economic Policy & Debt: External debt: Net flows' and
      topic != 'Economic Policy & Debt: External debt: Debt outstanding' and
      topic != 'Economic Policy & Debt: Balance of payments: Reserves & other items' and
      topic != 'Economic Policy & Debt: Balance of payments: Capital & financial account' and
      topic != 'Economic Policy & Debt: Official development assistance' and
      topic != 'Economic Policy & Debt: External debt: Commitments' and
      topic != 'Economic Policy & Debt: Balance of payments: Current account: Goods, services & income' and
      topic != 'Economic Policy & Debt: National accounts: Local currency at constant prices: Value added' and
      topic != 'Economic Policy & Debt: External debt: Debt ratios & other items' and
      topic != 'Economic Policy & Debt: National accounts: US$ at constant 2005 prices: Aggregate indicators' and
      topic != 'Economic Policy & Debt: External debt: Disbursements' and
      topic != 'Economic Policy & Debt: External debt: Currency composition' and
      topic != 'Economic Policy & Debt: National accounts: US$ at current prices: Other items' and
      topic != 'Economic Policy & Debt: National accounts: US$ at constant 2005 prices: Value added' and
      topic != 'Economic Policy & Debt: External debt: Arrears, reschedulings, etc.' and
      topic != 'Economic Policy & Debt: National accounts: US$ at current prices: Value added' and
      topic != 'Economic Policy & Debt: External debt: Amortization' and
      topic != 'Economic Policy & Debt: External debt: Terms' and
      topic != 'Economic Policy & Debt: Balance of payments: Current account: Balances' and
      topic != 'Economic Policy & Debt: External debt: Undisbursed debt' and
      topic != 'Economic Policy & Debt: External debt: Debt service' and
      topic != 'Economic Policy & Debt: External debt: Interest' and
      topic != 'Economic Policy & Debt: National accounts: US$ at constant 2005 prices: Expenditure on GDP' and
      topic != 'Economic Policy & Debt: National accounts: Local currency at current prices: Value added' and
      topic != 'Economic Policy & Debt: Purchasing power parity' and
---      topic != 'Economic Policy & Debt: National accounts: US$ at current prices: Aggregate indicators' and
      topic != 'Economic Policy & Debt: National accounts: Adjusted savings & income' and
      topic != 'Economic Policy & Debt: Balance of payments: Current account: Transfers' and
      topic != 'Economic Policy & Debt: National accounts: Local currency at constant prices: Expenditure on GDP' and
      topic != 'Economic Policy & Debt: National accounts: Local currency at current prices: Expenditure on GDP'
order by topic;
---


---counting distinct indictors in economy_draf2 table
select distinct count(IndicatorName)
from economy_draf2
where topic like 'Econ%'
---54631 indicators


---looking for the indicator with the biggest stddev
select CountryName, IndicatorName, stddev(Value)
from economy_draft2
where Value is not null
group by 1,2
having stddev(Value) is not null
order by 3 desc
---

