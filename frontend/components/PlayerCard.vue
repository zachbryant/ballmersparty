<template lang="pug">
  div
    b-row
      b-col
        div(class="circle" v-bind:style="{ border: borderSize solid borderColor }")

      b-col

</template>

<script>
export default {
  name: 'playercard',
  data() {
    return {}
  }
}
</script>

<style lang="scss" scoped>
.circle {
  border-radius: 50%;
  background: transparent;
  border: 3px solid white;
}
</style>
