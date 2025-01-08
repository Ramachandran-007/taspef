<template>
  <div 
    class="pdf-modal-container"
    @contextmenu.prevent
    @keydown.ctrl.67.prevent
    @keydown.ctrl.80.prevent
  >
    <!-- Close Button -->
    <button 
      @click="$emit('close')" 
      class="close-button"
      aria-label="Close PDF viewer"
    >
      <span class="text-xl">×</span>
    </button>

    <!-- Loading State -->
    <div v-if="loading" class="flex justify-center items-center h-full">
      <p class="text-gray-600">Loading PDF...</p>
    </div>

    <!-- Error State -->
    <div v-if="error" class="flex justify-center items-center h-full">
      <p class="text-red-600">{{ error }}</p>
    </div>

    <!-- PDF Content -->
    <div class="pdf-scroll-container" ref="scrollContainer" @scroll="onScroll">
      <div class="pdf-content p-4">
        <div v-for="pageNum in totalPages" :key="pageNum" class="page-wrapper mb-4">
          <div class="page-number">Page {{ pageNum }}</div>
          <canvas 
            :ref="el => setCanvasRef(el, pageNum)"
            class="mx-auto shadow-lg bg-white"
          ></canvas>
        </div>
      </div>
    </div>

    <!-- PDF Controls - Bottom Fixed -->
    <div class="pdf-controls">
      <div class="controls-wrapper">
        <div class="navigation-controls">
          <button 
            @click="scrollToPage(currentPage - 1)"
            class="control-button"
            :disabled="currentPage <= 1"
            aria-label="Previous Page"
          >
            Previous
          </button>
          
          <div class="page-navigation">
            <input 
              type="number"
              min="1"
              :max="totalPages"
              v-model="currentPageInput"
              @keyup.enter="scrollToPage(currentPageInput)"
              class="page-input"
              placeholder="Page"
              aria-label="Go to specific page"
            />
            <span class="text-gray-700">of {{ totalPages }}</span>
          </div>

          <button 
            @click="scrollToPage(currentPage + 1)"
            class="control-button"
            :disabled="currentPage >= totalPages"
            aria-label="Next Page"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { GlobalWorkerOptions } from 'pdfjs-dist';

GlobalWorkerOptions.workerSrc = '/node_modules/pdfjs-dist/build/pdf.worker.mjs';

const props = defineProps({
  pdfUrl: {
    type: String,
    required: true
  }
});

defineEmits(['close']);

const loading = ref(true);
const error = ref(null);
const scale = ref(1.0);
const currentPage = ref(1);
const currentPageInput = ref(1);
const totalPages = ref(0);
const scrollContainer = ref(null);
const pageCanvases = ref(new Map());
let pdfDoc = null;

const setCanvasRef = (el, pageNum) => {
  if (el) {
    pageCanvases.value.set(pageNum, el);
  }
};

const renderPage = async (pageNum) => {
  try {
    const canvas = pageCanvases.value.get(pageNum);
    if (!canvas) return;

    const page = await pdfDoc.getPage(pageNum);
    const viewport = page.getViewport({ scale: scale.value });
    const context = canvas.getContext('2d');
    
    canvas.height = viewport.height;
    canvas.width = viewport.width;

    const renderContext = {
      canvasContext: context,
      viewport: viewport
    };

    await page.render(renderContext).promise;
  } catch (err) {
    console.error(`Error rendering page ${pageNum}:`, err);
    error.value = `Error rendering page ${pageNum}`;
  }
};

const renderAllPages = async () => {
  for (let pageNum = 1; pageNum <= totalPages.value; pageNum++) {
    await renderPage(pageNum);
  }
};

const scrollToPage = (pageNum) => {
  if (pageNum < 1 || pageNum > totalPages.value) return;
  
  const canvasElement = pageCanvases.value.get(pageNum);
  if (canvasElement) {
    canvasElement.scrollIntoView({ behavior: 'smooth' });
    currentPage.value = pageNum;
    currentPageInput.value = pageNum;
  }
};

const onScroll = () => {
  if (!scrollContainer.value) return;
  
  // Debounce scroll handler
  clearTimeout(window.scrollTimeout);
  window.scrollTimeout = setTimeout(() => {
    updateCurrentPage();
  }, 100);
};

const updateCurrentPage = () => {
  if (!scrollContainer.value) return;

  const containerRect = scrollContainer.value.getBoundingClientRect();
  const containerMiddle = containerRect.top + (containerRect.height / 2);

  for (let [pageNum, canvas] of pageCanvases.value.entries()) {
    const rect = canvas.getBoundingClientRect();
    if (rect.top <= containerMiddle && rect.bottom >= containerMiddle) {
      currentPage.value = pageNum;
      currentPageInput.value = pageNum;
      break;
    }
  }
};

const loadPDF = async () => {
  if (!props.pdfUrl) {
    error.value = 'No PDF URL provided';
    loading.value = false;
    return;
  }

  loading.value = true;
  error.value = null;

  try {
    const loadingTask = pdfjsLib.getDocument(props.pdfUrl);
    pdfDoc = await loadingTask.promise;
    totalPages.value = pdfDoc.numPages;
    
    await renderAllPages();
    loading.value = false;
  } catch (err) {
    console.error('Error loading PDF:', err);
    error.value = `Error loading PDF: ${err.message}`;
    loading.value = false;
  }
};

watch(() => props.pdfUrl, loadPDF);
watch(() => scale.value, renderAllPages);

onMounted(() => {
  loadPDF();
});
</script>

<style scoped>
.pdf-modal-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: #f5f5f5;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  user-select: none;
  -webkit-user-select: none;
}

.close-button {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 2.5rem;
  height: 2.5rem;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 1010;
  transition: background-color 0.2s;
}

.close-button:hover {
  background: #f3f4f6;
}

.pdf-scroll-container {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  margin-bottom: 80px;
}

.pdf-content {
  max-width: 1200px;
  margin: 0 auto;
}

.page-wrapper {
  position: relative;
  padding: 1rem;
  background: white;
  border-radius: 0.5rem;
}

.page-number {
  position: absolute;
  top: 0.5rem;
  left: 0.5rem;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.875rem;
}

.pdf-controls {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: white;
  border-top: 1px solid #e5e7eb;
  padding: 1rem;
  z-index: 1010;
}

.controls-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.navigation-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.control-button {
  padding: 0.5rem 1rem;
  background: #4f46e5;
  color: white;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  transition: background-color 0.2s;
}

.control-button:hover:not(:disabled) {
  background: #4338ca;
}

.control-button:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}

.page-input {
  width: 4rem;
  padding: 0.25rem 0.5rem;
  border: 1px solid #e5e7eb;
  border-radius: 0.375rem;
  text-align: center;
}

.page-navigation {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

canvas {
  max-width: 100%;
  height: auto !important;
}
</style>