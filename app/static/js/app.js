Vue.config.delimiters = ['[[', ']]']
Vue.config.unsafeDelimiters = ['[[[', ']]]']


const app = Vue.extend({})

const router = new VueRouter()

router.start(app, 'body')
