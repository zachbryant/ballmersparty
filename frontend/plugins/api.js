import Vue from 'vue'
import io from 'socket.io-client'

class Api {
  constructor() {
    this.socket = io('/')
  }

  register(username, joincode) {
    return new Promise((resolve, reject) => {
      this.socket.emit('register', {
        username: username.trim(),
        joincode: joincode.trim()
      })
      this.socket.once('registered', data => {
        if (data.success) {
          resolve()
        } else {
          reject(data.error)
        }
      })
    })
  }

  onGameState(func) {
    this.socket.on('game_state', func)
  }

  _gameAction(object) {
    this.socket.emit('game_action', object)
  }
}

Vue.prototype.$api = new Api()
