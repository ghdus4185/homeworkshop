# 27 workshop

항상 CDN으로만 사용해왔던 Bootstrap을 이번에는 직접 CSS, JS 파일로 다운로드 받아
Django 프로젝트에 Static 파일로 추가하고 사용해보자.

```python
{% load static %}
<link rel="stylesheet" href="{% static 'static/css/bootstrap.css' %}">
<script src="{% static 'js/bootstrap.js' %}"></script>
```