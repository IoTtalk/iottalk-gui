<template lang="jade">
  .content [[ conf | json ]]
  .ui.padded.grid
    .four.column.row
      .left.floated.column
        device(
          v-for="dev in conf.idf"
          v-bind:model="dev")
      .three.wide.column
        .ui.tiny.middle.aligned.progress
          .bar
      .two.wide.middle.aligned.column
        joint
      .three.wide.column
      .right.floated.column
        device(
          v-for="dev in conf.odf"
          v-bind:model="dev")
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
