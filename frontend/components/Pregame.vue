<template lang="pug">
  div#pregame(class="d-flex flex-column justify-content-between align-content-center")
    b-row
      b-col
        h3(v-if="started") Are you ready, {{userName}}?
        h3(v-else) Pre-game Room "{{roomName}}"
      // TODO b-col(class="align-self-end")
      //  h3 {{playerCount}} players online
    div#playerlist(class="flow-grid")
      PlayerCard(
        v-for="p in players" 
          :key="p.sid" 
          :sid="p.sid" 
          :handle="p.username" 
          :score="p.score"
          :ready="p.ready"
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
              h4(class="mb-0 justify-content-between align-content-center" v-html="quoteText")
              p(class="text-primary mt-2 mb-0") | 
                span(class="text-white") Steve Ballmer
      b-col
        b-btn(
          v-if="!isPartyMaster || (isPartyMaster && started)"
          :disabled="!started"
          block
          size="lg"
          :variant="readyState"
          class="mb-3 h-100"
          @click="ready()"
        ) 
          h2(class="my-0") {{readyText}}
        b-btn(
          v-if="!started && isPartyMaster"
          :disabled="playerCount < 2"
          block
          size="lg"
          variant="warning"
          class="mb-3 h-100"
          @click="start()"
        ) 
          h2(class="my-0") Start?

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
      quoteText: ''
    }
  },
  mounted() {
    this.refreshQuote()
  },
  computed: {
    started: function() {
      return this.$store.state.party.global.state == 'corral'
    },
    isPartyMaster: function() {
      return this.$store.state.party.user.is_party_master
    },
    roomName: function() {
      return this.$store.state.party.global.join_code
    },
    players: function() {
      return this.$store.state.party.global.users
    },
    playerCount: function() {
      return this.players.length
    },
    userReady: function() {
      return this.$store.state.party.user.ready
    },
    userName: function() {
      return this.$store.state.party.user.username
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
    ready() {
      // todo unready?
      this.$api.readyPlayer()
    },
    start() {
      this.$api.startGame()
    },
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
