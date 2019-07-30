# 09 homework


#### 1. HTML은 무엇의 약자인가? [ ]
- (3) Hyper Text Markup Language


#### 2. 다음 중 맞으면 T, 틀리면 F를 작성 하시오

– 웹 표준을 만드는 곳은 Mozilla 재단이다. [ F ] -> W3D 임
– 표(table) 을 만들 때에는 반드시 <th> 태그를 사용해야 한다. [ F ] -> 반드시는 아님
– 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다. [ T ]
– 인용문을 가리키는 태그는 <blockquote> 이다. [ T ]


#### 3. 보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가된 시맨틱(semantic) 태그를 모두 고르시오.
```python
<header> :  웹페이지의 헤더를 만들 때 사용
<section> : article안에 영역을 구분할 때 사용
<footer> : 웹페이지의 하단을 만들 때 사용
# 추가 
<nav> : 웹페이지의 메뉴를 만들 때 사용, 내부에 <ul>,<li>를 많이 사용 
<article> : 본문을 감싸줄 때 사용, 컨텐츠 영역
<aside> : 페이지 왼쪽이나 오른쪽에 부가적인 내용의 영역에 사용
<hgroup>  : 제목<h1>, 부제목<h2>으로 나눠 쓸 때 제목들을 하나로 묶어줌
```



#### 4. 아래 이미지와 같이 로그인 Form을 생성하는 HTML 코드를 작성하시오

```python
<form action="">
	<label for="name">ID:</label> 
    <input id="name" type="text" name="username"> 
    # 원하는걸 편하게 찾기 위한게 id이다
    # name은 말 그대로 이름을 설정해주는 것
    # id랑 name이랑 역활이 다른다
    <label for="password">PWD:</label>
    <input id="password" type="password" name="password">
    
    <input type="submit">
</form>
```
