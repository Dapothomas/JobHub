<template>
  <div class="py-2">
    <div class="p-6 rounded-md hover:bg-slate-100 dark:hover:bg-gray-800 backdrop-blur-lg bg-opacity-40 transition duration-500 cursor-pointer dark:bg-gray-900 dark:text-gray-100">
      <!-- Grid Layout -->
      <div class="grid md:grid-cols-4 gap-10 items-center">
        <!-- Job Title & Company -->
        <div>
          <h3 class="mb-2 text-xl font-poppins text-slate-800 dark:text-gray-100 font-semibold">
            {{ job.title || 'N/A' }}
          </h3>
          <p class="text-gray-600 dark:text-gray-400 font-poppins">
            {{ job.company_name || 'Company Name' }}
          </p>
        </div>

        <!-- Location -->
        <div class="md:text-center text-left">
          <h3 class="mb-2 text-lg font-poppins text-slate-800 dark:text-gray-100">
            {{ job.company_location || 'Location' }}
          </h3>
          <p class="text-gray-600 dark:text-gray-400 font-poppins">
            {{ job.position_salary || '$0 - $0' }}
          </p>
        </div>

        <!-- Posted Date -->
        <div class="md:text-center text-left">
          <h3 class="mb-2 text-lg font-poppins text-slate-800 dark:text-gray-100">
            Posted at
          </h3>
          <p class="text-gray-600 dark:text-gray-400 font-poppins">
            {{ job.created_at_formatted || 'Posted Date' }}
          </p>
        </div>

        <!-- Actions -->
        <div class="flex md:justify-center justify-left">
          <NuxtLink
            :to="'/browse/' + job.id"
            class="bg-slate-700 hover:bg-slate-800 dark:bg-slate-600 dark:hover:bg-slate-700 rounded-md py-3 px-8 text-center font-semibold text-white inline-block text-lg"
          >
            Details
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

