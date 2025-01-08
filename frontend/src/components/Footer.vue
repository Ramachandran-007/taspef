<template>
  <footer class="bg-green-600 text-white py-4 mt-auto">
    <div class="text-xs container mx-auto px-4 flex flex-col md:flex-row justify-between items-center text-center md:text-left">
      <div class="mb-2 md:mb-0">
        Copyright &copy; {{ currentYear }} TASPEF. All rights reserved.
      </div>
      <div>
        Powered by <a href="https://www.skieztechnologies.org/" target="_blank" rel="noopener noreferrer" class="text-[#FFFBE6] hover:text-[#563A9C]">Skiez Technologies India Private Limited.</a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue';

const currentYear = ref(new Date().getFullYear());
</script>