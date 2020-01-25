<template>
  <div class="contact">
    <v-container fill-height>
      <v-layout row align-center>
        <v-flex>
          <v-card
            style="display: inline-block;"
            class="pl-4 pr-4 pb-3 pt-3"
            width="75%"
          >
            <v-card-title overflow>
              <h2 v-html="greet"></h2>
            </v-card-title>
            <v-form>
              <v-text-field
                v-model="user_name"
                name="user_name"
                label="@user-name"
                persistent-hint
              >
              </v-text-field>
              <v-text-field
                v-model="user_email"
                name="user_email"
                label="@user_email"
                persistent-hint
                :rules="[rules.required, rules.email]"
                required
              >
              </v-text-field>
              <v-text-field
                v-model="message"
                name="message"
                label="@message"
                persistent-hint
                :rules="messageRules"
                required
                multi-line
                :counter="500"
              >
              </v-text-field>
            </v-form>
            <v-card-actions>
              <div
                class="g-recaptcha"
                data-sitekey="6LeFEVYUAAAAANb9Me4PnVJBWEsl1EDXPzp_YrDE"
              ></div>
              <v-btn
                large
                block
                raised
                color="primary white--text"
                @click="sendMessage()"
                >Submit</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
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
