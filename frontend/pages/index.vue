<template lang="pug">
  div
    b-row
      b-col(cols="9")
        IntroChart
      b-col(cols="3")
        StartBox
</template>

<script scoped>
import Logo from '~/components/Logo.vue'
import StartBox from '@/components/StartBox.vue'
import IntroChart from '@/components/IntroChart.vue'

export default {
  name: 'home',
  components: {
    StartBox,
    IntroChart,
    Logo
  }
}
</script>

<style scoped>
.sexy_line {
  display: block;
  border: none;
  color: white;
  height: 3px;
  background: black;
  background: -webkit-gradient(
    radial,
    100% 100%,
    0,
    0% 0%,
    1000,
    from(#fff),
    to(rgba(0, 0, 0, 0))
  );
}

.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
