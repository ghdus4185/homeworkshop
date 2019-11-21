# 35workshop

- v-on 디렉티브를 활용하여, 다음과 같이 ‘+1’ 버튼을 누르면 숫자가 하나씩 증가하는
Counter 앱을 만들어 봅시다.

```html
<template>
  <div id="app">
    <button @click="countUp">+1</button>
    <p>Counter: {{count}}</p>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  },
  data() {
    return {
      count: 0
    }
  },
  methods: {
    countUp (){
      this.count ++
    }
  }
}
</script>

<style>
</style>

```