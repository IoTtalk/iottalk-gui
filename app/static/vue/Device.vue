<template lang="jade">
  .ui.raised.segments.device
    .ui.segment
      .ui.header.center.aligned [[ model.name ]]
    .ui.segment
      a
        i.configure.icon
    .ui.feature.center.aligned.segment(
      v-for="feature in model.features"
      draggable="true"
      v-on:dragstart="onDragStart($index, $event)"
      v-on:dragend="onDragEnd"
      v-on:drop.prevent.stop="onDrop"
      v-on:dragenter="onDragEnter($index, $event)"
      v-on:dragleave="onDragLeave($index, $event)"
    )
      // v-bind:class="{selected: (dragging == $index)}"
      span(style="z-index: -1: position: absolute")
        i.tag.icon
        | [[ feature | capitalize ]]
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
      ev.target.classList.add('selected')

      const canvas = document.createElementNS("http://www.w3.org/1999/xhtml","canvas");

      ev.dataTransfer.setData('text', 'XDD' + index)
      ev.dataTransfer.setDragImage(canvas, 25, 25)

      const pos = ev.target.getBoundingClientRect();
      this.$dispatch('feature-drag', {
        x: pos.right + 8,
        y: pos.y + pos.height / 2,
      })
      return false
    },
    onDragEnd(ev) {
      console.log('drag end')
      // this.dragging = -1
      ev.target.classList.remove('selected')
    },
    onDrop(ev) {
      console.log('dropped')
      const data = ev.dataTransfer.getData('text')
      console.log(data)
      this.dragging = -1
      ev.target.classList.remove('selected')
    },
    onDragEnter(idx, ev) {
      // this.dragging = idx;
      ev.target.classList.add('selected')
    },
    onDragLeave(idx, ev) {
      if (this.dragging !== idx)
        ev.target.classList.remove('selected')
    },
  },
}
</script>

<style scoped>
div.device div.selected{
  box-shadow: 0px 2px 5px #acacac inset;
}
</style>
