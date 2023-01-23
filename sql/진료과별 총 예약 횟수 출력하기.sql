SELECT MCDP_CD 진료과코드, count(MCDP_CD) 5월예약건수
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, "%Y-%m") = '2022-05'
GROUP BY 진료과코드
ORDER BY 5월예약건수 asc, 진료과코드 asc;
