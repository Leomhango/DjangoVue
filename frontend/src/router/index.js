import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Add from '../views/Add.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Add',
    name: 'Add',
    component: Add
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
