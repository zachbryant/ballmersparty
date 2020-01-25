<template lang="pug">
  div
    div#container
      Navbar
      nuxt(class="pt-4")
    Footer
</template>

<script>
import Navbar from '~/components/Navbar.vue'
import Footer from '~/components/Footer.vue'

export default {
  components: {
    Navbar,
    Footer
  }
}
</script>

<style lang="less">
// This helps align the navbar to 4% padding but fillwidth navbar
body {
  padding-left: 0;
  padding-right: 0;
}

#container {
  padding-left: 4%;
  padding-right: 4%;
}
</style>
