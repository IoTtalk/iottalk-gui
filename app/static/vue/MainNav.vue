<template lang="jade">
  div#main-nav.ui.red.huge.inverted.attached.menu
    div.ui.container
      div.header.item IoTtalk
      a.item(
        v-link="{name: 'home', activeClass: 'active', exact: true}"
      )
        i.home.icon
        | Home
      a.item
        i.cube.icon
        | Model
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

<style>
#main-nav {
  margin-bottom: 0px;
}
</style>
