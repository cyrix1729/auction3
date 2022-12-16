<script lang="ts">
import Bid from './Bid.vue';
import Question from './Question.vue';
import Vue from 'vue';

    export default{
    props: ["itemId"],
    data() {
        return {
            getResult: false,
            getItemData: null,
            getUserData: null,
            image: null,
            media: 'http://127.0.0.1:8000/media/',
        };
    },
    methods: {

        getDateTime(date){
                let cal_date = date.slice(0, 10)
                let time = date.slice(12, 16)
                return (cal_date.concat(' at ',time))
            },

        async getItem() {
            try {
                const res = await fetch(`http://localhost:8000/getItem/${this.itemId}`, { method: "get", "credentials": "include", });
                if (!res.ok) {
                    const message = `An error has occured: ${res.status} - ${res.statusText}`;
                    throw new Error(message);
                }
                const data = await res.json();
                /*let fr = new FileReader();
                fr.onload = function(e) {
                    document.getElementById('myIcon').src = fr.result;
                };*/
                this.getResult = true;
                this.getItemData = data.item;
                this.getUserData = data.seller;
            }
            catch (err) {
                console.error(err);
            }
        },
    },
    created() {
        this.getItem();
    },
    components: { Question, Bid }
}
</script>

<template>
    <header>
      <div class="">
            <div v-if="getResult" class="alert alert-secondary mt-2" role="alert">
              <div class="row" v-for="item in getItemData">
                <div class="p-2">
                    <img :src= "media + item.image" width="100" height="100" class="rounded text-start">
                </div>
                <div class="col-sm-12 text-center text-dark">
                  <p>Item: {{item.name}}</p>
                  <p>Description: {{item.desc}}</p>
                  <p>Starting at: {{getDateTime(item.start_time)}}</p>
                  <p>Ending at: {{getDateTime(item.end_time)}}</p>
                  <p>Starting bid: £{{item.start_price}}</p>
                  <p>Current bid: £{{item.cur_price}}</p>
                  </div>
              </div>
              <div class="row" v-for="user in getUserData">
                <div class="col-sm-12 text-center">
                    <b>{{user.first_name}}</b>
                    <b>{{user.last_name}}</b>
                </div>
              </div>
            </div>
        </div>
        <Question v-bind:itemId="itemId"/>
        <Bid v-bind:itemId="itemId"/>
    </header>
  </template>
