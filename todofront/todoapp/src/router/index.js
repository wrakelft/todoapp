import { createRouter, createWebHistory } from 'vue-router'
import TaskView from '../views/TaskView.vue'
import ProfileView from '../views/ProfileView.vue'

const routers = [
  {
    path: '/',
    name: 'Tasks',
    component: TaskView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})
 
export default router
