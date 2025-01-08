<template>
  <div class="min-h-screen">
    <!-- Hero Section with Video Background -->
    <div class="relative h-[500px]">
      <div class="absolute inset-0 overflow-hidden">
        <video 
          autoplay 
          loop 
          muted 
          playsinline
          class="absolute w-full h-full object-cover"
        >
          <source src="/img/Home.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
        <!-- Overlay -->
        <div class="absolute inset-0 bg-black bg-opacity-40"></div>
        <!-- Content -->
        <div class="relative h-full flex items-center justify-center">
          <div class="text-center text-white px-4">
            <h2 class="text-3xl md:text-4xl font-bold mb-4">Preserving Our Natural Heritage</h2>
            <p class="text-xl md:text-2xl">Working together to protect and conserve Tamil Nadu forests</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Quick Links Section -->
    <div class="bg-white py-12">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div 
            v-for="link in quickLinks" 
            :key="link.title"
            class="bg-green-50 rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow duration-300"
          >
            <component :is="link.icon" class="h-12 w-12 text-green-600 mb-4" />
            <h3 class="text-xl font-semibold text-green-800 mb-2">{{ link.title }}</h3>
            <p class="text-gray-600 mb-4">{{ link.description }}</p>
            <router-link 
              :to="link.href"
              class="inline-block bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 transition-colors duration-200"
            >
              Learn More
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Latest Updates Section -->
    <div class="bg-gray-50 py-12">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl font-bold text-green-800 mb-8 text-center">Latest Updates</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div 
            v-for="update in latestUpdates" 
            :key="update.title"
            class="bg-white rounded-lg shadow-md overflow-hidden"
          >
            <img :src="update.image" :alt="update.title" class="w-full h-48 object-cover" />
            <div class="p-6">
              <h3 class="text-xl font-semibold text-green-800 mb-2">{{ update.title }}</h3>
              <p class="text-gray-600 mb-4">{{ update.description }}</p>
              <p class="text-sm text-gray-500">{{ update.date }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { 
  BookOpenIcon,
  UserGroupIcon,
  BuildingOfficeIcon,
} from '@heroicons/vue/24/outline'

const quickLinks = [
  {
    title: 'E-Magazine',
    description: 'Read our latest Namadhu Vanam magazine featuring research and updates.',
    icon: BookOpenIcon,
    href: '/magazine'
  },
  {
  title: 'Board of Directors',
  description: '"Meet the board of directors shaping the vision of the TASPEF"',
  icon: BuildingOfficeIcon,
  href: '/board'
  },
  {
    title: 'Our Members',
    description: 'Meet our distinguished professors and environmental experts.',
    icon: UserGroupIcon,
    href: '/members'
  },
];

const latestUpdates = [
  {
    title: 'New Research Publication',
    description: 'Latest findings on Western Ghats biodiversity conservation.',
    image: '/img/lu1.jpg',
    date: 'July 15, 2023'
  },
  {
    title: 'Upcoming Workshop',
    description: 'Join us for a workshop on sustainable forest management.',
    image: '/img/lu2.webp',
    date: 'July 20, 2023'
  },
  {
    title: 'Conservation Success',
    description: 'Recent achievements in local forest protection initiatives.',
    image: '/img/lu3.jpg',
    date: 'July 25, 2023'
  }
];
</script>