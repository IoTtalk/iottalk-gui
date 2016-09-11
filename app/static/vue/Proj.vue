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
        div(v-for="g in graphs")
          graph(v-bind:conf="g")
      .column#ctrl-panel
        model-conf(
          v-if="ctrl_panel.type === 'model'"
          v-bind:model="ctrl_panel.data"
        )
        model-add(
          v-if="ctrl_panel.type === 'model_add'"
          v-bind:model="ctrl_panel.data"
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
    }
  },
  computed: {
    pid() {
      const id = this.$route.params.pid;

      this.$http.get(`/proj/${id}/`).then(
        res => {
          const data = res.json();

          const bindModel = (graph) => {
            /*
              graph: {
                'idf': [{
                  'name': '...',
                  'features': ['...'],
                  'models': {...},
                }],
                'odf': ...
              }
             */
            const _graph = Object.assign({}, graph);  // copy
            const {idf, odf} = _graph;
            const models = data.models;
            
            const link = (obj) => {
              if (models[obj.name] === undefined)
                return;
              obj.model = models[obj.name];
            };

            idf.map(link);
            odf.map(link);

            return _graph;
          };

          this.graphs = data.graphs.map(bindModel);
        },
        res => {  // error
          console.log('error: ' + res.json());
        })
      return id;
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
    'model-add': function(model){
      this.ctrl_panel.type = 'model_add';

      // add `enable` feild in each feature
      ['idf', 'odf'].map((df, idx, arr) => {
          model[df].map((feature, idx, arr) => {
              feature.enable = false;
          }, this);
      }, this);

      this.ctrl_panel.data = model;
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
