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
    
    <div v-else class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-blue-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
        <!-- Search Header -->
        <div class="relative py-20 sm:py-24 lg:py-28 bg-gradient-to-r from-blue-600 to-purple-600 dark:from-blue-800 dark:to-purple-800">
            <div class="absolute inset-0 bg-JobSearch bg-cover bg-center opacity-20"></div>
            <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center">
                    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-white mb-6">
                        Find Your
                        <span class="text-yellow-300">Dream Job</span>
                    </h1>
                    <p class="text-xl text-blue-100 mb-12 max-w-3xl mx-auto">
                        Discover thousands of opportunities from top companies worldwide
                    </p>

                    <!-- Search Bar -->
                    <div class="max-w-3xl mx-auto mb-8">
                        <div class="relative">
                            <div class="absolute inset-y-0 left-0 pl-4 sm:pl-6 flex items-center pointer-events-none">
                                <svg class="h-5 w-5 sm:h-6 sm:w-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                                </svg>
                            </div>
                            <input 
                                v-model="query"
                                type="search" 
                                placeholder="Search jobs, companies..."
                                class="w-full pl-12 sm:pl-14 pr-20 sm:pr-32 py-4 sm:py-6 text-base sm:text-lg bg-white/95 dark:bg-gray-800/95 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400 border-0 rounded-2xl shadow-xl focus:outline-none focus:ring-4 focus:ring-white/30 transition-all duration-300"
                                @keyup.enter="performSearch"
                            />
                            <div class="absolute inset-y-0 right-0 pr-2 sm:pr-3 flex items-center">
                                <button
                                    @click="performSearch"
                                    class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-4 sm:px-8 py-3 sm:py-4 rounded-xl text-sm sm:text-base font-semibold hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
                                >
                                    <span class="hidden sm:inline">Search</span>
                                    <svg class="w-4 h-4 sm:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Popular Searches -->
                    <div class="flex flex-col sm:flex-row items-center justify-center space-y-2 sm:space-y-0 sm:space-x-4 text-blue-100">
                        <span class="font-medium text-sm sm:text-base">Popular:</span>
                        <div class="flex flex-wrap gap-2 justify-center">
                            <button @click="handlePopularSearch('Cybersecurity Specialist')" 
                                   class="px-3 py-1.5 sm:px-4 sm:py-2 bg-white/20 hover:bg-white/30 rounded-full text-xs sm:text-sm font-medium transition-colors duration-200">
                                Cybersecurity
                            </button>
                            <button @click="handlePopularSearch('Marketing Manager')" 
                                   class="px-3 py-1.5 sm:px-4 sm:py-2 bg-white/20 hover:bg-white/30 rounded-full text-xs sm:text-sm font-medium transition-colors duration-200">
                                Marketing
                            </button>
                            <button @click="handlePopularSearch('Software Engineer')" 
                                   class="px-3 py-1.5 sm:px-4 sm:py-2 bg-white/20 hover:bg-white/30 rounded-full text-xs sm:text-sm font-medium transition-colors duration-200">
                                Software Engineer
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div class="lg:flex lg:gap-8">
                
                <!-- Sidebar - Categories (Desktop) -->
                <div class="hidden lg:block lg:w-1/4 lg:flex-shrink-0">
                    <div class="bg-white/70 dark:bg-gray-800/70 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-gray-200/50 dark:border-gray-700/50 sticky top-24">
                        <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-6 flex items-center">
                            <svg class="w-5 h-5 mr-2 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
                            </svg>
                            Filter by Category
                        </h3>
                        <div class="space-y-2">
                            <button 
                                v-for="category in jobCategories"
                                :key="category.id" 
                                @click="toggleCategory(category.id)"
                                class="w-full text-left px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200 hover:bg-blue-50 dark:hover:bg-gray-700"
                                :class="selectedCategoriesRef.includes(category.id) 
                                    ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg' 
                                    : 'text-gray-700 dark:text-gray-300'"
                            >
                                {{ category.title }} 
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Mobile Categories Filter -->
                <div class="lg:hidden mb-6">
                    <div class="bg-white/70 dark:bg-gray-800/70 backdrop-blur-sm rounded-2xl p-4 shadow-lg border border-gray-200/50 dark:border-gray-700/50">
                        <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-4">Categories</h3>
                        <div class="flex flex-wrap gap-2">
                            <button 
                                v-for="category in jobCategories"
                                :key="category.id" 
                                @click="toggleCategory(category.id)"
                                class="px-4 py-2 rounded-xl text-sm font-medium transition-all duration-200"
                                :class="selectedCategoriesRef.includes(category.id) 
                                    ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg' 
                                    : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'"
                            >
                                {{ category.title }} 
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Jobs List -->
                <div class="lg:flex-1">
                    <!-- Results Header -->
                    <div class="flex items-center justify-between mb-6">
                        <h2 class="text-2xl font-bold text-gray-900 dark:text-white">
                            {{ jobs.length }} Job{{ jobs.length !== 1 ? 's' : '' }} Found
                        </h2>
                        <div class="hidden sm:flex items-center space-x-2 text-sm text-gray-600 dark:text-gray-400">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"></path>
                            </svg>
                            <span>Sort by: Newest</span>
                        </div>
                    </div>

                    <!-- Jobs Grid -->
                    <div v-if="jobs.length === 0" class="text-center py-20">
                        <div class="w-20 h-20 mx-auto mb-6 bg-gradient-to-r from-blue-100 to-purple-100 dark:from-gray-800 dark:to-gray-700 rounded-2xl flex items-center justify-center">
                            <svg class="w-10 h-10 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2-2v2m8 0H8m8 0v2a2 2 0 01-2 2H10a2 2 0 01-2-2V6"></path>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-bold text-gray-900 dark:text-white mb-3">No jobs found</h3>
                        <p class="text-gray-500 dark:text-gray-400 text-lg">Try adjusting your search criteria or browse all categories</p>
                    </div>
                    
                    <div v-else class="space-y-6">
                        <job v-for="job in jobs"
                             :key="job.id"
                             :job="job"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
