<template lang="jade">
  // proj-nav

  .ui.two.column.divided.grid.ghost
    .stretched.row
      .column
      .column#ghost-ctrl-panel

  .ui.two.column.grid
    .stretched.row
      .column
        p Project [[ pid ]]
        div(v-for="g in graphs")
          graph(v-bind:conf="g")
      .column#ctrl-panel

</template>

<script>
import Graph from './Graph.vue'
import LineCanvas from './LineCanvas.vue'
import ProjNav from './ProjNav.vue'

export default {
  data() {
    return {
      graphs: [],
    }
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
    LineCanvas,
    ProjNav,
  },
}
</script>

<style>
#ghost-ctrl-panel {
  background-color: #f5f5f5;
}

html {
  height: 100%;
  position: relative;
}

body {
  height: 100%;
}
</style>

<style scoped>
.ui.grid.ghost {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  bottom: 0;
  margin: 0;
  padding: 0;
  padding-top: 40px;  /* preserve for menu */
  z-index: -1;
}

.ui.grid.ghost > div.row {
  margin: 0;
  padding: 0;
}

.ui.grid.ghost > div.row > div.column {
  padding-top: 20px;
}

.ui.grid {
  padding-left: 10px;
  padding-right: 10px;
}
</style>
