# 01 homework

## 1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

```python
import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

- 변수나 함수를 만들 때 여기 있는 것들은 피해야 한다.



## 2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (floating point rounding error) 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

```python
import math
math.isclose(a,b)
```



## 3. 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \ 을 작성하세요.

```python
# 줄바꿈
"|n"
# 탭
"|t"
# |
"||"
```



## 4. “ 안녕, 철수야 ” 를 String Interpolation을 사용하여 출력하세요.

```python
name = '철수'
print(f'안녕, {name}야') 
```



## 5. 다음 중 형변환시 오류가 발생하는 것은? 

```python
# 결과 1) 문자 "1"
# 2) 숫자 30
# 3) 숫자 5 
# 4) 문자열에 뭐가 들어있기 때문에 True
# 5) 3.5는 float 형식이기 때문에 오류 발생
```

