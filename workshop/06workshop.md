



# 06 workshop

## 아래와 같은 클래스 Circle이 있을 때, 반지름이 3이고 x, y 좌표가 (2, 4)인 원을 만들어 넓이와 둘레를 출력하시오.

##### 클래스 속성

- pi : 3.14

##### 인스턴스 속성(초기화 시 필요한 값들)

- r : 원의 반지름(필수 입력)
- x: x좌표(default 0)
- y: y좌표(default 0)

##### 인스턴스 메서드
- area(): 원의 넓이를 반환
- circumference(): 원의 둘레를 반환
- center(): 원의 중심인(x, y)좌표를 튜플로 반환
- move(x, y): 원의 중심인(x, y)좌표를 입력받은 값으로 변경하고 변경된 좌표값을 퓨플로 반환

```python
class circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)

c1 = circle(3, 2, 4)
print(c1)

print(c1.area())
print(c1.circumference())
print(c1.center())
```