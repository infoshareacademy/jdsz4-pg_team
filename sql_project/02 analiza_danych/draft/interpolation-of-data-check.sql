---checikng where the interpolation of data appeared
select distinct topic
from series
full join seriesnotes s on series.seriescode = s.seriescode
where (description ilike '%inter%');
---subtopics: 'Health: Reproductive health' and 'Health: Mortality'

