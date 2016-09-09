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
  methods: {
  },
  events: {
    'model-add': function(model) {
      this.$broadcast('model-add', model);
    },
  },
}
</script>
