<template lang="jade">
  div.joint
    div.ui.circular.massive.icon.button
      i.code.icon
</template>

<script>

export default {
  methods: {
  },
}
</script>

<style scope>
div.joint > div.button {
  transition: transform 1s ease;
  transform: scale(0.5) rotate(0deg);
}
div.joint > div.button:hover {
  transform: scale(1) rotate(360deg);
}
</style>
