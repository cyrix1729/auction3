<template>
    <input class="bg-light text-dark" required placeholder= 'search' ref="searchField"/>
    <button class="bg-info text-white" v-on:click="search">SEARCH</button>
    <p></p>
    <div>
        <ul v-if="active" class="col-sm">
            <h1 class="rounded bg-primary p-4">Listings</h1>
            <p class= "rounded bg-light shadow text-info p-4 text-start"  v-for = "element in items.item">
                <div class="d-flex flex-row">
                    <div class="p-2">
                        <img :src= "media + getImage(element)" width="100" height="100" class="rounded text-start">
                    </div>
                    <div class="p-2">
                        <h4 class="text-dark">{{ element.name }}</h4>
                        Description: <i>{{ element.desc }}</i><br>
                        Started on: {{ getStartDate(element.start_time) }}<br>
                        Ending on: {{ getEndTime(element.end_time)}}<br>
                        Starting Price: £{{ element.start_price }}<br>
                        Current Price: £{{ element.cur_price }} <br>
                    </div>
                </div>
                <button class="btn btn-sm btn-success mt-3 rounded bg-primary text-light p-2">
                    <router-link style="text decoration: none; color: inherit;" :to="{name: 'View Item', params: {itemId: element.id}}">SHOW ITEM</router-link>
                </button>
            </p>



            <div v-if="items.item.length <= 0">
                <b class="text-light">There is no listing related to {{searchData}}</b>
            </div>
        </ul>
    </div>
</template>


<script lang="ts">
import Vue from 'vue';
    export default {
        data(){
            return {
                items: [] ,
                active: false,
                media: 'http://127.0.0.1:8000/media/',
                showItem: false,
                itemToDisplay: 0,
                componentKey: 0,
                searchData: '-',
            }




        },
        created(){
            this.fetchListings()
        },

        methods: {
            search(){
                if (this.$refs.searchField.value.length > 0){
                this.searchData = (this.$refs.searchField.value as string);
            }
            else{
              this.searchData = '-';
            }
            this.fetchListings();
            },
            getImage(item){
                console.log(item.image.slice(1,-1));
               return item.image.slice(1,-1)
            },

            getStartDate(date){
                return date.slice(0, 10)
            },

            getEndTime(date){
                let cal_date = date.slice(0, 10)
                let time = date.slice(12, 16)
                return (cal_date.concat(' at ',time))
            },



            async fetchListings(){
                try{
                    let response = await fetch(`http://localhost:8000/api/listings/${this.searchData}`)
                    let data = await response.json()
                    this.items = data
                    console.log(this.items)
                    this.active = true;
                }
                    catch(error){
                        console.log(error)
                    }

            },
            displayItem (item_id : number){
                this.itemToDisplay = item_id;
                if (this.showItem == false){
                    this.showItem = !this.showItem;
                }
                else{
                    console.log("forcing reload")
                this.forceRerender();
                }
            },
        forceRerender() {
            this.componentKey += 1;
        },

        },
      }

  </script>
