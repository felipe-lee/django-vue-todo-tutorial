// main.js

import Vue from 'vue';

import App from './App';
import store from './store/store.js';

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store: store,
  components: {App},
  render: h => h(App)
});
