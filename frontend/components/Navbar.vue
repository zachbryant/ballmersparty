<template>
  <div>
    <b-navbar toggleable="md" type="light" variant="light">
      <b-navbar-brand to="/">Balmer Rules</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/" active-class="active">Balmer Sucks</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  methods: {
  },
  computed: {

  }
}
</script>

<style scoped></style>
