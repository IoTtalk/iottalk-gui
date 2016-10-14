<template lang="jade">
  g
    path(
      d="M [[ startx ]] [[ starty ]] a 2 2 0 0 0 0 5 h 300 a 2 2 0 0 0 0 -5 Z"
      stroke="#e5e5e5"
      fill="#e5e5e5"
      stroke-width="1"
    )
    path(
      d="M [[ startx ]] [[ starty ]] a 2 2 0 0 0 0 5 h 100 a 2 2 0 0 0 0 -5 Z"
      stroke="#888"
      fill="#888"
      stroke-width="1"
    )
</template>

<script>
export default {
  data() {
    return {
      startx: '250',
      starty: '150',
    }
  },
}
</script>

<style>
</style>

<style scoped>
</style>
