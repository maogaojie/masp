// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import header from './components/header.vue'
import foot from './components/foot.vue'

Vue.config.productionTip = false
    // Vue.prototype.axios = axios // 全局注册
    // axios.defaults.withCredentials = true;
Vue.component('hd', header)
Vue.component('foot', foot)
    /* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
})
