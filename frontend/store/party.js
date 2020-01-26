export const state = () => ({
  global: {
    join_code: '',
    state: '',
    num_rounds_played: 0,
    num_total_rounds: 0,
    users: [{
      username: 'undefined',
      sid: '',
      ready: false,
      score: 0
    }],
    problem: {
      name: '',
      description: ''
    },
    stats: {
      // TODO
    }
  },
  user: {
    username: '',
    ready: false,
    tests_passed: 0,
    tests_failed: 0,
    // TODO user stats
  }
})

export const mutations = {
  updateGameState(state, newState) {
    console.log("update game state: " + newState)
    state.global = newState.global
    state.user = newState.user
  }
}
