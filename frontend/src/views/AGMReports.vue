<template>
  <div class="container mx-auto px-4 py-8">
    <h2 class="text-2xl font-bold mb-6">AGM Reports</h2>
    <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      <div v-for="report in reports" :key="report.id" class="bg-white p-4 rounded-lg shadow">
        <h3 class="font-semibold mb-2">{{ report.title }}</h3>
        <p class="text-gray-600 mb-4">{{ report.date }}</p>
        <button
          @click="openReport(report)"
          class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          View Report
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const reports = [
  {
    id: 1,
    title: 'Annual General Meeting 2024',
    date: 'September 24, 2024',
    url: '/agm-report-detail/1'
  },
  // Add more reports as needed
];

const openReport = (report) => {
  router.push({
    name: 'agm-detail',
    params: { id: report.id }
  });
};
</script>