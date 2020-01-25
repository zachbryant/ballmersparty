<template lang="pug">
	div
		b-card(bg-variant="primary" border-variant="primary" class="pl-4 pr-4 pt-0 pb-3 mb-3")
			h5(class="text-center align-center pb-3")
				div(class=" align-center")
					span [ start | join ] 
					b-tooltip(
						target="partyTooltip" 
						triggers="hover"
						max-width="200px"
						placement="bottom"
						delay="100"
						custom-class="note"
					) {{ tooltip }}
					span#partyTooltip (?)
			div(class="form-group")
				label(for="partyIdInput") @party-id
				input#partyIdInput(type="text" class="form-control" aria-describedby="partyIdHelp" placeholder="my-memorable-id")
				small#partyIdHelp(class="form-text") Share this name with your friends!
			div(class="form-group")
				label(for="userIdInput") @handle
				input#userIdInput(type="text" class="form-control" aria-describedby="userIdHelp" placeholder="batman")
				small#userIdHelp( class="form-text") What should we call you?
				
			b-btn(
				block
				size="lg"
				variant="primary"
				class="mb-3"
				@click="startParty()"
			) continue

			small By proceeding you agree to our 
				a(class="underline" v-b-modal.termsModal) terms
				|  and 
				a(class="underline" v-b-modal.privacyModal) privacy policy

			b-modal#termsModal(size="xl" title="Terms and Conditions")
				Terms
			b-modal#privacyModal(size="xl" title="Privacy Policy") Placeholder: You have no right to privacy on any data we collect while you visit this website.
</template>

<script>
import Terms from './Terms'
import Privacy from './Privacy'
export default {
	name: 'StartBox',
	data() {
		return {
			valid: false,
			agree: false,
			user_id: '',
			party_id: '',
			nameRules: [
				v => !!v || 'This field is required',
				v => v.length >= 3 || 'Must be at least be at least 3 characters.',
				v => v.length <= 32 || 'Must be less than 32 characters.'
			],
			passRules: [
				v => !!v || 'This field is required',
				v => v.length >= 6 || 'Must be at least be at least 6 characters.',
				v => v.length <= 32 || 'Must be less than 32 characters.'
			],
			tooltip: 'New accounts and parties are created on the fly.'
		}
	},
	methods: {
		startParty() {
			if (this.$refs.form.validate()) {
				console.log('party!')
				console.log(this.user_id)
			}
		}
	},
	components: {
		Terms,
		Privacy
	}
}
</script>

<style lang="less" src="../assets/less/global.less")</style>
