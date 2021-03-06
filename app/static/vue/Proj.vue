<template lang="pug">
  div
    .ui.two.column.divided.grid.ghost
      .stretched.row
        .column
        .column#ghost-ctrl-panel

    .ui.two.column.grid
      .row
        .column
          h2.ui.header.center.aligned Project [[ pid ]]
          div(v-for="pk in graphs")
            graph(
              v-bind:conf="ref.graphs[pk]"
              v-bind:ref="ref"
              v-bind:cur-model="curModel"
              v-bind:feature-match="featureMatch"
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
          da-bind(
            v-if="ctrl_panel.type === 'da_bind'"
            v-bind:model="ctrl_panel.data"
            v-bind:da-list="apiService.dev.daList"
          )

    line-svg
</template>

<script>
import APIService from './APIService';

import DaBind from './DABind.vue';
import Graph from './Graph.vue';
import LineSVG from './LineSVG.vue';
import ModelAdd from './ModelAdd.vue';
import ModelConf from './ModelConf.vue';
import ProjNav from './ProjNav.vue';

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
      pid: undefined,
      featureMatch: {
        graph: null,  // graph id
        input: {
          da: null,  // device application id
          feature: null,  // feature name
        },
        output: {
          da: null,
          feature: null,
        },
      },
    }
  },
  mounted() {
    this.pid = this.$route.params.pid;

    this.$Progress.start();

    this.$http.get('/conf/mqtt/').then(
      res => {
        this.$Progress.increase(10);
        return res.json();
      },
      res => {  // error
        console.error(res);
      }
    ).then(
      data => {
        if (data === undefined)
          return;

        const {
          scheme,
          host,
          port
        } = data;

        const url = `${scheme}://${host}:${port}`;
        this.apiService = new APIService.APIService(url);

        return new Promise((resolve, reject) => {
          resolve(this.apiService);
        });
      }
    ).then(
      () => {
        this.$Progress.increase(10);
        return this.$http.get(`/proj/${this.pid}/`);
      }
    ).then(
      res => {
        this.$Progress.increase(10);
        return res.json();
      },
      res => {  // error
        this.$Progress.fail();
        console.error(res);
      }
    ).then(
      data => {
        if (data === undefined){
          this.$Progress.fail();
          return;
        }
        else if (data.state === 'error') {
          console.log(data);
          this.$Progress.fail();
          return;
        }

        this.graphs = data.graphs;
        this.ref = data.ref;
        this.proj = data.proj;

        // attach to graph api services
        this.graphs.map((g_id) => {
          this.apiService.attach_graph(g_id);
        });

        this.$Progress.finish();
      }
    );
  },
  computed: {
    curModel() {
      if (this.ctrl_panel.type !== 'model')
        return
      return this.ctrl_panel.data;
    }
  },
  methods: {
  },
  components: {
    DaBind,
    Graph,
    ModelAdd,
    ModelConf,
    ProjNav,
    'line-svg': LineSVG,
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
    'ctrl-panel-fin': function() {
      this.ctrl_panel.type = null;
      this.ctrl_panel.data = null;
    },
    'da-bind-conf': function(model) {
      this.ctrl_panel.type = 'da_bind';
      this.ctrl_panel.data = model;
    },
    'feature-match': function(model, fname /* feature name */) {
      if (!model.da)
        return;

      const slots = this.featureMatch;
      const slot = slots[model.type];

      slot.da = model.da.id;
      slot.feature = fname;

      if (model.type === 'input')
        this.featureMatch.graph = model.graph;

      // check both of `input` and `output` slots
      // if both ared filled, send the `add_link` request to graph api,
      // then empty this slots.
      if (!this.featureMatch.input.da || !this.featureMatch.output.da)
        return;

      const pub = this.apiService.graphs[this.featureMatch.graph];
      const payload_i = {
        'op': 'add_link',
        'da_id': slots.input.da,
        'idf': slots.input.feature,
      };
      const payload_o = {
        'op': 'add_link',
        'da_id': slots.output.da,
        'odf': slots.output.feature,
      };

      pub(payload_i);
      pub(payload_o);

      // clean up
      slots.graphs = null;
      slots.input.da = null;
      slots.input.feature = null;
      slots.output.da = null;
      slots.output.feature = null;
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
