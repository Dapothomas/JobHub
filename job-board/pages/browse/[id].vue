<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

definePageMeta({
  layout: 'onemore'
});

const route = useRoute();
const job = ref({});
const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;
const isLoading = ref(true); 

onMounted(async () => {
  try {
    const response = await axios.get(`${API_URL}/api/v1/jobapp/${route.params.id}/`); 
    job.value = response.data;
  } catch (error) {
    console.error('Error fetching job details:', error);  
  } finally {
    isLoading.value = false;
  }
});

useSeoMeta({
    title: 'Job Details',
    description: 'Job Details',
    ogTitle: 'Job Details',
    ogDescription: 'Job Details',
    ogImage: '/logo.png',
});

</script>

<template>
    <div v-if="isLoading" class="fixed inset-0 dark:bg-gray-900 bg-white flex items-center justify-center z-50">
        <div>
            <h1 class="text-gray-900 dark:text-white font-poppins font-bold text-3xl animate-throb">
                JobHub
            </h1>
        </div>
    </div>

    <div v-else class="flex flex-col md:flex-row mb-16">
        <div class="mt-32 md:mx-12 mx-6">
            <h1 class="font-poppins text-3xl font-medium">{{ job.title }}</h1>
            <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2">{{ job.company_name }}</h1>
            <div class="border border-x-0 border-t-1 py-6 mt-5 pb-20">
                <p class="font-poppins text-sm text-gray-700 font-thin mt-2">{{ job.description }}
                </p>
            </div>
        </div>
        <div class="md:mx-20 mx-7 md:w-1/3 mt-20 md:mt-32 border md:shadow-custom3 p-10 rounded-md divide-y">
            <div class="pb-5">
                <h1 class="font-poppins text-2xl font-medium">Company</h1>
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2"><span class="font-semibold">Name: </span>{{job.company_name }}</h1>
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2"><span class="font-semibold">Location: </span>{{ job.company_location }}</h1>
            </div>
            <div class="py-5">
                <h1 class="font-poppins text-2xl font-medium">Position</h1>
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2"><span class="font-semibold">Work arrangement: </span>{{ job.position_location}}</h1>
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2"><span class="font-semibold">Salary:</span> {{ job.position_salary }}</h1>
            </div>
            <div class="py-5 mb-4">
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2">{{ job.create_at_formatted }}</h1>
            </div>
            <a href="#" class="md:w-1/2 w-full px-28  py-2 mb-3 mt-2 text-white bg-blue-950 rounded-sm hover:bg-slate-950 focus:outline-none focus:ring focus:ring-indigo-300">Apply</a>
        </div>
    </div>
</template>

