import Vue from 'vue'
import VueProgressBar from 'vue-progressbar'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

import 'animate'  // animate.css
import 'semantic'  // semantic-ui

import App from './vue/App.vue'
import Home from './vue/Home.vue'
import Proj from './vue/Proj.vue'


Vue.use(VueProgressBar, {
  color: 'rgb(143, 255, 199)',
  failedColor: 'red',
  height: '2px'
});
Vue.use(VueRouter);
Vue.use(VueResource);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Vue.component('home', Home),
  },
  {
    path: '/proj/:pid',
    name: 'proj',
    component: Vue.component('proj', Proj),
  }
]

const router = new VueRouter({
  routes,
  linkActiveClass: 'active',
})

const app = new Vue({
  el: 'body',
  router,
  render: h => h(App),
});
