<template lang="pug">
  b-navbar(class="mt-3" toggleable="md" type="dark" variant="dark")
    b-col(cols="7" class="mr-5")
      nuxt-link(to="/")
        h1(class="text-primary") Ballmer's Peak: Party Edition
          span(class="blink") _
    b-col(cols="4" class="text-center")
      span(class="header-menu-sep") [
      nuxt-link(to="/party" active-class="clicked")
        span(class="header-menu-item") Party
      span(class="header-menu-sep") |
      nuxt-link(to="/about" active-class="clicked")
        span(class="header-menu-item") About
      span(class="header-menu-sep") |
      nuxt-link(to="/contact" active-class="clicked")
        span(class="header-menu-item") Contact
      span(class="header-menu-sep") ]
</template>

<script>
export default {
  name: 'navbar',
  data() {
    return {}
  },
  methods: {}
}
</script>

<style lang="less" src="../assets/less/global.less"></style>
