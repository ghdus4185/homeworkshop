# 17 homework


#### 1. Django Form Class를 만들 때, Django에 내장되어 있는 모듈을 import 하고 해당 모듈 에 정의된 Class를 상속받아야 한다. 해당 모듈을 import 하는 코드를 작성하시오.
```python
from django import forms
from .models import Class_name
```





#### 2.  Form Class를 Template에서 활용하기 위해서 변수 form에 Form Class의 인스턴스를 할당하여 Template으로 전달하였다. Template에서 <p> Tag로 감싸진 form을 렌더링 하기 위한 코드를 작성하시오.

```python
class Meta:
    model = Class_name
    fields = '__all__'
```



### 3. Form Class를 활용할 때, Form에 담긴 데이터가 유효한지 체크하기 위해서 is_valid() 메소드를 활용하였다. 유효성 검사를 통과한 후, 유효한 데이터를 가져오기 위하여 빈칸 (a)에 들어가야하는 코드를 작성하시오. (단, StudentForm Class는 forms.Form을 상속 받았다고 가정한다.)



- (a) = `objects`