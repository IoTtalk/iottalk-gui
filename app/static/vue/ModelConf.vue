<template lang="jade">
  h2.ui.center.aligned.header [[ model.name ]]

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
  },
  methods: {
  },
};
</script>

<style scoped>
h2.ui.header {
  height: 20px;
}
</style>
