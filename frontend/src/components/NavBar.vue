<template>
  <header>
    <!-- Top bar -->
    <div class="bg-white-800 px-4">
      <div class="container mx-auto px-4 py-2">
        <div class="flex flex-col md:flex-row items-center relative">
          <!-- Logo -->
          <div class="w-1/5 flex-shrink-0">
            <img src="/public/img/taspef-logo.png" alt="TNASPEF Logo" class="h-16 w-16 md:h-20 md:w-20 object-contain mx-auto md:mx-0" />
          </div>

          <!-- Centered title -->
          <div class="text-gray text-center md:text-center">
            <h1 class="text-md md:text-xl lg:text-2xl font-bold leading-tight mt-4 md:mt-0">
              Tamil Nadu Association of Senior Professionals of Environment and Forests
            </h1>
          </div>
        </div>
      </div>
    </div>

    <!-- Navigation menu -->
    <nav class="bg-green-600 shadow-lg">
      <div class="container mx-auto px-4">
        <!-- Desktop menu -->
        <div class="hidden md:flex justify-center">
          <div class="flex space-x-1">
            <router-link
              v-for="item in navigation"
              :key="item.name"
              :to="item.href"
              class="px-4 py-3 text-white hover:bg-green-700 transition-colors duration-200 font-medium flex items-center space-x-1"
            >
              <component :is="item.icon" class="h-5 w-5" />
              <span>{{ item.name }}</span>
            </router-link>
          </div>
        </div>

        <!-- Mobile menu button -->
        <div class="md:hidden flex justify-center py-2">
          <button
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="text-white p-2 rounded-md hover:bg-green-700 focus:outline-none"
          >
            <Bars3Icon v-if="!mobileMenuOpen" class="h-6 w-6" />
            <XMarkIcon v-else class="h-6 w-6" />
          </button>
        </div>

        <!-- Mobile menu -->
        <div v-show="mobileMenuOpen" class="md:hidden">
          <div class="px-2 pt-2 pb-3 space-y-1">
            <router-link
              v-for="item in navigation"
              :key="item.name"
              :to="item.href"
              class="block px-3 py-2 text-white hover:bg-green-700 transition-colors duration-200 font-medium text-center"
              @click="mobileMenuOpen = false"
            >
              <div class="flex items-center justify-center space-x-2">
                <component :is="item.icon" class="h-5 w-5" />
                <span>{{ item.name }}</span>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { 
  Bars3Icon, 
  XMarkIcon,
  HomeIcon,
  DocumentTextIcon,
  BookOpenIcon,
  UserGroupIcon,
  FolderIcon,
  BuildingOfficeIcon,
} from '@heroicons/vue/24/outline'

const mobileMenuOpen = ref(false)

const navigation = [
  { name: 'Home', href: '/', icon: HomeIcon },
  { name: 'Board of Directors', href: '/board', icon: BuildingOfficeIcon },
  { name: 'AGM Reports', href: '/agm-reports', icon: DocumentTextIcon },
  { name: 'Namadhu Vanam E-Magazine', href: '/magazine', icon: BookOpenIcon },
  { name: 'Members', href: '/members', icon: UserGroupIcon },
]
</script>