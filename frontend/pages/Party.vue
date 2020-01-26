<template lang="pug">
  div#party(class="d-flex flex-column justify-content-between align-content-center")
    div#playerlist(class="flow-grid")
      PlayerCard(
        v-for="p in players" 
          v-bind:key="p.uuid" 
          v-bind:handle="p.handle" 
          v-bind:score="p.score"
          v-bind:color="p.color"
          v-bind:lenny="p.lenny"
      )
    b-row
      b-col
        b-card#quoteContainer
          b-row
            b-col(cols="1" class="ml-3 mr-2")
              h3(class="fa fa-quote-left text-primary")
            b-col(cols="10")
              h4(class="mb-0 justify-content-between align-content-center" ) All in, baby! We are winning, winning, winning, winning.
              p(class="text-primary mt-2 mb-0") | 
                span(class="text-white") Steve Ballmer
      b-col
        b-btn(
          block
          size="lg"
          variant="primary"
          class="mb-3 h-100"
        ) 
          h2(class="my-0") READY

</template>

<script>
import PlayerCard from '@/components/PlayerCard.vue'

export default {
  name: 'party',
  components: {
    PlayerCard
  },
  props: {
    quote: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      players: [
        {
          uuid: 0,
          handle: 'batman',
          score: 72,
          color: '#FF00FF'
        },
        {
          uuid: 1,
          handle: 'batman',
          score: 72,
          color: '#11bbFF'
        },
        {
          uuid: 2,
          handle: 'batman',
          score: 72,
          color: '#cc4411'
        },
        {
          uuid: 3,
          handle: 'batman',
          score: 72,
          color: '#00FFFF'
        },
        {
          uuid: 4,
          handle: 'batman',
          score: 72,
          color: '#FFFF00'
        }
      ]
    }
  },
  computed: {
    rowCount: function() {
      return this.playerCount / 3
    },
    playerCount: function() {
      return this.players.length
    }
  }
}
</script>

<style lang="scss" scoped>
#party {
  min-height: 100%;
}

#playerlist {
  min-height: 75%;
}

#quoteContainer {
  background: rgba(255, 255, 255, 0.2);
}
</style>
