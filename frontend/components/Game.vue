<template lang="pug">
  b-card#gameContainer(class="pl-2 pr-3")
    b-row(class="h-100")
      b-col(class="pr-4")
        div(ref="markHtml" v-html="renderedMarkdown" class="shrinkH1")
      b-col
        // TODO fix height1
        b-row(class="mb-3" align-v="between" align-h="center")
          b-col(cols="8" class="px-0")
            p(class="mb-0") Tests: 
              span(class="text-success") {{passedCount}}
              |  / 
              span(class="text-primary") {{failedCount}}
          b-col(cols="4" class="px-0")
            b-btn(
              block
              size="lg"
              variant="success"
              class=""
              @click="submit()"
            ) 
              h3(class="my-0") Run
        b-row
          div(ref="editor" style="width: 100% !important;min-height: 100% !important;")
</template>

<script>
import marked from 'marked'
import katex from 'katex'
import renderMathInElement from 'katex/contrib/auto-render/auto-render'
import 'katex/dist/katex.min.css'
import 'codemirror/lib/codemirror.css'
import 'codemirror/theme/material-darker.css'
import CodeMirror from 'codemirror'
import 'codemirror/mode/python/python'

export default {
  name: 'game',
  components: {},
  data() {
    return {
      editor: undefined,
      passedCount: 0,
      failedCount: 0,
      name: 'Problem name'
    }
  },
  mounted() {
    this.editor = CodeMirror(this.$refs.editor, {
      value: 'def main():\n\tpass\n\nif __name__ == "__main__":\n\tmain()',
      lineNumbers: true,
      theme: 'material-darker',
      smartIndent: true,
      lineWrapping: true,
      spellcheck: true,
      mode: 'python'
    })
    this.editor.setSize('100%', '100%')
  },
  methods: {
    submit() {
      let plaintext = this.editor.getValue()
      this.$api.submitAnswer(plaintext)
      // TODO loading animation
    }
  },
  computed: {
    renderedMarkdown: function() {
      let renderedMarkdown = marked(
        this.$store.state.party.global.problem.description
      )
      this.$nextTick(() => {
        renderMathInElement(this.$refs.markHtml, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
          ]
        })
      })
      return renderedMarkdown
    }
  }
}
</script>

<style lang="scss">
.CodeMirror {
  height: 100%;
  min-height: 100%;
}
.shrinkH1 > h1 {
  font-size: 2.6rem !important;
}

#gameContainer {
  background: rgba(255, 255, 255, 0.1);
}
</style>
