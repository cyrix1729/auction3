<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
</script>
<template>
  <div class="row border rounded bg-dark shadow p-4">
  <ul>
    <h4 class="rounded bg-primary text-dark p-2"><router-link style="text decoration: none; color: inherit;" to="/profile">Profile</router-link></h4>
    <h4 class="rounded bg-primary text-dark p-2"><router-link style="text decoration: none; color: inherit;" to="/makeListing">Make A Listing</router-link></h4>
    <h4 class="rounded bg-primary text-dark p-2"><router-link style="text decoration: none; color: inherit;" to="/listings">Listings</router-link></h4>
  </ul>
  <router-view></router-view>
  </div>
</template>


