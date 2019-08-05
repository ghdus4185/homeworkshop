# 13 homework

#### 1. Django는 요청에 대한 응답을 할 때, 기본적으로 허용된 도메인으로부터 온 요청에 한해서만 응답을 하도록 설정되어 있다. settings.py 파일에서 특정 도메인을 허용하기 위해 수정해야 하는 변수명을 찾아 작성하시오.

```python
INSTALLED_APPS = [
    'pages',                  # 이 부분을 추가해서 내가 만든 page를 보여줄 수 있게 한다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
#### 2. 주소 ‘/ssafy’로 요청이 들어왔을 때 실행되는 함수가 views.py 파일 안의 ssafy 함수일때, 요청에 응답할 수 있도록 urls.py에 추가하여야 하는 코드를 작성하시오.
```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls), #admin이라는 경로가 들어오면 뒤에꺼를 실행해라
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('greeting/<str:name>', views.greeting),
    path('cube/<int:num>/', views.cube),
    path('mul/<int:num1>/<int:num2>/', views.mul),
    path('dtl/', views.dtl),
    path('christmas/', views.christmas)
]
```


#### 3. Django 서버를 실행하는 명령어를 작성하시오.
`python manage.py runserver`



#### 4. Django는 MTV로 이루어진 Web Framework이다. MTV가 무엇의 약자인지 작성하시오.
```
M Model		테이터를 관리
T Template	사용자가 보는 화면
V View		중관 관리자
```