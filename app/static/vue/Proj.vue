<template lang="jade">
  .ui.container
    .header Project No. [[ pid ]]
    .content
      p(v-for="g in graphs") test [[ g | json ]]
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
  data() {
    return {
      graphs: [],
    }
  },
  computed: {
    pid() {
      const id = this.$route.params.pid

      this.$http.get(`/proj/${id}`).then(
        res => {
          const data = res.json()
          console.log(data)
          this.graphs = data.graphs
        },
        res => {  // error
          console.log('error: ' + res.json())
        })
      return id
    },
  },
  components: {
    Device,
  },
}
</script>
