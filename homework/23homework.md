# 23 Homework

#### 1. Django에서 Database에 값을 일괄 삽입하기 위하여 Fixture 기능을 이용한다. Fixture파일은 기본적으로 각각의 app 폴더 안의 fixtures 폴더에 위치해야 하며, 파일 형식은(a) 또는 (b)를 사용한다.

**(a) json**

**(b) YAML**

#### 2. D23 Workshop과 같이 Database에 데이터가 저장되어 있을 때, Django Fixture 기능을 이용하여 아래와 같은 yaml형식의 Fixture 파일을 만들려고 한다. 입력해야 하는 명령어를 작성하시오. (단, 파일 이름은 person.yaml로 한다.)

person.yaml

```
-model: myapp.person
 pk: 1
 fields:
 	 first_name: John
	 last_name: Lennon
-model: myapp.person
 pk: 2
 fields:
 	 first_name: Paul
	 last_name: McCartney
	
```

명령어 타이핑 전

`pip install pyyaml`

`python manage.py dumpdata --format=yaml > person.yaml `