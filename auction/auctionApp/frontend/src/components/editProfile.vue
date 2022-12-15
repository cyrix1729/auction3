<template>
    <div>
        <h1>
            Edit Profile
        </h1>
        <form @submit = 'editData' method="post">
            Username: 
            <input required v-model= user.username  />
            <br>
            Email: 
            <input type = 'email' required v-model= user.email  />
            <br>
            Date of Birth: 
            <input type = 'Date' required v-model= user.DOB  />
            <br>
            Profile Image: 
            <input class="form-control" type="file" name="file" ref="post_image" accept="image/png, image/jpeg" @change="handleFileUpload( $event )" required/>
            <input type="submit" value="Update" />
        </form>

        

    </div>
    

</template>

<script lang="ts">
import Vue from 'vue'  
import axios from 'axios'
import VueAxios from 'vue-axios'

    export default {
        data(){
            return {
                user: [],
            }
        },
        created(){
            this.fetchUser()
        },

        methods: {
            handleFileUpload(event : Event){
                if (event.target != null){
                    this.file = (event.target as any).files[0];
                }
            },
            async postItem() {
                const form = document.getElementById('postItem');
                const formData = new FormData(form as any);
                formData.append('file', (this.file as any));
                formData.append('seller', this.userId);
                try {
                    console.log("uwu")
                        const res = await fetch('http://localhost:8000/postItem', { 
                            method: "post",
                            body : formData,
                            'credentials': "include",
                        });
                    }
                catch(e){
                    console.log(e)
                }
            },

            getCookie(ck) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== "") {
                    const cookies = document.cookie.split(";");
                    for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, ck.length + 1) === (ck + "=")) {
                        cookieValue = decodeURIComponent(cookie.substring(ck.length + 1));
                        break;
                    }
                    }
                }
                return cookieValue;
    },
            async editData(e){
                try{
                    e.preventDefault()   
                    let payload = {
                    username: this.user.username,
                    email: this.user.email,
                    DOB: this.user.DOB,}
                    console.log(payload)
                    let response = await fetch(`http://127.0.0.1:8000/api/user`, {
                    'credentials': "include",
                    method: 'PUT',
                    headers: {
                    'Content-Type': 'application/json',
                    "X-CSRFToken": this.getCookie("csrftoken"),
                    },
                    body: JSON.stringify(payload)})
                }
                catch(error){
                        console.log(error)
                    }
            
            },

            async fetchUser(){
                try{
                    let response = await fetch('http://127.0.0.1:8000/api/user',{
                    'credentials': "include",})
                    let data = await response.json()
                    this.user = data.cur_user_data
                    
                }
                    catch(error){
                        console.log(error)
                    }
                
            },

            
        }
    }

        

</script>