<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

definePageMeta({
  layout: 'onemore'
})

const jobCategories = ref([]);
const jobs = ref([]);
const selectedCategoriesRef = ref('');
const selectedCategories = []
const queryRef = ref('');
const query = ref('');
const router = useRouter();
const isLoading = ref(true);

const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;

console.log('Runtime config:', config.public);
console.log('API URL:', config.public.apiUrl);

function performSearch() {
    queryRef.value = query.value;
    console.log('searched')
    fetchJobs();
}
async function fetchJobs() {
    try {
        const jobsResponse = await axios.get(`${API_URL}/api/v1/jobapp/browsejobs/?categories=${selectedCategoriesRef.value}&query=${queryRef.value}`);
        jobs.value = jobsResponse.data;
    } catch (error) {
        console.error('Error fetching jobs:', error);
    }

function toggleCategory(id){
    const index = selectedCategories.indexOf(id)
    if(index === -1){
        selectedCategories.push(id)
    } else {
        selectedCategories.splice(index, 1)
    }

    selectedCategoriesRef.value = selectedCategories.join(',')
    fetchJobs()
}

async function handlePopularSearch(searchTerm) {
    try {
        const response = await axios.get(`${API_URL}/api/v1/jobapp/browsejobs/?query=${searchTerm}`);
        if (response.data && response.data.length > 0) {
            // Navigate to the first matching job's detail page
            router.push(`/browse/${response.data[0].id}`);
        }
    } catch (error) {
        console.error('Error fetching jobs:', error);
    }
}

onMounted(async () => {
    try {
        const categoriesResponse = await axios.get(`${API_URL}/api/v1/jobapp/categories/`);
        jobCategories.value = categoriesResponse.data;
        await fetchJobs();
    } catch (error) {
        console.error('Error fetching data:', error);
    } finally {
        isLoading.value = false;
    }
});

useSeoMeta({
    title: 'Browse Jobs',
    description: 'Browse Jobs',
    ogTitle: 'Browse Jobs',
    ogDescription: 'Browse Jobs',
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
    
    <div v-else class="dark:bg-gray-900">
        <div class="relative py-16  mt-16 bg-blue-950">
        <div class="absolute inset-0 
            bg-JobSearch
            bg-cover bg-center opacity-70 z-0">
        </div>
        <div class="relative z-10 text-white flex 
            items-center justify-center h-full">
            <div>
                    <div class="relative w-full justify-center flex">
                        <input 
                            v-model="query"
                            type="search" 
                            id="fname" 
                            class="w-full px-32 md:px-12 py-3 mt-2 text-black shadow-custom3 bg-gray-0 rounded-3xl focus:outline-none focus:ring focus:ring-indigo-300 pl-12"
                            placeholder="Find a Job..."
                            required
                        />
                        <button
                        v-on:click="performSearch"
                        class="absolute right-0 px-10 py-6 mt-2 hover:text-white transition duration-500 rounded-r-3xl  hover:bg-slate-950">
                            <svg 
                            xmlns="http://www.w3.org/2000/svg" 
                            fill="none" 
                            viewBox="0 0 24 24" 
                            stroke-width="1.5" 
                            stroke="currentColor" 
                            class="absolute flex justify-center w-full items-center right-1 top-1/2 transform -translate-y-1/2 size-7 hover:text-white text-gray-500">
                            <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                        </svg>
                        </button>
                    </div>
                    <div class="hidden md:flex mt-5">
                        <h3 class="text-white font-poppins mr-6">Popular Searches: </h3>
                        <div class="flex flex-cols-3 divide-x">
                            <a @click.prevent="handlePopularSearch('Cybersecurity Specialist')" 
                               class="hover:underline px-2 text-white font-poppins cursor-pointer">
                               Cybersecurity Specialist
                            </a>
                            <a @click.prevent="handlePopularSearch('Marketing Manager')" 
                               class="hover:underline px-2 text-white font-poppins cursor-pointer">
                               Marketing Manager
                            </a>
                            <a @click.prevent="handlePopularSearch('Software Engineer')" 
                               class="hover:underline px-2 text-white font-poppins cursor-pointer">
                               Software Engineer
                            </a>
                        </div>
                    </div>
            </div>
        </div>
    </div>
    <div class=" mx-5 md:mx-16 py-12 md:flex">
        <div class="mt-3 w-1/5 hidden md:block">
            <h3 class="text-gray-500 dark:text-gray-50 text-sm font-poppins font-light pt-5">
                Categories
            </h3>
            <div class="mt-6 space-y-4">
                <p 
                v-for="category in jobCategories"
                :key="category.id" 
                v-on:click="toggleCategory(category.id)"
                class="text-gray-800 dark:text-gray-100 font-poppins text-sm cursor-pointer font-light px-3 rounded-md py-4"
                v-bind:class="{'dark:text-gray-100 text-gray-900 underline underline-offset-4 ': selectedCategoriesRef.includes(category.id)}">
                {{ category.title }} 
                </p>
            </div>
        </div> 
        <div class="w-full divide-y">
            <job 
            v-for="job in jobs"
            :key="job.id"
            :job="job"/>
        </div> 
    </div>
    </div>
</template>
