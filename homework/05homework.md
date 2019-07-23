# 05 homework

# 1. 위와 같은 코드가 fibo.py 파일에 작성되어 있을 때, 아래와 같이 함수를


```python
# from 모듈명 import 어트리뷰트 as 이름
from fibo import fibo_recursion as recursion
recursion(4)
```





## 2. 다음 에러들이 어떠한 경우에 발생하는지 간단하게 작성하시오.



```python
# ZeroDivisionError
num = int(input())
divi = num / 0

# NameError
print(asd)

# TypeError
round('3.5')
print(1 + '등')

# IndexError
my_list = [1,2,3]
my_list[100]

# KeyError
sports = {'soccer': 'messi'}
sports['ronaldo']

# ModuleNotFoundError
import mathasdf

# ImportError
from bs4 import BTS
```