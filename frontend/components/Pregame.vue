<template lang="pug">
  div#pregame(class="d-flex flex-column justify-content-between align-content-center")
    b-row
      b-col
        h3 Pre-game Room
      // TODO b-col(class="align-self-end")
      //  h3 {{playerCount}} players online
    div#playerlist(class="flow-grid")
      PlayerCard(
        v-for="p in players" 
          v-bind:key="p.uuid" 
          v-bind:handle="p.handle" 
          v-bind:score="p.score"
          v-bind:color="p.color"
          v-bind:lenny="p.lenny"
      )
    // TODO pre-game room status bar
    // Quote and ready elements
    b-row(class="mt-5")
      b-col
        b-card#quoteContainer(@click="refreshQuote()" style="cursor: pointer;")
          b-row
            b-col(cols="1" class="ml-3 mr-2")
              h3(class="fa fa-quote-left text-primary")
            b-col(cols="10")
              h4(class="mb-0 justify-content-between align-content-center" ) {{quoteText}}
              p(class="text-primary mt-2 mb-0") | 
                span(class="text-white") Steve Ballmer
      b-col
        b-btn(
          block
          size="lg"
          :variant="readyState"
          class="mb-3 h-100"
          @click="userReady = !userReady"
        ) 
          h2(class="my-0") {{readyText}}

</template>

<script>
import PlayerCard from '@/components/PlayerCard.vue'
import quotes from '@/assets/quotes'

export default {
  name: 'pregame',
  components: {
    PlayerCard
  },
  props: {},
  data() {
    return {
      quoteText: '',
      userReady: false,
      lobbyReady: false,
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
          deltaScore: 10,
          color: '#FFFF00'
        },
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
        }
      ]
    }
  },
  mounted() {
    this.refreshQuote()
  },
  computed: {
    rowCount: function() {
      return this.playerCount / 3
    },
    playerCount: function() {
      return this.players.length
    },
    readyState: function() {
      if (this.userReady) {
        return 'success'
      }
      return 'primary'
    },
    readyText: function() {
      if (this.userReady) {
        return 'Ready!'
      }
      return 'Ready?'
    }
  },
  methods: {
    refreshQuote() {
      this.quoteText = quotes[Math.floor(Math.random() * quotes.length)]
    }
  }
}
</script>

<style lang="scss" scoped>
#pregame {
  min-height: 100%;
}

#playerlist {
  min-height: 75%;
}

#quoteContainer {
  background: rgba(255, 255, 255, 0.2);
}
</style>
