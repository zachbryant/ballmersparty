<template lang="pug">
  div
    Navbar#navbar
    div#container
      transition(name="fade" mode="out-in")
        nuxt#view(class="pt-4")
    Footer
</template>

<script>
import Navbar from '~/components/Navbar.vue'
import Footer from '~/components/Footer.vue'

export default {
  components: {
    Navbar,
    Footer
  },
  mounted() {
    this.$api.onGameState(response => {
      this.$store.commit('party/updateGameState', response)
    })
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
  min-height: calc(100vh - 60px - 80px);
}

#navbar {
  height: 78px;
}

#view {
  min-height: calc(100vh - 78px - 60px - 60px);
}
</style>
