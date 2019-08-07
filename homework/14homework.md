# 14 homework


#### 1. Django는 MTV로 이루어진 Web Framework이다. MTV가 무엇의 약자인지 작성하시오.
```
M Model		테이터를 관리
T Template	사용자가 보는 화면
V View		중관 관리자
```

#### 2. Django 서버를 실행하는 명령어를 작성하시오.
`django-admin startapp pages`



#### 3. Django는 요청에 대한 응답을 할 때, 기본적으로 허용된 도메인으로부터 온 요청에 한해서만 응답을 하도록 설정되어 있다. settings.py 파일에서 특정 도메인을 허용하기 위해 수정해야 하는 변수명을 찾아 작성하시오.

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

