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
INSERT INTO friends 
VALUE(1, Justin, Seoul), 
VALUE(2, Simon, New York), 
VALUE(3, Chang, Las Vegas), 
VALUE(4, John, Sydney);
```

### 3. 스키마를 다음과 같이 변경하시오.

```python
ALTER TABLE friends ADD COLUMN marride INTEGER;
```

### 4. 데이터를 다음과 같이 추가하시오.

```python
UPDATE friends
SET married=1
WHERE id=1;
UPDATE friends
SET married=0
WHERE id=2;
UPDATE friends
SET married=0
WHERE id=3;
UPDATE friends
SET married=1
WHERE id=4;
```



