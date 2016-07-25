import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './vue/App.vue'
import Home from './vue/Home.vue'

Vue.config.delimiters = ['[[', ']]']
Vue.config.unsafeDelimiters = ['[[[', ']]]']

Vue.use(VueRouter)

const router = new VueRouter()

router.map({
  '/': {
    component: Home,
  }
})

router.start(App, 'body')
