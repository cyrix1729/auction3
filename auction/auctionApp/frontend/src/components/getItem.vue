<script lang="ts">

    export default{
    props: ["itemId"],
    data() {
        return {
            getResult: false,
            getItemData: null,
            getUserData: null,
            image: null,
        };
    },
    methods: {
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
}
</script>

<template>
    <header>
      <div class="">
            <div v-if="getResult" class="alert alert-secondary mt-2" role="alert">
              <div class="row" v-for="item in getItemData">
                  <div class="col-sm-12 text-center">
                    <b>{{item.name}}</b>
                    <b>{{item.desc}}</b>
                    <b>{{item.start_time}}</b>
                    <b>{{item.end_time}}</b>
                    <b>{{item.start_price}}</b>
                    <b>{{item.cur_price}}</b>
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
    </header>
  </template>