# 20 homework


#### 1. School 모델과 Student 모델을 1:N 관계로 설정하려고 한다. models.py의 Student 모델 에서 필요한 코드를 작성하시오.
```python
class Student(models.Model):
    content = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
```



#### 2. Question 모델과 Comment 모델은 1:N 관계를 형성하고 있다. 위와 같은 코드가 있을 때, views.py에서 해당 Question의 모든 Comment를 가져오기 위한 코드를 작성하시오. (단, related_name은 설정하지 않았다고 가정한다.)

```python
from django.shortcuts import render, redirect
from .models import Question

def index(request):
	questions = Question.objects.all()
    context = {
        'questions':questions
    }
	return render('index.html', questions)

question.answer_set.all
```



#### 3. 기본적으로 1:N 관계를 설정할 때, ForeignKey를 이용해서 1에 해당하는 클래스를 지정 한다. 지정한 클래스가 Movie일 때, ForeignKey로 지정된 컬럼의 이름은 무엇인가?

`question_id`

