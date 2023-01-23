SELECT name, count(name) count
from animal_ins
group by name
having count(name) > 1
order by name 
