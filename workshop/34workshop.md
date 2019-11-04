# 32 Workshop

### Problem

#### 다음과 같은 Vue 인스턴스가 있을 때, v-for와 v-if 디렉티브를 활용하여 짝수만 나타나
도록 하는 리스트를 작성하시오.

![1572853371003](34workshop.assets/1572853371003.png)

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <li v-for="number in numbers" v-if="number%2===0">
      {{number}}
    </li>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      },
    })
  </script>
</body>
</html>
```

