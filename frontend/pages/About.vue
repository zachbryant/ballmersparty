<template lang="pug">
	div
		b-container(fluid)
			b-row(class="text-center")
				b-col(cols="4 text-center")
					h3#explain_title /**** Eh what's all this now? ****/
					p Programmers have a bit of a reputation for drinking. If (or when) you've had to read someone else's 
						a(class="underline" href="https://imgs.xkcd.com/comics/code_quality.png" target="_blank") soul sucking documentation for work, you'll understand.
						|  The peak is named after Steve Ballmer (the former CEO of Microsoft) for his sudden outbursts and outlandish public behavior, which make him seem constantly intoxicated. It is rumored that the peak lies at approximately 0.1337% BAC, but it varies for individuals. 
					p In 2012 
						a(class="underline" href="https://www.sciencedirect.com/science/article/pii/S1053810012000037" target="_blank") researchers found
						|  that intoxicated participants were better creative problem solvers than the sober participants. There's a little truth to everything, huh?
					p If you spend enough time here, we might end up with conclusive data on the exact location of Ballmer's Peak. 
						strong Climb on!
				b-col(cols="8")
					pre#ascii_art {{ asciiart }}
</template>

<script>
import asciiart from '../assets/asciiart'

export default {
  name: 'explain',
  data() {
    return {
      asciiart
    }
  }
}
</script>

<style scoped>
p {
  text-align: justify;
  text-shadow: none;
}
</style>
