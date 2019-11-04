# 32 Workshop

### Problem

#### 아래의 주석 내용에 따라 JavaScript 코드를 작성하시오.

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
  <h1>0</h1>
  <button id='change-btn'>Click it</button>
  <script>
  // #change-btn을 button 상수에 할당한다
  const button = document.querySelector('#change-btn')
  // h1 태그를 header 상수에 할당한다
  const header = document.querySelector('h1')
  // clickCount 변수를 0으로 초기화 한다
  let clickCount = 0
  // button에 'click' eventListener를 추가한다. 클릭이 발생하면,
  // clickCount가 1씩 증가한다.
  button.addEventListener('click', (e)=>{
    clickCount ++
  })
  // header 안의 내용을 clickCount로 변경한다.
  header.innerText = clickCount
</script>
</body>
</html>
```

