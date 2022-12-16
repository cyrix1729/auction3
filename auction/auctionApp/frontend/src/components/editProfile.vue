<template>
    <div class="text-dark border rounded bg-light">
        <h1>
            Edit Profile
        </h1>
        <form id="putProfile" action="">
            Username: 
            <input class="bg-light rounded shadow" required v-model= user.username  />
            <br>
            Email: 
            <input class="bg-light rounded shadow" type = 'email' required v-model= user.email  />
            <br>
            Date of Birth: 
            <input class="bg-light rounded text-dark shadow" type = 'Date' required v-model= user.DOB  />
            <br>
            Profile Image: 
            <input class="form-control shadow" type="file" name="file" ref="post_image" accept="image/png, image/jpeg" @change="handleFileUpload( $event )"/>
            <button class="btn btn-info shadow" @click="editData">Update</button>
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
                file: File
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
                const form = document.getElementById('postImage');
                const formData = new FormData(form as any);
                formData.append('file', (this.file as any));

                try{
                    e.preventDefault()   
                    let payload = {
                    username: this.user.username,
                    email: this.user.email,
                    DOB: this.user.DOB,}
                    console.log(payload)

                    let res = await fetch(`http://127.0.0.1:8000/api/user`, {
                    'credentials': "include",
                    method: 'PUT',
                    headers: {
                        "X-CSRFToken": this.getCookie("csrftoken"),
                    },
                    body: formData,

                })}

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