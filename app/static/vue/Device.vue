<template lang="jade">
  .ui.raised.segments.device
    .ui.segment
      .header.center.aligned [[ model.name ]]
    .ui.segment
      a
        i.configure.icon
    .ui.center.aligned.feature.segment(
      v-for="feature in model.features"
      draggable="true"
      v-on:dragstart="onDragStart($index, $event)"
      v-on:dragend="onDragEnd"
      v-on:drop.prevent.stop="onDrop"
      v-bind:class="{selected: (dragging == $index)}"
    )
      i.tag.icon
      | [[ feature | capitalize ]]
      // a.right.floated.conn-point
      //   i.square.icon
</template>

<script>
export default {
  data() {
    return {
      dragging: -1,
    }      
  },
  props: {
    model: Object,
  },
  methods: {
    onDragStart(index, ev) {
      console.log('drag start ' + index)
      this.dragging = index

      const canvas = document.createElementNS("http://www.w3.org/1999/xhtml","canvas");

      ev.dataTransfer.setData('text', 'XDD' + index)
      ev.dataTransfer.setDragImage(canvas, 25, 25)
      return false
    },
    onDragEnd(ev) {
      console.log('drag end')
      this.dragging = -1
    },
    onDrop(ev) {
      console.log('dropped')
      const data = ev.dataTransfer.getData('text')
      console.log(data)
    },
  },
}
</script>

<style scoped>
a.conn-point i{
  position: absolute;
  color: #acacac;
}
div.device div.selected{
  box-shadow: 0px 2px 5px #acacac inset;
}
</style>
