import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

if (window.Telegram?.WebApp) {
  window.Telegram.WebApp.ready(); // WebApp is ready
  window.Telegram.WebApp.expand(); // fullsize window
}

app.use(router)

app.mount('#app')
