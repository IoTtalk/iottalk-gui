<template lang="jade">
  div#main-nav.ui.red.huge.inverted.attached.menu
    div.ui.container
      div.header.item IoTtalk
      a.item(
        v-link="{name: 'home', activeClass: 'active', exact: true}"
      )
        i.home.icon
        | Home
      .ui.pointing.dropdown.link.item
        i.cube.icon
        | Model
        i.dropdown.icon
        .menu
          .item(
            v-for="model in models"
            v-on:click="onModelAdd(model)"
          ) [[ model.name ]]
      a.item(
        v-link="{path: '/setting', activeClass: 'active'}"
      )
        i.setting.icon
        | Setting
</template>

<script>
import semantic from "../../static/semantic/semantic.min.js";

export default {
  data() {
    return {
      models: [],
    };
  },
  methods: {
    getModels() {
      this.$http.get('/mod/').then(
        res => {  // on success
          this.models = res.json();
        },
        res => {  // on error
          console.log('error: ' + res.json());
        }
      );
    },
    onModelAdd(model) {
      this.$dispatch('model-add', model);
    },
  },
  ready() {
    this.getModels();
    $('.ui.dropdown').dropdown({
      on: 'hover',
      transition: 'drop',
      action: 'hide',
    });
  },
}
</script>

<style>
#main-nav {
  margin-bottom: 0px;
}
</style>
