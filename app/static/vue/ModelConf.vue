<template lang="pug">
  div
    h2.ui.center.aligned.header Config: [[ model.name ]]

    table.ui.basic.celled.definition.table
      thead
        tr
          th Enable
          th [[ type_map[model.type] ]]
      tbody
        tr(v-for="feature in model.features")
          td.collapsing
            .ui.fitted.slider.checkbox
              input(
                type="checkbox"
                v-model="feature.enable"
              )
              label
          td [[ feature.name | capitalize ]]

    button.ui.button(v-on:click="saveModel")
      i.ui.icon.save
      | Save
    button.ui.button(v-on:click="deleteModel")
      i.ui.icon.trash
      | Delete
</template>

<script>
import arrayRemove from 'jqb-array-remove';

export default {
  data() {
    return {
      type_map:{
        'input': 'Input Device Feature',
        'output': 'Output Device Feature',
      }
    }
  },
  props: {
    model: Object,
    ref: Object,
  },
  methods: {
    deleteModel() {
      const dev_id = this.model.pk;

      this.$http.delete(`/mod/obj/${dev_id}/`).then(
        res => {
          return res.json()
        },
        res => {  // error
          console.log(res)
        }
      ).then(
        data => {
          if (data === undefined)
            return;
          if (data.state !== 'ok') {
            console.error(data);
            return;
          }

          const graph = this.ref.graphs[this.model.graph];
          graph[this.model.type] = arrayRemove(graph[this.model.type], dev_id);

          this.ref.models[dev_id] = undefined;
          this.$dispatch('msg-show', {
            header: `Device ${this.model.name} deleted.`,
            level: 'success',
          });
          this.$dispatch('ctrl-panel-fin');
        }
      );
    },
    _getEnabledFeatures(features) {
      const ret = {}

      features.map(f => {
        ret[f.pk] = f.enable;
      })

      return ret;
    },
    saveModel() {
      const dev_id = this.model.pk;
      const payload = {
        'features': this._getEnabledFeatures(this.model.features),
      }

      this.$http.post(`/mod/obj/${dev_id}/`, payload).then(
        res => {
          return res.json();
        },
        res => {  // error
          console.error(res);
        }
      ).then(
        data => {
          if (data === undefined)
            return;
          if (data.state !== 'ok') {
            console.error(data);
            return;
          }

          this.$dispatch('msg-show', {
            header: `Device ${this.model.name} saved.`,
            level: 'success',
          });
          this.$dispatch('ctrl-panel-fin');  // finish
        }
      );
    },
  },
};
</script>

<style scoped>
h2.ui.header {
  height: 20px;
}
</style>
