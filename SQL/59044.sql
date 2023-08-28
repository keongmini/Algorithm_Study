-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS as I
LEFT JOIN ANIMAL_OUTS as O ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3