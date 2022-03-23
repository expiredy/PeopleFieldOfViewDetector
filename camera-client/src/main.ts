import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { useSockets } from '@/compositions/useSockets'

const sendingVideoFrames = useSockets()

createApp(App).use(router).mount('#app')
