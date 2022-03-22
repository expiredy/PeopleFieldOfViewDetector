<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <img src="https://c.tenor.com/yix4n2xax3kAAAAC/blackhout-one-piece.gif">
    <h2>Wanna hear a joke?</h2>
    <h6>Your mom</h6>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'

@Options({
  props: {
    msg: String
  }
})
export default class HelloWorld extends Vue {
  msg!: string
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
