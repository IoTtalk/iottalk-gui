<template lang="pug">
  div#main-nav.ui.red.huge.inverted.attached.menu
    div.ui.container
      div.header.item IoTtalk
      router-link.item(
        v-bind:to="{ name: 'home' }"
      )
        i.home.icon
        | Home
      .ui.simple.dropdown.item
        i.cube.icon
        | Model
        i.dropdown.icon
        .menu
          .item(
            v-for="model in models"
            v-on:click="onModelAdd(model)"
          ) {{ model.name }}
      router-link.item(
        v-bind:to="{ path: '/setting' }"
      )
        i.setting.icon
        | Setting
</template>

<script>
export default {
  name: 'MainNav',
  data() {
    return {
      models: [],
    };
  },
  methods: {
    getModels() {
      this.$http.get('/mod/').then(
        res => {  // on success
          return res.json();
        },
        res => {  // on error
          console.error(res);
        }
      ).then(
        data => {
          this.models = data;
        }
      );
    },
    onModelAdd(model) {
      this.$dispatch('model-add', JSON.parse(JSON.stringify(model)));  // the cloned one
    },
  },
  mounted() {
    this.getModels();
  },
}
</script>

<style>
#main-nav {
  margin-bottom: 0px;
}
</style>
