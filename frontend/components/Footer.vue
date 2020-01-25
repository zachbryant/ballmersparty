<template lang="pug">
  footer(class="footer")
    b-container(fluid class="container")
      p(class="note") Made with 
        i(class="fa fa-heart" style="font-size:16px;color:white;")
        span(class="note")  at Purdue.
</template>

<style>
.footer {
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px;
  line-height: 60px;
}
</style>
