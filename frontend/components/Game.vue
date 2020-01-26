<template lang="pug">
  b-card#gameContainer(class="pl-2 pr-3")
    b-row(class="h-100")
      b-col(class="pr-4")
        div(ref="markHtml" v-html="renderedMarkdown" class="shrinkH1")
      b-col
        // TODO fix height1
        b-row
          div(ref="editor" style="width: 100% !important;min-height: 100% !important;")
        b-row(class="mt-3")
          b-col(cols="8" class="px-0")
            p Tests: 
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

let temp =
  "# Integers come in all sizes\n\
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: **$2^31 - 1$** (c++ int) or  **$2^63 - 1$** (C++ long long int).\n\
As we know, the result of **$a^b$** grows really fast with increasing **b**.\n\
Let's do some calculations on very large integers.\n\
**Task**\n\
Read four numbers, **a**, **b**, **c**, and **d**, and print the results of **$a^b + c^d$**.\n\
**Input Format**\n\
Integers **a**, **b**, **c**, and **d** are given on four separate lines, respectively.\n\
**Constraints**\n\
$1 \\leq a \\leq 1000$\n\n\
$1 \\leq b \\leq 1000$\n\n\
$1 \\leq c \\leq 1000$\n\n\
$1 \\leq d \\leq 1000$"

export default {
  name: 'game',
  components: {},
  data() {
    return {
      editor: undefined,
      passedCount: 0,
      failedCount: 0,
      name: 'Problem name',
      markdown: temp
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
      let renderedMarkdown = marked(this.markdown)
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
