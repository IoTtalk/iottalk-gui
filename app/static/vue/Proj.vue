<template lang="jade">
  .ui.container(
    v-on:dragover="allowDragOver"
    v-on:drop.prevent.stop=""
  )
    .header Project No. [[ pid ]]

    div(v-for="g in graphs")
      graph(v-bind:conf="g")
  
    line-canvas(
      v-bind:x="pageX"
      v-bind:y="pageY"
      v-bind:startx="startX"
      v-bind:starty="startY"
    )
</template>

<script>
import Graph from './Graph.vue'
import LineCanvas from './LineCanvas.vue'

export default {
  data() {
    return {
      graphs: [],

      startX: -1,  // the start anchor
      startY: -1,

      pageX: -1,  // the mouse position
      pageY: -1,
    }
  },
  methods:{
    allowDragOver(ev) {
      // console.log(`drag over! (${ev.pageX}, ${ev.pageY})`)

      // binding for trigger canvas re-draw
      this.pageX = ev.pageX
      this.pageY = ev.pageY

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
  events: {
    'feature-drag': function(pos){
      ({
        x: this.startX,
        y: this.startY
       } = pos);
    },
    'feature-dragend': function(){
      this.$broadcast('feature-dragend')
    },
  },
}
</script>
