



# 07 homework

###  다음은 더하기 기능만이 구현된 간단한 Calculator 클래스이다.

#### 1. 인스턴스 메서드, 스태틱 메서드, 클래스 메서드에 해당 하는 함수가 무엇인지 작성하시오.
```python
class Calculator:
    count = 0
    
    def info(self):
        print('나는 계산기  입니다.')
    
    @staticmethod
    def add(a, b):
        Calculator.count += 1
        print(f'{a} + {b} 는 {a+b} 입니다.')
    
    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')
```
```python
- 인스턴스 메서드
  info()
- 스태틱 메서드
  add(a,b)
- 클래스 메서드
  history(cls)
```


####  2. 각각의 함수(메서드)를 실행하는 코드를 작성하시오.

```python
c = Calculator()
c.info()
Calculator.add(1,2)
Calculator.history()
```


#### 3. 파라미터 self와 cls에는 어떤 값이 할당 되는지 작성하시오.

```python
인스턴스 객체 자체가 self 안에 들어간다
class객체가 들어간다
```