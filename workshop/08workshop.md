# 08 workshop

#### Flask에서 Dictionary 자료형을 이용하여 다음 조건을 만족하는 ‘나만의 영어 단어장’ 페이지를 만들어보세요.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/dictionary/<string:word>")
def dictionary(word):
    my_fruits = {
        "apple":'사과'
    }

    if word in my_fruits:
        return f"{word}은(는) {my_fruits[word]}!"
    else:
        return f"{word}은(는) 나만의 단어장에 없는 단어입니다!"
```
