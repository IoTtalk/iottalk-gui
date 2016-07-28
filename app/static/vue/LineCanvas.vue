<template lang="jade">
  canvas#line-canvas
</template>

<script>
export default {
  data() {
    return {
    }
  },
  props: [
    'x',
    'y',
    'startx',
    'starty',
  ],
  methods: {
    onDraw(_alpha=1) {
      const ctx = this.ctx;
      const alpha = _alpha;

      ctx.clearRect(0, 0, this.$el.width, this.$el.height);
      
      ctx.beginPath();
      ctx.moveTo(this.startx, this.starty);
      ctx.lineTo(this.x, this.y);
      ctx.lineWidth = 5;
      ctx.strokeStyle = `rgba(221, 221, 221, ${alpha})`;
      ctx.lineCap = 'round';
      ctx.stroke();
      ctx.closePath();
    },
  },
  computed: {
    ctx(){
      const width = document.body.clientWidth;
      const height = document.body.clientHeight;
      const canvas = this.$el;
      
      canvas.width = width;
      canvas.height = height;

      return canvas.getContext('2d');
    },
  },
  watch: {
    'x': 'onDraw',
    'y': 'onDraw',
  },
  events: {
    'feature-dragend': function(){
      const self = this;
      
      function fadeOut(_alpha) {
        const alpha = _alpha - 0.1;

        self.onDraw(alpha);

        if (Math.floor(alpha * 10) == 0)
          return;

        setTimeout(() => {
            fadeOut(alpha)
        }, 100);
      }

      fadeOut(1);
    },
  },
}
</script>

<style scoped>
canvas {
  background-color: transparent;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
</style>
