import Vue from 'vue'
import VueRouter from  'vue-router'
import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import PostItem from '../components/postItem.vue'
import { createRouter, createWebHistory } from 'vue-router'
import { processExpression } from '@vue/compiler-core'

Vue.use(VueRouter)

const routes = [
    {
        path: "/makeListing",
        name: "Make Listing",
        component: () => import('../components/postItem.vue')
    },
]

const router = new VueRouter({
    mode: 'history',
    base: processExpression.env.BASE_URL,
    routes
})

export default router