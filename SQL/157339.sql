-- 참고 https://velog.io/@nsh0310/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4SQL-%ED%8A%B9%EC%A0%95-%EA%B8%B0%EA%B0%84%EB%8F%99%EC%95%88-%EB%8C%80%EC%97%AC-%EA%B0%80%EB%8A%A5%ED%95%9C-%EC%9E%90%EB%8F%99%EC%B0%A8%EB%93%A4%EC%9D%98-%EB%8C%80%EC%97%AC%EB%B9%84%EC%9A%A9-%EA%B5%AC%ED%95%98%EA%B8%B0

-- 코드를 입력하세요
SELECT C.CAR_ID, C.CAR_TYPE, ROUND(C.DAILY_FEE * 30 * (100 - D.DISCOUNT_RATE) / 100, 0) AS FEE
FROM CAR_RENTAL_COMPANY_CAR as C
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as D ON C.CAR_TYPE = D.CAR_TYPE
-- JOIN은 두 테이블만
WHERE C.CAR_ID NOT IN
    (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as H WHERE END_DATE >= '2022-11-01' AND START_DATE < '2022-12-01')
    -- 서브쿼리 사용해서 대여 가능한 자동차 찾기
AND C.CAR_TYPE IN ('SUV', '세단') 
AND D.DURATION_TYPE = '30일 이상'
AND ROUND(C.DAILY_FEE * 30 * (100 - D.DISCOUNT_RATE) / 100, 0) BETWEEN 500000 AND 2000000
-- between 사용
ORDER BY FEE desc, C.CAR_TYPE, C.CAR_ID desc