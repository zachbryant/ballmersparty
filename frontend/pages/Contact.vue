<template lang="pug">
	div(class="contact")
		b-row(align-center)
			b-card(
				border-variant="dark"
				bg-variant="dark"
				class="pl-4 pr-4 pb-3 pt-3 w-75"
			)
				h2(v-html="greet")
				form(class="needs-validation mb-3" novalidate v-on:submit.prevent="startParty")
					div(class="form-group")
						label(for="emailInput") Email
						input#emailInput(
							autofocus
							v-model="email" 
							type="email" 
							class="form-control errorInput" 
							aria-describedby="emailHelp" 
							placeholder="email@example.com"
						)
						small#emailHelp(class="form-text") What's your email?
						div(class="invalid-feedback") Please enter a valid email.
					div(class="form-group")
						label(for="messageInput") Message
						input#messageInput(
							v-model="message" 
							type="text" 
							class="form-control errorInput" 
							aria-describedby="messageHelp" 
							placeholder="I'd like to tell you...."
						)
						small#messageHelp( class="form-text") What would you like to say?
						div(class="invalid-feedback") Please enter a message.
				
					b-btn(
						block
						variant="primary"
						@click=""
					) Submit
</template>

<script>
const greetings = [
  'I hope you have a compliment for me.. &#3900;&#8226;&#771;&#865; &#631;&#8226;&#771;&#865;&#3901;',
  'Is everything okay?',
  "It's so good to see you! ( &#865;&#7508; &#860;&#662; &#865;&#7508; )",
  'Leave a message after the beep...',
  "How's my driving?",
  'The Doctor is <i>in!</i>',
  'Tell me where it hurts.',
  "I've been expecting you. ( &#865;&#664;&#9581;&#860;&#662;&#9582;&#865;&#664;)",
  "What's up, doc?",
  "Tag, you're it!",
  'Lets get ready to <b>RUMBLLLEEEEE!</b> &#12541;&#3900; &#3232;&#30410;&#3232; &#3901;&#65417;',
  'Please, have a seat.',
  '*crickets*',
  'Beep boop I AM SELF AWARE ด้้้้้็็็็็้้้้้็็็็็้้้้้็็็็็้้้้้็็็็็้้้้้็็็็็้้้้้็็็็็้้้้้็็็็็้้้้้дด็็็็็้้้้้็็็็้้้้้็็็็็้้้้้็็็็็้้้้้็็็็็้้้้้',
  'Show me the money!',
  "Let's chat &#8226;&#8255;&#8226;"
]

export default {
  name: 'contact',
  data() {
    return {
      greet: greetings[Math.floor(Math.random() * greetings.length)],
      user_name: '',
      user_email: '',
      message: '',
      messageRules: [
        v => !!v || 'This field is required',
        v => v.length > 15 || 'Must be at least be at least 15 characters.',
        v => v.length <= 500 || 'Must be less than 500 characters.'
      ],
      rules: {
        required: value => !!value || 'This field is required.',
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Invalid e-mail.'
        }
      }
    }
  }
}
</script>

<style lang="less" src="../assets/less/global.less"></style>

<style lang="less" scoped>
@primary: rgba(239, 83, 80, 1);

h2,
i {
  color: @primary !important;
}
</style>
