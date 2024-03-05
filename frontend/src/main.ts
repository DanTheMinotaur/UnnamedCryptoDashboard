import './assets/css/nucleo-icons.css'
import './assets/css/nucleo-svg.css'
import './assets/css/material-dashboard.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
