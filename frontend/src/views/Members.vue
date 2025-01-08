<template>
  <div class="container mx-auto px-4 py-4">
    <marquee class="text-[#FF2929] font-semibold mb-2">
      FORM NO VI - Register of members to be maintained under sub-section (1) of section 14 of the Tamilnadu Societies Registration Act, 1975 (Tamil Nadu Act 27 of 1975)
    </marquee>

    <div class="text-white p-6 mb-4" style="background-color: #001A6E;">
      <div class="text-center text-xl font-bold">
        REGISTER OF MEMBERS
      </div>
      <div class="text-center mt-2">
        <div>Name and address of the society: <strong>Tamil Nadu Association of Senior Professionals of Environment and Forests</strong></div>
        <div>Date of Registration: <strong>10.09.2007</strong></div>
        <div>The Registration number and Year of Registration: <strong>270/2007</strong></div>
        <div class="mt-4 font-semibold">LIST OF LIFE MEMBERS AS ON 22.09.2024</div>
      </div>
    </div>

    <div class="flex items-center justify-between mb-6">
      <h2 class="text-2xl font-bold">Our Members</h2>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search members"
        class="w-full md:w-80 px-4 py-1 border border-gray-400 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
      />
    </div>

    <!-- Members List -->
    <div class="bg-white rounded-lg shadow-lg overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">S.No.</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Subscription</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Joining Date</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Contact Number</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="(member, index) in filteredMembers" :key="member.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-500">{{ index + 1 }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex space-x-2">
                  <div class="text-sm font-medium text-gray-900">{{ member.name }},</div>
                  <div class="text-sm text-gray-500">{{ member.designation }}</div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                  {{ member.subscription }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ formatDate(member.joining_date) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ member.phone || '-' }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { membersService } from '../services/membersService'

const members = ref([])
const searchQuery = ref('')
const loading = ref(true)

const filteredMembers = computed(() => {
  if (!searchQuery.value) return members.value
  
  const query = searchQuery.value.toLowerCase()
  return members.value.filter(member => 
    member.name.toLowerCase().includes(query) ||
    member.designation.toLowerCase().includes(query) ||
    (member.occupation && member.occupation.toLowerCase().includes(query))
  )
})

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-IN', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  })
}

onMounted(async () => {
  try {
    members.value = await membersService.getAllMembers()
  } catch (error) {
    console.error('Failed to load members:', error)
  } finally {
    loading.value = false
  }
})
</script>