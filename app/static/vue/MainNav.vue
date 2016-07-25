<template lang="jade">
  div.ui.olive.huge.inverted.attached.menu
    div.ui.container
      div.header.item IoTtalk
      a.item(
        v-link="{path: '/', activeClass: 'active', exact: true}"
      )
        i.home.icon
        | Home
      a.item(
        v-link="{path: '/setting', activeClass: 'active'}"
      )
        i.setting.icon
        | Setting
</template>

<script>
export default {
}
</script>

<style scoped>
.menu {
  margin-bottom: 20px;
}
</style>
