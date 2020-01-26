<template lang="pug">
  b-card#card(bg-variant="dark" :border-variant="readyColorVariant" class="my-3 mx-4")
    b-row
      b-col(cols="3" align-self="center")
        div(
          class="circle d-flex justify-content-center align-items-center" 
          :style="{ border: `${borderSize} solid ${playercolor}` }"
        )
          h4#lenny(:style="{ color: this.playercolor }") ♥‿♥

      b-col(cols="6" align-self="start")
        h4#handle(class="mt-2 mb-2") {{handle}}
        span#score {{score}} points 
        span#plusScore(:class="`text-${deltaColorClass}`")  (+{{deltaScore}})

      b-col(cols="3" align-self="center")
        div#badge

</template>

<script>
export default {
  name: 'playercard',
  props: {
    color: {
      type: String,
      default: function() {
        return '#fff'
      }
    },
    ready: {
      type: Boolean,
      default: function() {
        return false
      }
    },
    handle: {
      type: String,
      required: true
    },
    score: {
      type: Number,
      default: function() {
        return 0
      }
    },
    deltaScore: {
      type: Number,
      default: function() {
        return 0
      }
    },
    lenny: {
      type: String,
      default: function() {
        return '?'
      }
    }
  },
  data() {
    return {
      borderSize: '3px',
      playercolor: this.color
    }
  },
  computed: {
    started: function() {
      return this.$store.state.party.global.state == 'corral'
    },
    deltaColorClass: function() {
      if (this.deltaScore > 0) {
        return 'info'
      }
      return 'white'
    },
    readyColorVariant: function() {
      if (this.ready) return 'success'
      if (this.started) return 'primary'
      return 'light'
    }
  }
}
</script>

<style lang="scss" scoped>
.circle {
  border-radius: 50%;
  width: 5vw;
  height: 5vw;
  background: transparent;
  border: 3px solid white;
}

#lenny {
  margin: 0 auto;
}

#handle {
  font-weight: bold;
}

#card {
  box-shadow: 3px 2px rgba(0, 0, 0, 0.2);
}

#plusScore {
}
</style>
