-- 코드를 입력하세요
SELECT ROUND(AVG(DAILY_FEE), 0) as AVERAGE_FEE
-- 소수점 첫번째 자리에서 반올림 = 소수점 자리 없음
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'