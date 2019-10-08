# 21 workshop

```python
<h1>{{question.title}}</h1>
{% if question.answer_set.all %}
 {% for answer in question.answer_set.all %}
    <ul>
    <div class="alert alert-primary" role="alert">
    <li>{{choice.content}}: {{choice.votes}}</li>
        <a href="{% url 'questions:answer_delete' question.id %}" class="btn btn-danger"> 삭제</a>
        <div>
    <ul>
    {% endfor %}
    {% endif %}
```
