<template lang="jade">
  main-nav
  router-view
</template>

<script>
import MainNav from './MainNav.vue'

export default {
  replace: false,
  components: {
    MainNav,
  },
}
</script>
