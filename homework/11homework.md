# 11 homework


#### 1. 다음은 Bootstrap의 어떤 component인지 작성하고, 아래와 같이 만들기 위해서
어떤 class를 사용해야 하는지 작성하시오.
`button`

`<button type="button" class="btn btn-danger">Danger</button>`


#### 2. 다음은 Bootstrap의 어떤 component인지 작성하고, 아래와 같이 만들어 보시오.

`<div class = "alert alert-info" role="alert"></div>`


#### 3. Bootstrap Grid System은 레이아웃을 ____(A)____개의 column으로, ____(B)____개의 반응형 사이즈 조건을 사용하여 구축한다. (A)와 (B)에 들어갈 내용을 작성하시오.

`12 column`

`4개의 기본 반응형 사이즈 조건`

정확하게는 4개 extra small의 경우 자동으로 size를 조절해주기 때문




#### 4. Bootstrap Grid System을 활용하여, 아래와 같이 만들어 보시오.
(테두리와 배경색은 아래의 코드를 참고하시오.)

```css
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  <style>
    div{
        border: 1px solid block;
    }
    .row{
        background-color: moccasin;
    }
  </style>
  <div class="container">
    <div class="row"></div>
    <div class="col-3">25%</div>
    <div class="col-6">50%</div>
    <div class="col-3">25%</div>
  </div>
</body>
```



