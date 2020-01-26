<template lang="pug">
  b-card#card(bg-variant="dark" :border-variant="readyColorVariant" class="my-3 mx-4")
    b-row
      b-col(cols="3" align-self="center")
        div(
          class="circle d-flex justify-content-center align-items-center" 
          :style="{ border: `${borderSize} solid ${color}` }"
        )
          h5#lenny(:style="{ color: `${color}` }") {{lenny}}

      b-col(cols="6" align-self="start")
        h4#handle(class="mt-2 mb-2") {{handle}}
        span#score {{score}} points 
        span#plusScore(:class="`text-${deltaColorClass}`")  (+{{deltaScore}})

      b-col(cols="3" align-self="center")
        div#badge

</template>

<script>
import lennys from '@/assets/lenny'

export default {
  name: 'playercard',
  props: {
    sid: String,
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
    }
  },
  methods: {
    hash(sid) {
      var hash = 0,
        i,
        chr
      if (sid.length === 0) return hash
      for (i = 0; i < sid.length; i++) {
        chr = sid.charCodeAt(i)
        hash = (hash << 5) - hash + chr
        hash |= 0 // Convert to 32bit integer
      }
      return hash
    }
  },
  data() {
    return {
      borderSize: '3px',
      playercolor: this.color
    }
  },
  computed: {
    lenny: function() {
      let h = this.hash(this.handle)
      if (h < 0) h *= -1
      let ind = h % lennys.length
      return lennys[ind]
    },
    color: function() {
      let h = this.hash(this.handle)
      if (h < 0) h *= -1
      let r = (h & 0xff0000) % 255,
        g = (h & 0x00ff00) % 255,
        b = (h & 0x0000ff) % 255
      console.log(r)
      console.log(g)
      console.log(b)
      return `rgb(${r}, ${g}, ${b})`
    },
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
  width: 5.5vw;
  height: 5.5vw;
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
