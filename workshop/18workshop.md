# 18 workshop

### 1. 아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 데이터를 입력해 봅시다.

```python
CREATE TABLE bands (
	id INTEGER,
    name TEXT,
    debut INTEGER
);

INSERT INTO bands VALUE(1, 'Queen', 1973);
INSERT INTO bands VALUE(2, 'Coldplay', 1998);
INSERT INTO bands VALUE(3, 'MCR', 2001);

.headers on
.mode column

SELECT * FROM bands;
```

### 2. bands 테이블에서 모든 데이터 레코드의 id와 name만 조회하는 SQL query문을 작성하고 실행하시오.

```python
SELECT id, name FROM bands;
```

### 3. bands 테이블에서 debut가 2000보다 작은 밴드들의 이름만을 조회하는 SQL query문 을 작성하고 실행하시오.

```python
SELECT name FROM bands WHERE debut <= 2000;
```

