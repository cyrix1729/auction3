import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import './style.css'
import App from './App.vue'
import router from './router'
// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { createApp } from 'vue'


createApp(App).use(router).mount('#app')
