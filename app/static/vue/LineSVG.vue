<template lang="pug">
  svg
    progress-bar
</template>

<script>
import ProgressBar from './svg/ProgressBar.vue'

export default {
  components: {
    ProgressBar,
  },
}
</script>

<style scoped>
svg {
  width: 50%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
</style>

<style>
</style>
