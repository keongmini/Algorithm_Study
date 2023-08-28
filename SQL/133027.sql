-- 코드를 입력하세요
SELECT F.FLAVOR
FROM FIRST_HALF AS F
JOIN JULY AS J ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
-- 맛을 기준으로 묶기
ORDER BY (SUM(J.TOTAL_ORDER) + SUM(F.TOTAL_ORDER)) desc
-- 묶은 후 값 다 더해서 바로 정렬
LIMIT 3