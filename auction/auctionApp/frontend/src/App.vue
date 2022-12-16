<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
</script>
<template>
  <ul>
    <li><router-link to="/profile">Profile</router-link></li>
    <li><router-link to="/makeListing">Make A Listing</router-link></li>
    <li><router-link to="/listings">Listings</router-link></li>
  </ul>
  <router-view></router-view>
</template>


