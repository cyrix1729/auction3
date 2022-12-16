<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import Profile from './components/Profile.vue'
import editProfile from './components/editProfile.vue'
import listings from './components/listings.vue'
import PostItem from './components/postItem.vue';
import GetQuestionsOnItems from './components/GetQuestionsOnItems.vue';
</script>

<script lang="ts">
export default {
  data() {
        return {
          searchData: '-',
          componentKey: 0,
        };
    },
  methods: {
        search() {
            if (this.$refs.searchField.value.length > 0){
                this.searchData = (this.$refs.searchField.value as string);
                this.forceRerender();
            }
            else{
              this.searchData = '-';
              this.forceRerender();
            }
        },
        forceRerender() {
            this.componentKey += 1;
        },
      },
      components: {
        listings, PostItem,
      }
    }
</script>
<template>
  <button class="bg-primary text-light"> Profile </button>
  <router-link to="/makeListing">Make A Listing</router-link>
  <input required placeholder= 'search' ref="searchField"/>
  <button v-on:click="search">SEARCH</button>
  <listings v-bind:searchData="searchData" :key="componentKey"/>
  <Profile/>
  <editProfile/>
</template>


