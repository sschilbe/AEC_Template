import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false

new Vue({
 render: h => h(App),
 router,
 vuetify,
 /* 
  * Put all globally available data here, this data can be accessed in .Vue files via:
  * -this.$root.$data...-
  */
 data: {

 }
}).$mount('#app')
