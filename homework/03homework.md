# 03 homework

## 1. Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.

```python
print() 
abs() 
len() 
list() 
dict()
input()
# 등등 ..
```





## 2. 다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
    
ssafy(name='허준','구미')  

# name에 허준이 들어가고 구미가 또 들어가서 오류가 생긴다
```



## 3. 다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.

```python
def my_func(a,b):
    c = a + b
    print( c )
    
result = my_func(4,7)

# result 값은 11 이다.
```

```python
#파라미터 o & 리턴 o
def my_sum(a, b):
    result = a +b
    return result

total = my_sum(2,3)
print(total)
print(type(total))

#파라미터 x & 리턴 o
def hello():
    return 'hello'

greeting = hello()
print(greeting)
print(type(greeting))

#파라미터 o & 리턴 x
def say(name, age):
    print(f'제 이름은{name}이고, 나이는 {age}살 입니다.')
    
a = say('hoyeon',123)
print(a)  # 사용자가 리턴을 적지 않으면 함수는 None을 반환한다

#파라미터x & 리턴x
def say():
    print('안녕하세요')
    
a = say()
print(a)
```

