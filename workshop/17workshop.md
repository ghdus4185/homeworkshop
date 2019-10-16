# 17 workshop

### 1. 학생들의 이름과 나이를 저장하기 위한 Form Class를 정의하려고 한다. 다음과 같이 Student Model이 존재할 때, 해당 Model에 데이터를 입력하기 위하여 가장 적절한 Form Class인 StudentForm Class를 작성하시오.

```python
class StudentFrom(forms.ModelForm)
	class meta:
        model = Student
        field = '__all__'
```

### 2.  views.py의 코드가 다음과 같을 때, new.html에서 위에서 만든 Form Class를 활용하여 Form Tag가 보여지도록 하는 코드를 작성하시오. (사용자가 데이터를 입력하고 Submit 버튼을 누르면 ‘/students/create/’로 요청을 보내며, method는 POST 방식을 사용한다.)

```python
def new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new.html')
    else:
        form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'new.html', context)
```