<template>
  <div class="fixed inset-0 bg-white">
    <!-- Header -->
    <div class="bg-green-800 text-white px-4 py-2 flex items-center justify-between">
      <h1 class="text-lg font-bold">{{ title }}</h1>
      <button 
        @click="goBack"
        class="p-2 hover:bg-green-700 rounded-full"
      >
        <XMarkIcon class="h-6 w-6" />
      </button>
    </div>

    <!-- PDF Viewer -->
    <div class="h-[calc(100vh-3rem)] overflow-auto">
      <SecurePDFViewer 
        v-if="pdfUrl"
        :pdf-url="pdfUrl"
        class="h-full w-full"
      />
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { XMarkIcon } from '@heroicons/vue/24/outline';
import SecurePDFViewer from '../components/SecurePDFViewer.vue';

const route = useRoute();
const router = useRouter();

const pdfUrl = computed(() => route.query.url?.toString());
const title = computed(() => route.query.title?.toString());

onMounted(() => {
  if (!pdfUrl.value) {
    console.error('No PDF URL provided');
    router.push('/magazine');
  }
});

const goBack = () => {
  router.back();
};
</script>
