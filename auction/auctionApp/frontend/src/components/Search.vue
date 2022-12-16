<script lang="ts">
import listings from './listings.vue';
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
        listings,
      }
    }
</script>

<template>
    <input class="bg-light" required placeholder= 'search' ref="searchField"/>
    <button class="bg-info text-white" v-on:click="search">SEARCH</button>
    <listings v-bind:searchData="searchData" :key="componentKey"/>
</template>