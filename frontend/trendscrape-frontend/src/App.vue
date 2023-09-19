<script setup>
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
import USData from './components/USData.vue';
import UKData from './components/UKData.vue';
</script>

<template>
  <div class="min-h-screen bg-gray-900 flex flex-col">

  
  <div class="flex fixed top-0 w-screen justify-center items-center text-center">
    <Navbar/>
  </div>

  <div class="flex mb-auto flex-grow justify-center mt-10">
    <USData/>
  </div>
  <div class="flex mb-auto flex-grow justify-center mt-10">
    <UKData/>
  </div>

  <div class="fixed bottom-0 left-0 w-screen ">
    <Footer/>
  </div>

</div>

</template>

