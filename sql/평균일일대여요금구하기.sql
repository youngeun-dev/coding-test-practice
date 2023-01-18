SELECT round(avg(daily_fee),0) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
group by car_type
having car_type = "SUV"
