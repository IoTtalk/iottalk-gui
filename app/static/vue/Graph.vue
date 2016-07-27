<template lang="jade">
  .ui.padded.grid
    .four.column.row
      .left.floated.column
        device
      .right.floated.column
        device
</template>

<script>
import Device from './Device.vue'

export default {
  props: [
   'conf',
  ],
  components: {
    Device,
  },
}
</script>
