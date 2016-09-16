<template lang="jade">
  .ui.message.icon(
    v-if="enabled"
    v-bind:class="[level]"
  )
    i.icon(
      v-if="icon"
      v-bind:class="icon"
    )
    .content
      .header(v-if="header") [[ header ]]
      p(v-if="body") [[ body ]]
</template>

<script>
export default {
  data() {
    return {
      header: '',
      body: '',
      level: '',  // (success|error|info|warning)
      enabled: false,
    }
  },
  computed: {
    icon() {
      if (this.level === 'success')
        return ['check', 'circle'];
      else if (this.level === 'error')
        return ['remove', 'circle'];
      else if (this.level === 'info')
        return ['info', 'circle'];
      else if (this.level === 'warning')
        return ['warning', 'circle'];
      else
        return;
    },
  },
  events: {
    'show-msg': function(msg) {
      const duration = msg.duration || 5000;

      if (this.enabled !== false)
        clearTimeout(this.enabled)

      this.enabled = true;
      this.header = msg.header;
      this.body = msg.body;
      this.level = msg.level;

      this.enabled = setTimeout(() => {this.enabled = false}, duration);
    },
  },
}
</script>

<style scoped>
.ui.message {
  position: fixed;
  bottom: 0;
  width: 100%;
  border-radius: 0px;
  margin: 0;
  border: 0;
  min-height: 40px;
  text-align: center;
  box-shadow: 0 0 0 #fff;
}
.ui.icon.message > .icon {
  font-size: 2em;
}
</style>
