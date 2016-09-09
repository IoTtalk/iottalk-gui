<template lang="jade">
  .content [[ conf | json ]]
  .ui.padded.grid
    .four.column.row
      .left.floated.column
        device(:model="conf.idf[0]")
      .three.wide.column
        .ui.tiny.middle.aligned.progress
          .bar
      .two.wide.middle.aligned.column
        joint
      .three.wide.column
      .right.floated.column
        device(:model="conf.odf[0]")
</template>

<script>
import Device from './Device.vue'
import Joint from './Joint.vue'

export default {
  props: {
    conf: Object,
  },
  components: {
    Device,
    Joint,
  },
  methods: {
  },
}
</script>
