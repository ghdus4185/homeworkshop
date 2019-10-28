# 26 workshop

아래의 회원가입 페이지는 Django.contrib.auth.forms 모듈의 UserCreationForm 클래
스를 활용한 것이다. 아래와 같은 페이지를 만들기 위하여 views.py와 template
(signup.html)에 작성하여야 하는 코드를 작성하시오.

```python
from django.contrib.auth import UserCreationForm
def signup(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

<form action="" method="POST">
	{% csrf_token %}
	{{form}}
	<input type="submit">
</form>
```