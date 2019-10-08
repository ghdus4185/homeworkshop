# 19 homework

### 1. 다음과 같은 스키마를 가지는 데이터베이스 테이블 friends를 생성하시오.

```python
CREATE TABLE friends (
	id INTEGER,
    name TEXT,
    location TEXT
);
```

### 2. 해당 테이블에 다음과 같이 데이터를 입력하시오.

```python
INSERT INTO friends VALUES(1, Justin, Seoul)
INSERT INTO friends VALUES(2, Simon, New York)
INSERT INTO friends VALUES(3, Chang, Las Vegas)
INSERT INTO friends VALUES(4, John, Sydney)
```

### 3. 스키마를 다음과 같이 변경하시오.

```python
ALTER TABLE friends ADD COLUMN created_at marride INTEGER;
```

### 4. 데이터를 다음과 같이 추가하시오.

```python
INSERT INTO friends(marride) VALUES(1)
INSERT INTO friends(marride) VALUES(0)
INSERT INTO friends(marride) VALUES(0)
INSERT INTO friends(marride) VALUES(1)
```



