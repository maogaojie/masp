import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import index from '@/components/index'
Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
        path: '/s',
        name: 'HelloWorld',
        component: HelloWorld
    }, {
        path: '/',
        name: 'index',
        component: index
    }]
})
