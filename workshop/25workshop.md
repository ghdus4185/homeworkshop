# 25 workshop

```python
class Article(models.Model):
    title = CharField(max_length=100)
    content = CharField(max_length=100)
    article = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class Hashtag(models.Model):
    content = CharField(max_length=100)
    hashtag = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```