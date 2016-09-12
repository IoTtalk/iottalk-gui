<template lang="jade">
  .ui.raised.segments.device
    .ui.horizontal.segments
      .ui.center.aligned.segment.setting-cell
        a(v-on:click="modelSelect")
          i.setting.icon
      .ui.segment
        .ui.header.center.aligned.model-name [[ model.name ]]
    .ui.feature.center.aligned.segment.feature-cell
      .ui.segment(
        v-for="feature in model.features"
      ) [[ feature.name | capitalize ]]
</template>

<script>
export default {
  data() {
    return {
    }      
  },
  props: {
    model: Object,
  },
  methods: {
      modelSelect() {
        this.$dispatch('modelSelect', this.model.model);
      },
  },
}
</script>

<style scoped>
div.device div.selected{
  box-shadow: 0px 2px 5px #acacac inset;
}

.feature-cell {
  padding: 6px;
  padding-top: 0px;
}

.feature-cell > .segment {
  margin: 0px;
  margin-top: 6px;
}

.feature-cell > .segment:hover {
  cursor: pointer;
  box-shadow: 0px 1px 3px #96B5FE;
}

.ui.segment.setting-cell {
  padding-left: 3px;
  padding-right: 0px;
  padding-bottom: 0px;
}

.ui.segment.setting-cell i {
  font-size: 2.5em;
}

.model-name {
  color: #999;
}
</style>
