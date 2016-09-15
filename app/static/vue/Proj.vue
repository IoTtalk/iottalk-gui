<template lang="jade">
  // proj-nav

  .ui.two.column.divided.grid.ghost
    .stretched.row
      .column
      .column#ghost-ctrl-panel

  .ui.two.column.grid
    .row
      .column
        p Project [[ pid ]]
        div(v-for="pk in graphs")
          graph(
            v-bind:conf="ref.graphs[pk]"
            v-bind:ref="ref"
          )
      .column#ctrl-panel
        model-conf(
          v-if="ctrl_panel.type === 'model'"
          v-bind:model="ctrl_panel.data"
          v-bind:ref="ref"
        )
        model-add(
          v-if="ctrl_panel.type === 'model_add'"
          v-bind:model="ctrl_panel.data"
          v-bind:graphs="graphs"
          v-bind:ref="ref"
        )

</template>

<script>
import Graph from './Graph.vue'
import LineCanvas from './LineCanvas.vue'
import ModelAdd from './ModelAdd.vue'
import ModelConf from './ModelConf.vue'
import ProjNav from './ProjNav.vue'

export default {
  data() {
    return {
      graphs: [],
      ctrl_panel: {
        type: null,
        data: null,
      },
      ref: {},
      proj: {},
    }
  },
  computed: {
    pid() {
      const id = this.$route.params.pid;

      this.$http.get(`/proj/${id}/`).then(
        res => {
          return res.json();
        },
        res => {  // error
          console.log('error: ' + res.json());
        }
      ).then(
        data => {
          if (data === undefined)
            return;
          else if (data.state === 'error') {
            console.log(data);
          }

          this.graphs = data.graphs;
          this.ref = data.ref;
          this.proj = data.proj;
        }
      );
      return id;
    },
  },
  methods: {
    cleanCtrlPanel() {
      this.ctrl_panel.type = null;
      this.ctrl_panel.data = null;
    },
  },
  components: {
    Graph,
    LineCanvas,
    ModelAdd,
    ModelConf,
    ProjNav,
  },
  events: {
    modelSelect(model) {
      this.ctrl_panel.type = 'model';
      this.ctrl_panel.data = model;
    },
    'model-add': function(model) {
      this.ctrl_panel.type = 'model_add';
      this.ctrl_panel.data = model;
    },
    'model-add-fin': function() {
      return this.cleanCtrlPanel();
    },
    'model-conf-fin': function() {
      return this.cleanCtrlPanel();
    },
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
