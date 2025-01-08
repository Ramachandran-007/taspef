<template>
  <div class="container mx-auto px-4 py-8">
    <h2 class="text-2xl oxygen-bold mb-6">Namadhu Vanam E-Magazine</h2>

    <!-- Sorting Controls -->
    <div class="mb-6">
      <label class="oxygen-regular text-gray-600 mr-4">Sort By:</label>
      <select v-model="sortOrder" class="border rounded px-3 py-2 oxygen-regular">
        <option value="latest">Latest Issue</option>
        <option value="previous">Previous Issue</option>
      </select>
    </div>

    <!-- Loading and Error States -->
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-600 oxygen-regular">Loading magazines...</p>
    </div>
    <div v-else-if="error" class="text-center py-8">
      <p class="text-red-500 oxygen-regular">Error: {{ error }}</p>
    </div>

    <!-- Magazine Grid -->
    <div v-else class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <div v-for="issue in sortedMagazines" :key="issue.id" class="bg-white rounded-lg shadow-lg overflow-hidden">
        
        <div class="w-full h-48 bg-gray-200">
          <img v-if="issue.cover_image_url" :src="issue.cover_image_url" alt="Cover Image" class="w-full h-full object-cover" />
        </div>

        <div class="p-4">
          <h3 class="oxygen-bold text-xl mb-2">{{ issue.title }}</h3>
          <p class="oxygen-regular text-gray-600 mb-4">{{ formatDate(issue.date) }}</p>
          <button
            @click="openMagazine(issue)"
            class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 w-full oxygen-regular"
          >
            Read Magazine
          </button>
        </div>
      </div>
    </div>

    <!-- Secure PDF Viewer -->
    <SecurePDFViewer
      v-if="selectedMagazine"
      :pdfUrl="selectedMagazine.pdf_url"
      :show="pdfViewerVisible"
      @close="closePDFViewer"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import SecurePDFViewer from '../components/SecurePDFViewer.vue';

// State variables
const magazines = ref([]);
const sortOrder = ref('latest');
const loading = ref(true);
const error = ref(null);
const pdfViewerVisible = ref(false);
const selectedMagazine = ref(null);

// Format date for display
const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
};

// Parse date for sorting
const parseDate = (dateStr) => new Date(dateStr);

// Computed property to sort magazines
const sortedMagazines = computed(() => {
  const sorted = [...magazines.value].sort((a, b) => parseDate(b.date) - parseDate(a.date));
  return sortOrder.value === 'latest' ? sorted.slice(0, 1) : sorted.slice(1);
});

const fetchMagazines = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/magazines/');
    magazines.value = response.data.map(item => ({
      id: item.id,
      title: item.title,
      date: item.date,
      cover_image_url: item.cover_image_url,
      pdf_url: item.pdf_url // Using pdf_url instead of pdf_file to match API response
    }));
  } catch (err) {
    error.value = err.message || 'Failed to fetch magazines.';
  } finally {
    loading.value = false;
  }
};

// Open the PDF magazine
const openMagazine = (issue) => {
  if (!issue.pdf_url) {
    error.value = 'No PDF available for this magazine.';
    return;
  }
  selectedMagazine.value = issue;
  pdfViewerVisible.value = true;
};

// Close the PDF viewer
const closePDFViewer = () => {
  pdfViewerVisible.value = false;
  selectedMagazine.value = null;
};

// Fetch magazines when the component is mounted
onMounted(fetchMagazines);
</script>