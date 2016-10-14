<template lang="pug">
  .ui.padded.grid
    .four.column.row
      .left.floated.column
        device(
          v-for="dev in conf.input"
          v-bind:model="ref.models[dev]"
          v-bind:class!="{'selected': curModel && curModel.pk === dev}"
          v-bind:feature-match="featureMatch.input"
        )
      .three.wide.column
        // space for progress bar
      .two.wide.middle.aligned.column
        joint
      .three.wide.column
      .right.floated.column
        device(
          v-for="dev in conf.output"
          v-bind:model="ref.models[dev]"
          v-bind:class!="{'selected': curModel && curModel.pk === dev}"
          v-bind:feature-match="featureMatch.output"
        )
</template>

<script>
import Device from './Device.vue'
import Joint from './Joint.vue'

export default {
  props: {
    conf: Object,
    ref: Object,
    curModel: Object,
    featureMatch: Object,
  },
  components: {
    Device,
    Joint,
  },
  methods: {
  },
}
</script>
