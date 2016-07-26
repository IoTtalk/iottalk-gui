<template lang="jade">
  div.ui.container
    div.ui.raise.segment
      a(href="#"
        v-on:click="create_proj")
        div.ui.header
          i.icon.plus
          div.content Create a new project
</template>

<script>
export default {
  methods: {
    create_proj() {
      this.$http.put('/proj/', {}).then(res => {
        const data = res.json()
        console.log(data.pid)

        this.$router.go({
          name: 'proj',
          params: {
            pid: data.pid
          }
        })
      }, res => {
        console.log(res) // error
      })
    }
  }
}
</script>
