<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavMain from './components/main/NavMain.vue';

</script>

<template>
  <NavMain />
  <main class="main-content position-relative max-height-vh-100 h-100 border-radius-lg ">
    <RouterView />
  </main>
</template>