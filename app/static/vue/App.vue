<template lang="pug">
  div
    main-nav
    // vue-progress-bar
    // router-view
    // msg-banner(ref="msg")
</template>

<script>
import MainNav from './MainNav.vue'
import MsgBanner from './MsgBanner.vue'

export default {
  name: 'App',
  components: {
    MainNav,
    MsgBanner,
  },
  methods: {
  },
  events: {
    'model-add': function(model) {
      this.$broadcast('model-add', model);
    },
    'msg-show': function(msg) {
      this.$refs.msg.$emit('show-msg', msg);
    }
  },
}
</script>
