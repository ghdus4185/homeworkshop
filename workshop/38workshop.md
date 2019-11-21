# 38workshop

- Axios를 활용하여, 아래 그림과 같이 ‘Get {N} Dogs!’ 버튼을 클릭하면 Dog API URL로
  HTTP 요청을 보내어 임의의 강아지 사진을 지정한 개수만큼 가져와 보여주는 앱을 만
  들어 봅시다.
- 요청을 보낼 API URL은![1574042082505](38workshop.assets/1574042082505.png)
  입니다. 어떠한 형태로 데이터를 가져올 수 있는지 브라우저 주소창에 입력하여 확인해
  보세요.

```html
<template>
  <div id="app">
    <div>
      <select name="" v-model="photo_cnt">
        <option v-for="num in nums" :key="num">{{num}}</option>
      </select>
      <button @click="getAnimalPhoto">Get {{photo_cnt}} Dogs!</button>
    </div>
    <img v-for="(url, idx) in photo_urls" :key="idx" :src="url" alt="">
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
      nums: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    photo_cnt: '',
    photo_urls: []
    }
  },
  methods: {
    getAnimalPhoto(){
      const URL = `https://dog.ceo/api/breeds/image/random/${this.photo_cnt}`
      axios.get(URL)
      .then((res)=>{
        console.log(res)
        this.photo_urls = res.data.message
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

