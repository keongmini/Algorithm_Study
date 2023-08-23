-- 코드를 입력하세요
SELECT 
    DATE_FORMAT(A.SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
    A.PRODUCT_ID,
    A.USER_ID,
    A.SALES_AMOUNT
FROM (
        SELECT *
        FROM ONLINE_SALE

    UNION ALL
    -- 두 테이블 합치기
    
    -- 합칠 때 컬럼 수 동일, 컬럼 순서 동일
        SELECT
            OFFLINE_SALE_ID AS ONLINE_SALE_ID,
            -- 컬럼명 맞춰주기
            NULL AS USER_ID,
            -- 컬럼값 지정 
            PRODUCT_ID,
            SALES_AMOUNT,
            SALES_DATE
        FROM OFFLINE_SALE
    ) AS A
    -- 별명 지정 필수 
WHERE SALES_DATE LIKE '2022-03%'
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID


-- 참고 https://eunsun-zizone-zzang.tistory.com/95