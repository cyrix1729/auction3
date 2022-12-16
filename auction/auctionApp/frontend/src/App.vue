<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
</script>

<script lang="ts">
    export default {
        data(){
            return {
                user: [],
                // Media link - Contains all media (item images, profile pictures)
                media: 'http://127.0.0.1:8000/media/'
            }
        },

        methods: {
            // Logs a user out
            async logOut(){
                try{
                    let response = await fetch('http://localhost:8000/logout/',{
                    'credentials': "include",});
                    response = await fetch('http://127.0.0.1:8000/logout/',{
                    'credentials': "include",});
                      console.log("clicked");
                }
                catch(error){
                    console.log(error)
                }
                
            }, 
        }
    }





</script>


<template>
  <div class="row border rounded bg-dark shadow p-4">
  <ul>
    <h4 class="rounded bg-primary text-dark p-2"><router-link style="text decoration: none; color: inherit;" to="/profile">Profile</router-link></h4>
    <h4 class="rounded bg-primary text-dark p-2"><router-link style="text decoration: none; color: inherit;" to="/makeListing">Make A Listing</router-link></h4>
    <h4 class="rounded bg-primary text-dark p-2"><router-link style="text decoration: none; color: inherit;" to="/listings">Listings</router-link></h4>
    <h4 class="rounded bg-primary text-dark p-2"><button class="bg-danger rounded text-dark p-2" @click = 'logOut'>Log Out</button></h4>
  </ul>
  <router-view></router-view>
  </div>
</template>


