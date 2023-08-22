-- 코드를 입력하세요
SELECT FIRST_HALF.FLAVOR
FROM FIRST_HALF JOIN ICECREAM_INFO ON FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
-- FIRST_HALF 의 기본키, ICECREAM_INFO의 기본키이자 외래키 = FLAVOR
WHERE FIRST_HALF.TOTAL_ORDER > 3000
AND ICECREAM_INFO.INGREDIENT_TYPE = 'fruit_based'
ORDER BY FIRST_HALF.TOTAL_ORDER desc;
-- 큰 순서대로 = 내림차순 정렬