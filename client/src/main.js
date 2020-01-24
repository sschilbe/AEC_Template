import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VTooltip from 'v-tooltip';
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false;
Vue.use(VTooltip);

new Vue({
 render: h => h(App),
 vuetify,
 /*
  * Put all globally available data here, this data can be accessed in .Vue files via:
  * -this.$root.$data...-
  */
 data: {

 }
}).$mount('#app');

