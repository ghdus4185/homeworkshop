# 21 homework


#### 1. Question 모델과 Comment 모델이 1:N 관계를 형성하고 있을 때, 하나의 Question을 보여주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html 파일 이 있을 때, 모든 Comment의 content를 h3 태그를 이용하여 출력하는 for문을 작성하 시오. (단, related_name은 설정하지 않았다고 가정한다.)
```python
{% extends 'base.html' %}
{% block body %}
	{% for comment in question.comment_set.all %}
		<h3>{{comment.content}}</h3>
	{% endfor %}
{% endblock %}

```



#### 2. 다음과 같은 urls.py 파일이 있을 때, comment를 작성하는 폼을 만들기 위하여 form 태그 안에 action 속성값으로 넣어야 하는 경로를 작성하시오.

```python
{% extends 'base.html' %}
{% block body %}
  <div class="container w-50 my-3">
    <form action="{% url 'questions:comments_create' question.id %}" method="POST">
      {% csrf_token %}

    </form>
  </div>
{% endblock %}

```
