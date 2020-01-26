<template lang="pug">
  div#party(class="d-flex flex-column justify-content-between align-content-center")
    Pregame(v-if="showPregame")
    Game(v-else)
    b-btn(
      @click="showPregame = !showPregame"
    ) toggle pregame

</template>

<script>
import Pregame from '@/components/Pregame.vue'
import Game from '@/components/Game.vue'

export default {
  name: 'party',
  components: {
    Pregame,
    Game
  },
  props: {},
  data() {
    return {
      showPregame: true
    }
  },
  computed: {}
}
</script>

<style lang="scss" scoped>
#party {
  min-height: 100%;
}
</style>
