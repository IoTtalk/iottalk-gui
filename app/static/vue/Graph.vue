<template lang="jade">
  .content [[ conf | json ]]
  .ui.padded.grid
    .four.column.row
      .left.floated.column
        device(
          v-for="dev in conf.input"
          v-bind:model="ref.models[dev]")
      .three.wide.column
        .ui.tiny.middle.aligned.progress
          .bar
      .two.wide.middle.aligned.column
        joint
      .three.wide.column
      .right.floated.column
        device(
          v-for="dev in conf.output"
          v-bind:model="ref.models[dev]")
</template>

<script>
import Device from './Device.vue'
import Joint from './Joint.vue'

export default {
  props: {
    conf: Object,
    ref: Object,
  },
  components: {
    Device,
    Joint,
  },
  methods: {
  },
}
</script>
