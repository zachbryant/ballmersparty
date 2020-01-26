<template lang="pug">
	footer(class="footer")
		b-container(fluid class="container")
			b-row
				b-col
					p(class="note mb-0") Made with 
						i(class="fa fa-heart" style="font-size:16pxl;")
						span(class="note")  at Purdue.
				b-col
					p
						a(class="underline" v-b-modal.termsModalFooter) terms
						|  and 
						a(class="underline" v-b-modal.privacyModalFooter) privacy policy
						b-modal#termsModalFooter(size="xl" title="Terms and Conditions")
							Terms
						b-modal#privacyModalFooter(size="xl" title="Privacy Policy")
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
  }
}
</script>

<style>
.footer {
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  bottom: 0;
  width: 100%;
  height: 60px;
  line-height: 60px;
}
</style>
