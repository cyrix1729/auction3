import Profile from '../components/Profile.vue'
import Listing from '../components/listings.vue'
import PostItem from '../components/postItem.vue'
import EditProfile from '../components/editProfile.vue'
import Item from '../components/getItem.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: "/makeListing",
        name: "Make Listing",
        component: PostItem
    },
    {
        path: "/profile",
        name: "Profile",
        component: Profile
    },
    {
        path: "/editProfile",
        name: "Edit Profile",
        component: EditProfile
    },
    {
        path: "/listings",
        name: "Listings",
        component: Listing
    }, 
    {
        path: '/',
        redirect: '/listings'
    },
    {
        path: '/item/:itemId',
        name: 'View Item',
        component: Item,
        props: true,
    }
]

const router = new createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

export default router