<template lang="pug">
  div#party(class="d-flex flex-column justify-content-between align-content-center")
    // TODO smooth transitions here
    Pregame(v-if="showPregame")
    Game(v-else)
    //b-btn(
      @click="showPregame = !showPregame"
      ) toggle pregame

</template>

<script>
import Pregame from '@/components/Pregame.vue'
import Game from '@/components/Game.vue'

export default {
  name: 'party',
  middleware: 'party',
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
  computed: {
    showPregame() {
      return this.$store.state.party.global.state === 'pregame'
    }
  }
}
</script>

<style lang="scss" scoped>
#party {
  min-height: 100%;
}
</style>
