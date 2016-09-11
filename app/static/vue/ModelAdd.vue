<template lang="jade">
  h2.ui.center.aligned.header Add Device: [[ model.name ]]

  table.ui.basic.celled.definition.table(
    v-for="df in dfs"
    v-if="!!model[df.key]"
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
      ]
    }
  },
  props: {
    model: Object,
    graphs: Array,
  },
  methods: {
    createModel() {
      const payload = {
        model: this.model.pk,
        idf: this._getEnabledFeatures(this.model.idf),
        odf: this._getEnabledFeatures(this.model.odf),

        // append devices to the last graph
        graph: this.graphs[this.graphs.length - 1].pk,
      };
      console.log(payload);
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

          const input = data.input;
          const output = data.output;
          const graph = this.graphs[this.graphs.length - 1];

          // append devices to the last graph
          if (input !== null) {
            graph.idf.push(input);
          }
          if (output !== null) {
            graph.odf.push(output);
          }
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
