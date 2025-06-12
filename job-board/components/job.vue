<template>
  <div class="w-full">
    <div class="bg-white/70 dark:bg-gray-800/70 backdrop-blur-sm border border-gray-200/50 dark:border-gray-700/50 rounded-2xl p-6 sm:p-8 shadow-lg hover:shadow-xl transform hover:scale-[1.02] hover:-translate-y-1 transition-all duration-300 cursor-pointer">
      
      <!-- Mobile Layout (Stack vertically) -->
      <div class="block lg:hidden space-y-4">
        <!-- Header: Title & Company -->
        <div class="space-y-2">
          <h3 class="text-xl sm:text-2xl font-bold text-gray-900 dark:text-white leading-tight">
            {{ job.title || 'Job Title' }}
          </h3>
          <div class="flex items-center space-x-2 text-gray-600 dark:text-gray-300">
            <svg class="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
            </svg>
            <span class="font-medium">{{ job.company_name || 'Company Name' }}</span>
          </div>
        </div>

        <!-- Job Details Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <!-- Location -->
          <div class="flex items-center space-x-2 text-gray-600 dark:text-gray-300">
            <svg class="w-4 h-4 text-blue-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
            </svg>
            <span class="text-sm font-medium">{{ job.company_location || 'Location' }}</span>
          </div>

          <!-- Salary -->
          <div class="flex items-center space-x-2 text-gray-600 dark:text-gray-300">
            <svg class="w-4 h-4 text-green-500 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
            </svg>
            <span class="text-sm font-medium">{{ job.position_salary || 'Salary not specified' }}</span>
          </div>
        </div>

        <!-- Posted Date -->
        <div class="flex items-center justify-between pt-4 border-t border-gray-200 dark:border-gray-700">
          <div class="flex items-center space-x-2 text-gray-500 dark:text-gray-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <span class="text-sm">{{ job.created_at_formatted || 'Posted recently' }}</span>
          </div>

          <!-- Action Buttons -->
          <div class="flex items-center space-x-3">
            <NuxtLink
              :to="'/browse/' + job.id"
              class="inline-flex items-center px-4 py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white text-sm font-semibold rounded-xl hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-md"
            >
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
              </svg>
              View Details
            </NuxtLink>
            <dropdown2 :onDelete="deleteJob" :job="job" v-if="Myjobs"/>
          </div>
        </div>
      </div>

      <!-- Desktop Layout (Horizontal) -->
      <div class="hidden lg:grid lg:grid-cols-12 lg:gap-6 lg:items-center">
        
        <!-- Job Title & Company (4 columns) -->
        <div class="col-span-4 space-y-2">
          <h3 class="text-xl xl:text-2xl font-bold text-gray-900 dark:text-white leading-tight">
            {{ job.title || 'Job Title' }}
          </h3>
          <div class="flex items-center space-x-2 text-gray-600 dark:text-gray-300">
            <svg class="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
            </svg>
            <span class="font-medium">{{ job.company_name || 'Company Name' }}</span>
          </div>
        </div>

        <!-- Location (2 columns) -->
        <div class="col-span-2 text-center">
          <div class="flex items-center justify-center space-x-2 text-gray-600 dark:text-gray-300">
            <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
            </svg>
            <span class="font-medium">{{ job.company_location || 'Location' }}</span>
          </div>
        </div>

        <!-- Salary (2 columns) -->
        <div class="col-span-2 text-center">
          <div class="flex items-center justify-center space-x-2 text-gray-600 dark:text-gray-300">
            <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
            </svg>
            <span class="font-medium">{{ job.position_salary || 'Competitive' }}</span>
          </div>
        </div>

        <!-- Posted Date (2 columns) -->
        <div class="col-span-2 text-center">
          <div class="flex items-center justify-center space-x-2 text-gray-500 dark:text-gray-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <span class="text-sm font-medium">{{ job.created_at_formatted || 'Recently' }}</span>
          </div>
        </div>

        <!-- Actions (2 columns) -->
        <div class="col-span-2 flex justify-center space-x-3">
          <NuxtLink
            :to="'/browse/' + job.id"
            class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-md"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
            </svg>
            View Details
          </NuxtLink>
          <dropdown2 :onDelete="deleteJob" :job="job" v-if="Myjobs"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const userStore = useUserStore();
const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;
const emit = defineEmits(['deleteJob']);

const props = defineProps({
  Myjobs: {
    type: Boolean,
    default: false
  },
  job: {
    type: Object,
    required: true,
    default: () => ({}) 
  }
});

async function deleteJob() {
  await axios.delete(`${API_URL}/api/v1/jobapp/${props.job.id}/delete`, {
    method: 'DELETE',
    headers: {
      'Authorization': `Token ${userStore.user.token}`,
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    console.log('Job deleted successfully:', response.data);
    emit('deleteJob');
  })
  .catch(error => {
    console.error('Error deleting job:', error);
  });
}
</script>

