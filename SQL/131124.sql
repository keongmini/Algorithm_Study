-- 참고: https://velog.io/@kyky7896/ORACLE-SQL-%EA%B7%B8%EB%A3%B9%EB%B3%84-%EC%A1%B0%EA%B1%B4%EC%97%90-%EB%A7%9E%EB%8A%94-%EC%8B%9D%EB%8B%B9-%EB%AA%A9%EB%A1%9D-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0

-- 코드를 입력하세요
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS M
JOIN REST_REVIEW AS R ON M.MEMBER_ID = R.MEMBER_ID
WHERE R.MEMBER_ID =
    -- mysql - IN 연산자 대신 = 사용하기
    (SELECT MEMBER_ID FROM REST_REVIEW GROUP BY MEMBER_ID ORDER BY COUNT(MEMBER_ID) desc LIMIT 1)
    -- 서브쿼리 - Group by로 묶은 후에 갯수 세서 가장 많이 작성한 사람 찾기
ORDER BY REVIEW_DATE, R.REVIEW_TEXT