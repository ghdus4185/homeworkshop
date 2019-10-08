# 20 workshop

```python
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=100)

class Answer(models.Model):
    content = models.CharField(max_length=100)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
```

