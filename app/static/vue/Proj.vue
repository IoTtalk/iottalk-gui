<template lang="jade">
  .ui.container(
    v-on:dragover="allowDragOver"
    v-on:drop.prevent.stop=""
  )
    .header Project No. [[ pid ]]

    div(v-for="g in graphs")
      graph(v-bind:conf="g")
  
    line-canvas
</template>

<script>
import Graph from './Graph.vue'
import LineCanvas from './LineCanvas.vue'

export default {
  data() {
    return {
      graphs: [],
    }
  },
  methods:{
    allowDragOver(ev) {
      console.log(`drag over! (${ev.pageX}, ${ev.pageY})`)
      ev.dataTransfer.dropEffect = 'link'
    },
  },
  computed: {
    pid() {
      const id = this.$route.params.pid

      this.$http.get(`/proj/${id}`).then(
        res => {
          const data = res.json()
          this.graphs = data.graphs
        },
        res => {  // error
          console.log('error: ' + res.json())
        })
      return id
    },
  },
  components: {
    Graph,
    LineCanvas
  },
}
</script>
