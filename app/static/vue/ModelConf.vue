<template lang="jade">
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
      this.$http.delete(
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
            console.log(data);
            return;
          }
        }
      );
    },
    saveModel() {
    },
  },
};
</script>

<style scoped>
h2.ui.header {
  height: 20px;
}
</style>
