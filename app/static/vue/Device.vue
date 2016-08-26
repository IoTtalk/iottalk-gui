<template lang="jade">
  .ui.raised.segments.device
    .ui.segment
      .ui.header.center.aligned [[ model.name ]]
    .ui.segment
      a
        i.configure.icon
    .ui.feature.center.aligned.segment.feature-cell(
      v-for="feature in model.features"
    )
      .ui.raised.segment [[ feature | capitalize ]]
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
      canvas.width = canvas.height = 0;

      ev.dataTransfer.setData('text', 'XDD' + index)
      ev.dataTransfer.setDragImage(canvas, 0, 0)

      const pos = ev.target.getBoundingClientRect();
      this.$dispatch('feature-drag', {
        x: pos.right + 8,
        y: pos.y + pos.height / 2,
      })
      return false
    },
    onDragEnd(ev) {
      console.log('drag end')
      ev.target.classList.remove('selected')

      this.$dispatch('feature-dragend')
    },
    onDrop(ev) {
      console.log('dropped')
      const data = ev.dataTransfer.getData('text')
      console.log(data)

      this.dragging = -1
      ev.target.classList.remove('selected')
    },
    onDragEnter(idx, ev) {
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

.feature-cell {
  padding: 4px;
}
</style>
