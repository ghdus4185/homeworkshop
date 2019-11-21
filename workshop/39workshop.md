# 39workshop

Axios를 활용하여, 아래 그림과 같이 ‘Get Posts’ 버튼을 클릭하면 특정 URL로 HTTP
요청을 보내어 임의의 Post의 리스트를 가져와 보여주는 앱을 만들어 봅시다.
요청을 보낼 URL은 ![1574153930372](39workshop.assets/1574153930372.png) 입니
다. 어떠한 데이터들을 가져올 수 있는지 브라우저 주소창에 입력하여 확인해 보세요.

![1574153977264](39workshop.assets/1574153977264.png)

```html
<template>
  <div id="app">
    <button @click="getData">Get Posts!</button>
    <div class="container">
      <ul>
        <li v-for="(post, idx) in posts" :key="idx"><strong>{{post.title}}</strong> - {{post.body}}</li>
      </ul>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'app',
  components: {
  },
  data() {
    return {
    posts: []
    }
  },
  methods: {
    getData(){
      const URL = `https://jsonplaceholder.typicode.com/posts`
      axios.get(URL)
      .then((res)=>{
        console.log(res)
        this.posts = res.data
      })
      .catch((e)=>{
        console.log(e)
      })
    }
  }
}
</script>

<style>
</style>
```