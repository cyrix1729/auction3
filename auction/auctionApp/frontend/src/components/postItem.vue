<script lang="ts">
import { VueElement } from 'vue';

    export default {
        data() {
            return {
                getResult: null,
                file: File,
            }
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
                try {
                        const res = await fetch('http://localhost:8000/postItem', { 
                            method: "post",
                            body : formData,
                            'credentials': "include",
                        });
                        console.log(formData);
                        if (!res.ok) {
                            const message = `An error has occured: ${res.status} - ${res.statusText}`;
                            throw new Error(message);
                        }
                        
                        const data = await res.json();

                        const result = {
                            status: res.status + "-" + res.statusText,
                            headers: {
                                "Content-Type": res.headers.get("Content-Type"),
                                "Content-Length": res.headers.get("Content-Length"),
                            },
                            data: data,
                        };

                        this.getResult = data;

                } catch (err) {
                    console.error(err);
                }
            },
        },
    }
</script>


<template>
  <header>
    <div class="">
        <b>Item</b>
        <form id="postItem">
            <div class="form-group">
                <h24 class="text-light">name:</h24>
                <input class="form-control" type="text" name="name" ref="post_name" placeholder="name" required/>
            </div>
            <div class="form-group">
                <h24 class="text-light">description:</h24>
                <input class="form-control" type="text" name="desc" ref="post_desc" placeholder="description" required/>
            </div>
            <div class="form-group">
                <h24 class="text-light">starting at:</h24>
                <input class="form-control" type="datetime-local" name="startTime" ref="post_startTime" required/>
            </div>
            <div class="form-group">
                <h24 class="text-light">ending at:</h24>
                <input class="form-control" type="datetime-local" name="endTime" ref="post_endTime" required/>
            </div>
            <div class="form-group">
                <h24 class="text-light">starting bid:</h24>
                <input class="form-control" type="number" name="startPrice" ref="post_startPrice" required/>
            </div>
            <div class="form-group">
                <h24 class="text-light">post image:</h24>
                <input class="form-control" type="file" name="file" ref="post_image" accept="image/png, image/jpeg" @change="handleFileUpload( $event )" required/>
            </div>
            <div class="form-group">
                <button class="btn btn-primary" @click="postItem">SUBMIT</button>
            </div>
        </form>
      </div>
  </header>
</template>