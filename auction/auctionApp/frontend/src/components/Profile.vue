<template>
    <div>
        <h1>
             Profile
        </h1>
        <div class="form-group">
       <button @click = 'logOut'>Log Out</button>
       <a href = '/editProfile'>
        <button @click = 'editProfile'>Edit Profile</button>
       </a>
       <br>
       <b>Profile Picture:</b> <br>
        <img :src="media + user.image" width="100" height="100">
        <b>Username:</b> {{user.username}}<br>
       <b>Email:</b> {{user.email}}<br>
       <b>Date of Birth:</b> {{user.DOB}}<br>
        
            </div>
      
    </div>
    

</template>

<script lang="ts">
    export default {
        data(){
            return {
                user: [],
                media: 'http://127.0.0.1:8000/media/'
            }
        },
        created(){
            this.fetchUser()
        },

        methods: {
            
            
            async fetchUser(){
                try{
                    let response = await fetch('http://127.0.0.1:8000/api/user',{
                    'credentials': "include",})
                    let data = await response.json()
                    this.user = data.cur_user_data
                    this.user.image = this.user.image.slice(1, -1)
                }
                    catch(error){
                        console.log(error)
                    }
                
            },
            
            async logOut(){
                try{
                    let response = await fetch('http://127.0.0.1:8000/logout/',{
                    'credentials': "include",})
                
                }
                catch(error){
                    console.log(error)
                }
                
            },

            async editProfile(){
                try{
                    let response = await fetch('http://127.0.0.1:8000/logout/',{
                    'credentials': "include",})
                
                }
                catch(error){
                    console.log(error)
                }
                
            },
            
        }
    }





</script>