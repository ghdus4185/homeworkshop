# 21 workshop

```python
<h1>{{question.title}}</h1>
{% if question.answer_set.all %}
 {% for answer in question.answer_set.all %}
    <div class="alert alert-primary" role="alert">
    {{choice.content}}: {{choice.votes}}
        <a href="{% url 'questions:answer_delete' question.id %}" class="btn btn-danger"> 삭제</a>
        <div>
    {% endfor %}
    {% endif %}
```
