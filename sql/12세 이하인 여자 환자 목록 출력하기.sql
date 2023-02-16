SELECT pt_name, pt_no, gend_cd, age, IFNULL(TLNO, 'NONE') AS TLNO
from patient
where age <= 12 and gend_cd = 'W'
order by age desc, pt_name asc
