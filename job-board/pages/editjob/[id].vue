<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const router = useRouter();
const route = useRoute();
const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;
const userStore = useUserStore();
const formData = ref({});

onMounted(async () => {
  if (!userStore.user.isAuthenticated) {
    router.push('/login');
    return;
  }
  
  try {
    const response = await axios.get(`${API_URL}/api/v1/jobapp/${route.params.id}/`, {
      headers: {
        'Authorization': `Token ${userStore.user.token}`
      }
    });
    formData.value = response.data;
  } catch (error) {
    console.error('Error fetching job:', error);
  }
});

async function handleSubmit() {
  try {
    await axios.put(`${API_URL}/api/v1/jobapp/${route.params.id}/edit/`, formData.value, {
      headers: {
        'Authorization': `Token ${userStore.user.token}`,
        'Content-Type': 'application/json'
      }
    });
    router.push('/myjobs');
  } catch (error) {
    console.error('Error updating job:', error);
  }
}

useSeoMeta({
    title: 'Edit Job',
    description: 'Edit Job',
    ogTitle: 'Edit Job',
    ogDescription: 'Edit Job',
    ogImage: '/logo.png',
});

</script>

<template>
  <div class="pt-28 pb-10 px-12 min-h-screen bg-white dark:bg-gray-900">
    <h1 class="font-poppins text-2xl text-gray-700 dark:text-gray-200 font-sm mb-8">Edit Job</h1>
    
    <form @submit.prevent="handleSubmit" class="max-w-3xl">
      <!-- Title -->
      <div class="mb-6">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Job Title</label>
        <input 
          v-model="formData.title" 
          type="text" 
          class="w-full p-3 border rounded dark:bg-gray-800 dark:text-white dark:border-gray-600"
        />
      </div>

      <!-- Description -->
      <div class="mb-6">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Description</label>
        <textarea 
          v-model="formData.description" 
          rows="6"
          class="w-full p-3 border rounded dark:bg-gray-800 dark:text-white dark:border-gray-600"
        ></textarea>
      </div>

      <!-- Position Info -->
      <div class="grid md:grid-cols-2 gap-6 mb-6">
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Position Salary</label>
          <input 
            v-model="formData.position_salary" 
            type="text"
            class="w-full p-3 border rounded dark:bg-gray-800 dark:text-white dark:border-gray-600"
          />
        </div>
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Position Location</label>
          <input 
            v-model="formData.position_location" 
            type="text"
            class="w-full p-3 border rounded dark:bg-gray-800 dark:text-white dark:border-gray-600"
          />
        </div>
      </div>

      <!-- Company Info -->
      <div class="grid md:grid-cols-2 gap-6 mb-8">
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Company Name</label>
          <input 
            v-model="formData.company_name" 
            type="text"
            class="w-full p-3 border rounded dark:bg-gray-800 dark:text-white dark:border-gray-600"
          />
        </div>
        <div>
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Company Location</label>
          <input 
            v-model="formData.company_location" 
            type="text"
            class="w-full p-3 border rounded dark:bg-gray-800 dark:text-white dark:border-gray-600"
          />
        </div>
      </div>

      <button 
        type="submit"
        class="bg-indigo-600 text-white px-8 py-3 rounded hover:bg-indigo-700 transition-colors"
      >
        Update Job
      </button>
    </form>
  </div>
</template>