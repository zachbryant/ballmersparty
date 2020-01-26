<template lang="pug">
  b-card#gameContainer(class="pl-2 pr-3")
    b-row(class="")
      b-col(class="pr-4")
        b-row
          div(ref="markHtml" v-html="renderedMarkdown" class="shrinkH1")
        b-row(class="mb-4" align-v="between" align-h="center")
          b-col(cols="8" class="px-0")
            h5(class="mb-0") Tests: 
              span(class="text-success inline") {{passedCount}}
              |  / 
              span(class="text-primary") {{failedCount}}
          b-col(cols="4" class="px-0")
            b-btn(
              :disable="loading"
              block
              size="lg"
              variant="success"
              class=""
              @click="submit()"
            ) 
              h3(class="my-0") Run
        b-row#editorContainer
          div(ref="editor" style="width: 100% !important;")
        b-row(class="mt-4")
          b-col(cols="8" class="px-0")
            h5(class="mb-0") Tests: 
              span(class="text-success inline") {{passedCount}}
              |  / 
              span(class="text-primary") {{failedCount}}
          b-col(cols="4" class="px-0")
            b-btn(
              :disable="loading"
              block
              size="lg"
              variant="success"
              class=""
              @click="submit()"
            ) 
              h3(class="my-0") Run
</template>

<script>
import { Affix } from 'vue-affix'
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
  components: {
    Affix
  },
  data() {
    return {
      loading: false,
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
#editorContainer {
  //height: 100%;
}
.CodeMirror {
  height: 700px;
}
.shrinkH1 > h1 {
  font-size: 2.6rem !important;
}

#gameContainer {
  background: rgba(255, 255, 255, 0.1);
}
</style>
