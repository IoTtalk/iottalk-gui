<template lang="jade">
    canvas#line-canvas
</template>

<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    onDraw() {
    },
  },
  
}
</script>

<style scoped>
canvas {
  background-color: transparent;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
</style>
