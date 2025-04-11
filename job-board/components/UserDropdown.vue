<template>
  <div class="relative">
    <button @click="isOpen = !isOpen" class="flex items-center space-x-2 text-gray-700 dark:text-gray-200 focus:outline-none">
      <div class="w-8 h-8 rounded-full bg-indigo-600 flex items-center justify-center text-white font-semibold">
        {{ userInitial }}
      </div>
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <!-- Dropdown menu -->
    <div v-if="isOpen" 
         class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-md shadow-lg py-1 z-50">
      <!-- User Info Section -->
      <div class="px-4 py-3 border-b border-gray-200 dark:border-gray-700">
        <div class="flex items-center justify-center mb-2">
          <div class="w-10 h-10 rounded-full bg-indigo-600 flex items-center justify-center text-white font-semibold text-lg">
            {{ userInitial }}
          </div>
        </div>
        <div class="text-center">
          <p class="text-sm text-gray-700 dark:text-gray-200 font-medium truncate">
            {{ userStore.user.email }}
          </p>
        </div>
        <div v-if="userStore.user.isAuthenticated" class=" w-full px-3 mt-2 py-1 text-center flex justify-center rounded-full text-sm font-medium" 
             :class="userStore.user.userType === 'employer' ? 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200' : 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'">
          {{ userStore.user.userType === 'employer' ? 'Employer' : 'Job Seeker' }}
        </div>
      </div>
      
      <!-- Menu Items -->
      <NuxtLink to="/myjobs" 
                class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">
        My Jobs
      </NuxtLink>
      <NuxtLink to="/createjob" 
                class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">
        Create Job
      </NuxtLink>
      <button @click="logout" 
              class="block w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-gray-100 dark:hover:bg-gray-700">
        Logout
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const router = useRouter();
const isOpen = ref(false);

const userInitial = computed(() => {
  return userStore.user.email ? userStore.user.email[0].toUpperCase() : '';
});

function logout() {
  userStore.removeToken();
  router.push('/login');
  isOpen.value = false;
}

// Close dropdown when clicking outside
function handleClickOutside(event) {
  if (!event.target.closest('.relative')) {
    isOpen.value = false;
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script> 