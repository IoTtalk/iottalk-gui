<template>
  <div class="ui olive huge inverted attached menu">
    <div class="ui container">
      <div class="header item">
        IoTtalk
      </div>
      <a class="item"
        v-link="{path: '/', activeClass: 'active', exact: true}">
        <i class="home icon"></i>
        Home
      </a>
      <a class="item"
        v-link="{path: '/setting', activeClass: 'active'}">
        <i class="setting icon"></i>
        Setting
      </a>
    </div>
  </div><!-- .menu -->
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
