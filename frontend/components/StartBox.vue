<template lang="pug">
	div#startContainer
		b-card(bg-variant="primary" border-variant="primary" class="pl-4 pr-4 pt-0 pb-3 mb-3")
			h5(class="text-center align-center pb-3")
				div(class=" align-center")
					span(class="header-menu-item") [start | join] 
					b-tooltip(
						target="partyTooltip" 
						triggers="hover"
						max-width="200px"
						placement="bottom"
						delay="100"
						custom-class="note"
					) {{ tooltip }}
					span#partyTooltip (?)
			form(class="needs-validation" novalidate v-on:submit.prevent="startParty")
				div(class="form-group")
					label(for="partyIdInput") @party-id
					input#partyIdInput(
						autofocus
						v-model="partyId" 
						type="text" 
						class="form-control errorInput" 
						aria-describedby="partyIdHelp" 
						placeholder="my-memorable-id"
					)
					small#partyIdHelp(class="form-text") Share this name with your friends!
					div(class="invalid-feedback") Please enter a party ID.
				div(class="form-group")
					label(for="userIdInput") @handle
					input#userIdInput(
						v-model="userId" 
						type="text" 
						class="form-control errorInput" 
						aria-describedby="userIdHelp" 
						placeholder="batman"
					)
					small#userIdHelp( class="form-text") What should we call you?
					div(class="invalid-feedback") Please choose a username.

				small By proceeding you agree to our 
					a(class="underline" v-b-modal.termsModal) terms
					|  and 
					a(class="underline" v-b-modal.privacyModal) privacy policy

				b-btn(
					:disabled="continueDisabled"
					type="submit"
					block
					size="lg"
					variant="primary"
					class="mt-3"
					@click="startParty()"
				) 
					h3(class="my-0") Continue

			b-modal#termsModal(size="xl" title="Terms and Conditions")
				Terms
			b-modal#privacyModal(size="xl" title="Privacy Policy")
				Privacy
</template>

<script>
import Terms from './Terms'
import Privacy from './Privacy'

export default {
  name: 'StartBox',
  components: {
    Terms,
    Privacy
  },
  data() {
    return {
      continueDisabled: false,
      agree: false,
      userId: '',
      partyId: '',
      tooltip: 'New users and parties are created on the fly.'
    }
  },
  methods: {
    startParty() {
      // TODO autogenerate party id
      if (this.validatePartyId() && this.validateUserId()) {
        /*this.$store.dispatch('party/register', {
					router: this.$router,
					api: this.$api,
					userId: this.userId,
					partyId: this.partyId
				})*/
        this.continueDisabled = true
        this.$api
          .register(this.userId, this.partyId)
          .then(() => {
            setTimeout(() => {
              this.$router.push({
                path: '/party'
              })
            }, 500)
          })
          .catch(err => {
            console.err(err)
            this.continueDisabled = false
          })
      } else {
        if (!this.validatePartyId()) {
          this.animateCSS('#partyIdInput', 'shake')
        }
        if (!this.validateUserId()) {
          this.animateCSS('#userIdInput', 'shake')
        }
      }
    },
    textColor(b) {
      if (b) return ''
      return 'permaRed'
    },
    animateCSS(element, animationName, callback) {
      const node = document.querySelector(element)
      node.classList.add('animated', animationName)

      function handleAnimationEnd() {
        node.classList.remove('animated', animationName)
        node.removeEventListener('animationend', handleAnimationEnd)

        if (typeof callback === 'function') callback()
      }

      node.addEventListener('animationend', handleAnimationEnd)
    },
    validatePartyId() {
      return !!this.partyId
    },
    validateUserId() {
      return !!this.userId
    }
  },
  computed: {}
}
</script>

<style lang="less" src="../assets/less/global.less"></style>

<style scoped lang="scss">
.errorInput {
  animation-duration: 0.5s;
  animation-delay: 0s;
  animation-iteration-count: 1;
}
.startContainer {
  min-width: 400px;
}
</style>
