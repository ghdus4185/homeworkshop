# 18 homework


#### 1. 우리가 사용하는 SQLite는 RDBMS에 속한다. RDBMS의 특징을 2가지만 작성하시오.
- 모든 데이터를 2차원 테이블 형태로 표현한다.

- 만들거나 이용하기도 비교적 쉽지만 확장이 용이하다.

- 상호 관련성을 가진 테이블의 집합

  

#### 2. 다음 중 맞으면 T, 틀리면 F를 작성하시오.

1.  RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [  T  ] 
2.  SQL에서 명령어는 대문자로 써야만 동작한다. [  F  ] 
3.  일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [  T  ] 
4.  SQLite에서 dot(.) 으로 시작하는 명령어는 SQL이 아니다. [  T  ] 
5.  한 개의 DB 에는 한개의 테이블만 존재한다. [  F  ]



### 3. 다음 코드의 실행결과로 나타나는 값을 작성하세요. 

```python
sqlite> .nullvalue ‘NULL’  #NULL 값을 NULL로 설정
sqlite> CREATE TABLE ssafy ( 
    …> id INTEGER PRIMARY KEY, 
    …> location TEXT, 
    …> class INTEGER 
    …> ); 
sqlite> INSERT INTO ssafy (id, location) 
	…> VALUES (1, ‘JEJU’); 
sqlite> SELECT class FROM ssafy WHERE id=1;
```

```python
NULL
```

