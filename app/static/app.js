import Vue from 'vue'
import VueProgressBar from 'vue-progressbar'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

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

const router = new VueRouter();
const app = Vue.extend(App);

router.map({
  '/': {
    name: 'home',
    component: Vue.component('home', Home),
  },
  '/proj/:pid': {
    name: 'proj',
    component: Vue.component('proj', Proj),
  },
})

router.start(app, 'body');
