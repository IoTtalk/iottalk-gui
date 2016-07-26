import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

import App from './vue/App.vue'
import Home from './vue/Home.vue'
import Proj from './vue/Proj.vue'

Vue.config.delimiters = ['[[', ']]']
Vue.config.unsafeDelimiters = ['[[[', ']]]']

Vue.use(VueRouter)
Vue.use(VueResource)

const router = new VueRouter()

router.map({
  '/': {
    name: 'home',
    component: Home,
  },
  '/proj/:pid': {
    name: 'proj',
    component: Proj,
  },
})

router.start(App, 'body')
