import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import ElementUI from 'element-ui';
import axios from 'axios';
import 'element-ui/lib/theme-chalk/index.css';
import 'font-awesome/css/font-awesome.min.css';
import qs from 'qs';
import VCharts from 'v-charts';
import Mint from 'mint-ui';
import 'mint-ui/lib/style.css';
import './assets/js/btnPermissions';

Vue.use(ElementUI);
Vue.use(VCharts);
Vue.use(Mint);
Vue.prototype.axios = axios
Vue.prototype.qs = qs

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
