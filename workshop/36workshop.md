# 36workshop

- v-bind 디렉티브의 class 또는 style 전달인자를 사용하여 아래와 같이 ‘Toggle’ 버튼을
클릭 할 때 마다 작성된 문장이 빨강과 파랑으로 변경되도록 하는 앱을 만들어 봅시다.

```html
<template>
  <div id="app">
    <button @click="colorChange">Toggle</button>
    <p :style="{color: activeColor}">빨강과 파랑을 섞으면 보라색이 됩니다.</p>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  },
  data() {
    return {
      activeColor: 'red'
    }
  },
  methods: {
    colorChange (){
      if (this.activeColor === 'red') {
        this.activeColor = 'blue'
      } else {
        this.activeColor = 'red'
      }
    }
  }
}
</script>

<style>
</style>
```