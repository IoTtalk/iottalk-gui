<template lang="pug">
  div
    h2.ui.center.aligned.header Bind to [[ model.name ]]

    .ui.vertical.buttons(
      v-if!="candidateDA.length > 0"
    )
      .ui.fluid.button(
        v-for="da in candidateDA"
        v-on:click.native="bindDA(da)"
      )
        h3.ui.header [[ da.name ]]
        div [[ da.id ]]
</template>

<script>
import Utils from './Utils.js';


export default {
  data() {
    return {
    };
  },
  computed: {
    candidateDA() {
      const type = this.model.type;
      const typeMap = {
        input: 'idf_list',
        output: 'odf_list',
      };
      const dFeatSet = new Utils.Set(this.model.features.map((el) => {
        return el.name
      }));  // device object feature set

      const ret = [];

      for(const id in this.daList) {
        const da = this.daList[id];
        // TBD: the format of `idf_list` or `odf_list` will be change in
        // near feature
        const featList = da[typeMap[type]] || [];
        const featSet = new Utils.Set(featList.map(el => {
          return el[0];
        }));  // DA feature set

        if (dFeatSet.issubset(featSet))
          ret.push(da);
      }
      return ret;
    },
  },
  props: {
    model: Object,
    daList: Object,
  },
  methods: {
    bindDA(da) {
      this.model.da = da;
      this.$dispatch('ctrl-panel-fin');
    },
  },
}
</script>

<style scoped>
div.ui.vertical.buttons {
  width: 100%;
}
</style>
