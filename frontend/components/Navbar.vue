<template lang="pug">
  b-navbar(class="mt-3" toggleable="md" type="dark" variant="dark")
    b-col(cols="8")
      nuxt-link(to="/")
        h1 Ballmer's Peak: Party Edition
          span(class="blink") _
    b-col(cols="4" class="text-center")
      span(class="header-menu-sep") [
      nuxt-link(to="/party")
        span(v-bind:class="{ clicked: partyActive }" class="header-menu-item" v-on:click="mpartyActive()") Party
      span(class="header-menu-sep") |
      nuxt-link(to="/about")
        span(v-bind:class="{ clicked: aboutActive }" class="header-menu-item" v-on:click="maboutActive()") About
      span(class="header-menu-sep") |
      //nuxt-link(to="/blog")
        span(v-bind:class="{ clicked: blogActive }" class="header-menu-item" v-on:click="mblogActive()") Blog
      //span(class="header-menu-sep") |
      nuxt-link(to="/contact")
        span(v-bind:class="{ clicked: contactActive }"  class="header-menu-item" v-on:click="mcontactActive()") Contact
      span(class="header-menu-sep") ]
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      partyActive: false,
      aboutActive: false,
      blogActive: false,
      contactActive: false
    }
  },
  methods: {
    clearActive() {
      this.partyActive = false
      this.aboutActive = false
      this.blogActive = false
      this.contactActive = false
    },
    mpartyActive() {
      this.clearActive()
      this.partyActive = true
    },
    maboutActive() {
      this.clearActive()
      this.aboutActive = true
    },
    mblogActive() {
      this.clearActive()
      this.blogActive = true
    },
    mcontactActive() {
      this.clearActive()
      this.contactActive = true
    }
  }
}
</script>

<style lang="less" src="../assets/less/global.less"></style>
