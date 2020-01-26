<template lang="pug">
  div#party(class="d-flex flex-column justify-content-between align-content-center")
    transition(name="fade" mode="out-in")
      Pregame(v-if="showPregame")
      Game(v-if="playingRound")
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
    return {}
  },
  computed: {
    playingRound() {
      let state = this.$store.state.party.global.state
      return state === 'round'
    },
    showPregame() {
      let state = this.$store.state.party.global.state
      return state === 'pregame' || state === 'corral'
    }
  }
}
</script>

<style lang="scss">
#party {
  min-height: 100%;
}
</style>
