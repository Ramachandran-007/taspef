<template>
    <div class="container mx-auto px-4 py-8 max-w-4xl">
      <!-- Back button -->
      <button 
        @click="router.back()" 
        class="mb-6 flex items-center text-green-600 hover:text-green-700"
      >
        <span class="mr-2">←</span> Back to Reports
      </button>
  
      <!-- Header Section -->
      <div class="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h1 class="text-2xl font-bold text-center mb-4">Tamilnadu Association of Senior Professional of Environment and Forestry (TASPEF)</h1>
        <h2 class="text-xl text-center mb-4">Minutes of the XVIII Annual General Body Meeting</h2>
        <div class="text-gray-600 text-center">
          <p>Date: September 24, 2024</p>
          <p>Time: 11:00 AM</p>
          <p>Venue: IFS Officers Mess, Velacherry, Chennai</p>
        </div>
      </div>
  
      <!-- Main Content -->
      <div class="bg-white rounded-lg shadow-lg p-6">
        <!-- Attendees Section -->
        <section class="mb-8">
          <h3 class="text-lg font-semibold mb-4 text-green-700">Meeting Officials</h3>
          <div class="pl-4">
            <p class="mb-2">President: Dr.V.T.Kandasamy IFS, CCF (Retd)</p>
            <p class="mb-2">Chief Guest: Dr T. Sekar. IFS, PCCF(Retd)</p>
            <p class="mb-2">Guest of Honour: Thiru N. Krishnakumar, IFS, PCCF& HoFF (Retd)</p>
          </div>
        </section>
  
        <!-- Members Present -->
        <section class="mb-8">
          <h3 class="text-lg font-semibold mb-4 text-green-700">Members Present</h3>
          <ul class="list-disc pl-8">
            <li>Thiru V. Prabhakaran, IFS, APCCF (Retd)</li>
            <li>Thiru D. Arun, IFS, CF(Retd)</li>
            <li>Thiru S. Dhandayuthapani, DCF (Retd)</li>
            <li>Thiru G. Sivagurunathan, ACF (Retd)</li>
            <li>Thiru P.Ramachandran, ACF (Retd)</li>
            <li>Thiru P. Jeyabalan, IFS, DCF(Retd)</li>
            <li>Dr S. Davidraj, ACF(Retd)</li>
          </ul>
        </section>
  
        <!-- Additional Members -->
        <section class="mb-8">
          <h3 class="text-lg font-semibold mb-4 text-green-700">Additional Members Joined</h3>
          <ul class="list-disc pl-8">
            <li>Thiru S. Deepalingam, DCF(Retd)</li>
            <li>Thiru S. Palanichamy, DCF (Retd)</li>
            <li>Thiru S.B.Thiruvengadam, ACF (Retd)</li>
            <li>Thiru S. Velumani, IFS, DCF(Retd)</li>
            <li>Thiru G. Ramprasath, AD,Statistics (Retd)</li>
          </ul>
        </section>
  
        <!-- Agenda Items -->
        <section class="mb-8">
          <h3 class="text-lg font-semibold mb-4 text-green-700">Agenda Items and Resolutions</h3>
          <div class="space-y-4">
            <div v-for="(item, index) in agendaItems" :key="index" class="bg-gray-50 p-4 rounded-lg">
              <h4 class="font-semibold mb-2">{{ item.title }}</h4>
              <p class="text-gray-700">{{ item.resolution }}</p>
            </div>
          </div>
        </section>
  
        <!-- Closing -->
        <section class="mb-8">
          <h3 class="text-lg font-semibold mb-4 text-green-700">Meeting Conclusion</h3>
          <p>The AGM concluded at 2:00 PM with National Anthem.</p>
          <div class="mt-4 flex justify-between">
            <div>
              <p class="font-semibold">Dr.V.T.Kandasamy IFS (Retd)</p>
              <p>President</p>
            </div>
            <div>
              <p class="font-semibold">D.Arun</p>
              <p>General Secretary</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter, useRoute } from 'vue-router';

    const router = useRouter();
    const route = useRoute();

    const reportId = route.params.id;

  const agendaItems = [
    {
      title: "1. Approval of Previous Minutes",
      resolution: "The General Body resolved and approved the minutes of the XVI th meeting held on 17.09.2023 without any change."
    },
    {
      title: "2. Approval of Accounts",
      resolution: "The General Body approved the statements of accounts for the year 2023-24 with Audited report."
    },
    {
      title: "3. Statutory Auditor Nomination",
      resolution: "Unanimously resolved to continue the services of M/S S. Ganapathy & Co, Chennai 34, as Statutory Auditor for 2024-25."
    },
    {
      title: "4. Namathu Vanam E-magazine",
      resolution: "The AGM appreciated the Editorial Board and requested all members to contribute their experiences related to forestry, wildlife, and administrative matters."
    },
    {
      title: "5. Consultancy Services",
      resolution: "Resolved to continue efforts with the Forest Department and other departments to get projects for TASPEF."
    },
    {
      title: "6. Office Accommodation",
      resolution: "Resolved to continue efforts with PCCF & HoFF to accommodate the TASPEF office."
    },
    {
      title: "7. Website Development",
      resolution: "Resolved to create a website for TASPEF, with Dr S. David Raj assigned to create and maintain it."
    },
    {
      title: "8. Editorial Board Update",
      resolution: "Approved to include Mr G. Ramprasath as an Editorial Board member of Namathu Vanam."
    },
    {
      title: "9. Asset Disposal",
      resolution: "Resolved to entrust the Treasurer to dispose of useless items, except the AC which can be repaired for future use."
    },
    {
      title: "10. New Membership",
      resolution: "Resolved to request all members to enroll new members by introducing their retired friends."
    },
    {
      title: "11. Financial Resolution",
      resolution: "Approved Rs 1.00 lakh for presenting mementos/complements to all life members in the next AGM."
    }
  ];
  </script>
  
  <style scoped>
  .container {
    font-family: system-ui, -apple-system, sans-serif;
  }
  </style>