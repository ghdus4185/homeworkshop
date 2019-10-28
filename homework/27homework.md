# 27 Homework

#### 1. attachment 컬럼에 파일을 저장하려고 한다. 아래의 빈 칸 (a)에 정의해야 하는 field를 작성하시오.

```python
class Post(models.Model):
    attachment = models.(a)
```

**(a) : `FileField()`**



#### 2. 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 내부의 ‘/uploaded_files’로 지정하고자 한다. 이 때, settings.py에 작성해야 하는 설정 2가지와이것이 의미하는 바를 간략하게 작성하시오.

**settings.py**

```python
MEDIA_ROOT= os.path.join(BASE_DIR, 'uploaded_files')
MEDIA_URL='/media/'
```

**MEDIA_ROOT** : 파일의 위치

**MEDIA_URL** : 사용자가 요청하는 url 경로



#### 3. 개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더 내부의 ‘/assets’에 있다. ‘이 폴더 안에 Static 파일이 있다.’라고 Django 프로젝트에게 알려주기 위하여 settings.py에 작성해야 하는 설정을 작성하시오.

**setting.py**

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]
```




