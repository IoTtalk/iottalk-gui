<template lang="jade">
  h2.ui.center.aligned.header [[ model.name ]]

  table.ui.celled.definition.table
    thead
      tr
        th
        th Input Device Features
    tbody
      tr
        td.collapsing
          .ui.fitted.slider.checkbox
            input(type='checkbox')
            label
        td Feature 1
</template>

<script>
export default {
  props: {
    model: Object,
  },
};
</script>
