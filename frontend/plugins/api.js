import Vue from 'vue'
import io from 'socket.io-client'

class Api {
  constructor() {
    this.socket = io('/')
  }

  register(username) {
    return new Promise((resolve, reject) => {
      this.socket.emit('register', { username })
      this.socket.once('registered', data => {
        if (data.success) {
          resolve()
        } else {
          reject(data.error)
        }
      })
    })
  }

  createGame(options) {
    this.socket.emit('create_game', options)
  }

  joinGame(code) {
    this.socket.emit('join_game', { join_code: code })
  }

  onGameState(func) {
    this.socket.on('game_state', func)
  }

  _gameAction(object) {
    this.socket.emit('game_action', object)
  }
}

Vue.prototype.$api = new Api()
