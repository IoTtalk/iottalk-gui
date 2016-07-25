import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './vue/App.vue'

Vue.config.delimiters = ['[[', ']]']
Vue.config.unsafeDelimiters = ['[[[', ']]]']

Vue.use(VueRouter)

const router = new VueRouter()

router.start(App, 'body')
