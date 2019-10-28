# 22 Workshop

### Problem

#### 데이터베이스에 값을 추가할 때, 아래와 같이 검증하려고 한다. 빈칸 (a)와 (b)에 들어갈 알맞은 코드를 작성하시오.


```python
class Person(models.Model):
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[(a)])
    age = models.IntegerField(validators=[(b)])
```

**(a) : `EmailValidator(message="이메일 형식에 맞지 않습니다.")`**

**(b) : `MinValueValidator(20, message="미성년자는 노노")`**
