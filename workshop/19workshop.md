# 19 workshop


#### 1. 해당 테이블에 다음과 같이 컬럼을 추가하고 데이터를 삽입하시오.
```PYTHON
ALTER TABLE bands
ADD COLUMN members INTEGER;

UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;
```



#### 2. id가 3인 레코드의 members를 5로 수정하는 SQL query문을 작성하고 실행하시오.

```python
UPDATE bands SET members=5 WHRER id=3;
```



#### 3. Id가 2인 레코드를 삭제하는 SQL query를 작성하고 실행하시오.

```	PYTHON
DELETE FROM bands WHERE id=2;
```

