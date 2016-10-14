<template lang="pug">
  div
    h2.ui.center.aligned.header Add Device: [[ model.name ]]

    table.ui.basic.celled.definition.table(
      v-for="df in dfs"
      v-if="model[df.key].length != 0"
    )
      thead
        tr
          th Enable
          th [[ df.name ]]
      tbody
        tr(v-for="feature in model[df.key]")
          td.collapsing
            .ui.fitted.slider.checkbox
              input(
                type="checkbox"
                v-model="feature.enable"
              )
              label
          td [[ feature.name | capitalize ]]

    button.ui.button(v-on:click="createModel") Commit
</template>

<script>
export default {
  data() {
    return {
      dfs: [
        {key: 'idf', name: 'Input Device Feature'},
        {key: 'odf', name: 'Output Device Feature'},
      ],
    }
  },
  props: {
    model: Object,
    graphs: Array,
    ref: Object,
  },
  computed: {
    last_graph() {
      const idx = this.graphs[this.graphs.length - 1];
      return this.ref.graphs[idx];
    }
  },
  methods: {
    createModel() {
      const payload = {
        model: this.model.pk,
        idf: this._getEnabledFeatures(this.model.idf),
        odf: this._getEnabledFeatures(this.model.odf),

        // append devices to the last graph
        graph: this.last_graph.pk,
      };
      this.$http.put('/mod/obj/', payload).then(
        (response) => {
          return response.json();
        },
        (response) => {  // error
          console.log(response);
        }
      ).then(
        (data) => {
          if (data === undefined)
            return;
          else if (data.state === 'error') {
            console.log(data);
          }

          const input = data.input;
          const output = data.output;
          const graph = this.last_graph;

          // append devices to the last graph
          if (input !== null) {
            /*
             * Magic mentioned at:
             * https://vuejs.org/guide/reactivity.html#Change-Detection-Caveats
             */
            const obj = {};
            obj[input.pk] = input;
            this.ref.models = Object.assign({}, this.ref.models, obj);

            graph.input.push(input.pk);
          }
          if (output !== null) {
            /*
             * Magic mentioned at:
             * https://vuejs.org/guide/reactivity.html#Change-Detection-Caveats
             */
            const obj = {};
            obj[output.pk] = output;
            this.ref.models = Object.assign({}, this.ref.models, obj);

            graph.output.push(output.pk);
          }

          this.$dispatch('msg-show', {
            header: `Model ${this.model.name} created.`,
            level: 'success',
          });
          this.$dispatch('ctrl-panel-fin');  // finish
        }
      );
    },
    _getEnabledFeatures(df_list) {
      return df_list.filter((el) => {
        return el.enable;
      }).map((el) => {
        return el.pk;
      });
    },
  },
};
</script>

<style scoped>
h2.ui.header {
  height: 20px;
}
</style>
