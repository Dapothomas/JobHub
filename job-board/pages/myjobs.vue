<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();
const router = useRouter();
const jobs = ref([]);
const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;
const isLoading = ref(true);

// Computed statistics
const totalJobs = computed(() => jobs.value.length);
const activeJobs = computed(() => jobs.value.filter(job => job.is_active !== false).length);
const inactiveJobs = computed(() => jobs.value.filter(job => job.is_active === false).length);
const recentJobs = computed(() => {
    const thirtyDaysAgo = new Date();
    thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);
    return jobs.value.filter(job => new Date(job.created_at) > thirtyDaysAgo).length;
});

onMounted(() => {
    console.log('MyJobs mounted');
    userStore.initStore();
    
    console.log('Auth status:', userStore.user.isAuthenticated);
    console.log('Token:', userStore.user.token);

    if (!userStore.user.isAuthenticated || !userStore.user.token) {
        console.log('Not authenticated, redirecting to login');
        return;
    }
    
    getMyJobs();
});

async function getMyJobs() {
    try {
        console.log('Fetching jobs with token:', userStore.user.token);
        const response = await axios.get(`${API_URL}/api/v1/jobapp/myjobs/`, {
            headers: {
                'Authorization': `Token ${userStore.user.token}`,
                'Content-Type': 'application/json'
            }
        });
        jobs.value = response.data;
    } catch (error) {
        console.error('Error fetching jobs:', error);
        if (error.response?.status === 401) {
            console.log('Unauthorized, clearing token');
            userStore.removeToken();
            router.push('/login');
        }
    } finally {
        isLoading.value = false;
    }
}

function deleteJob(id) {
    console.log('Deleting job with id:', id);
    jobs.value = jobs.value.filter(job => job.id !== id);
}

useSeoMeta({
    title: 'My Jobs',
    description: 'My Jobs',
    ogTitle: 'My Jobs',
    ogDescription: 'My Jobs',
    ogImage: '/logo.png',
});
</script>

<template>
    <div v-if="isLoading" class="fixed inset-0 dark:bg-gray-900 bg-white flex items-center justify-center z-50">
        <div class="text-center">
            <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
            <h1 class="text-gray-900 dark:text-white font-bold text-2xl">
                Loading Your Jobs...
            </h1>
        </div>
    </div>

    <div v-else class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-blue-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            
            <!-- Header Section -->
            <div class="mb-12">
                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                    <div>
                        <h1 class="text-4xl sm:text-5xl font-bold text-gray-900 dark:text-white mb-2">
                            My Job Dashboard
                        </h1>
                        <p class="text-xl text-gray-600 dark:text-gray-400">
                            Manage your job postings and track applications
                        </p>
                    </div>
                    
                    <!-- Quick Actions -->
                    <div class="flex flex-col sm:flex-row gap-3">
                        <NuxtLink 
                            to="/createjob"
                            class="inline-flex items-center justify-center px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
                        >
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                            </svg>
                            Post New Job
                        </NuxtLink>
                        <button class="inline-flex items-center justify-center px-6 py-3 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 font-semibold rounded-xl border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors duration-200">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2-2V7a2 2 0 012-2h2a2 2 0 002 2v2a2 2 0 002 2h6a2 2 0 002-2V7a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 00-2 2h-2a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2a2 2 0 00-2-2H9a2 2 0 00-2 2v2a2 2 0 01-2 2H3a2 2 0 01-2-2v-2a2 2 0 012-2h2a2 2 0 012-2z"></path>
                            </svg>
                            Export Data
                        </button>
                    </div>
                </div>
            </div>

            <!-- Statistics Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                
                <!-- Total Jobs -->
                <div class="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-gray-200/50 dark:border-gray-700/50 hover:shadow-xl transition-shadow duration-300">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-sm font-medium text-gray-600 dark:text-gray-400">Total Jobs</p>
                            <p class="text-3xl font-bold text-gray-900 dark:text-white">{{ totalJobs }}</p>
                        </div>
                        <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl flex items-center justify-center">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2-2v2m8 0H8m8 0v2a2 2 0 01-2 2H10a2 2 0 01-2-2V6"></path>
                            </svg>
                        </div>
                    </div>
                    <div class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                        All your job postings
                    </div>
                </div>

                <!-- Active Jobs -->
                <div class="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-gray-200/50 dark:border-gray-700/50 hover:shadow-xl transition-shadow duration-300">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-sm font-medium text-gray-600 dark:text-gray-400">Active Jobs</p>
                            <p class="text-3xl font-bold text-green-600 dark:text-green-400">{{ activeJobs }}</p>
                        </div>
                        <div class="w-12 h-12 bg-gradient-to-r from-green-500 to-green-600 rounded-xl flex items-center justify-center">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                            </svg>
                        </div>
                    </div>
                    <div class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                        Currently accepting applications
                    </div>
                </div>

                <!-- Inactive Jobs -->
                <div class="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-gray-200/50 dark:border-gray-700/50 hover:shadow-xl transition-shadow duration-300">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-sm font-medium text-gray-600 dark:text-gray-400">Inactive Jobs</p>
                            <p class="text-3xl font-bold text-gray-600 dark:text-gray-400">{{ inactiveJobs }}</p>
                        </div>
                        <div class="w-12 h-12 bg-gradient-to-r from-gray-500 to-gray-600 rounded-xl flex items-center justify-center">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                            </svg>
                        </div>
                    </div>
                    <div class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                        Closed or paused positions
                    </div>
                </div>

                <!-- Recent Jobs -->
                <div class="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-gray-200/50 dark:border-gray-700/50 hover:shadow-xl transition-shadow duration-300">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-sm font-medium text-gray-600 dark:text-gray-400">Recent (30d)</p>
                            <p class="text-3xl font-bold text-purple-600 dark:text-purple-400">{{ recentJobs }}</p>
                        </div>
                        <div class="w-12 h-12 bg-gradient-to-r from-purple-500 to-purple-600 rounded-xl flex items-center justify-center">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                            </svg>
                        </div>
                    </div>
                    <div class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                        Posted in last 30 days
                    </div>
                </div>
            </div>

            <!-- Jobs Section -->
            <div class="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-3xl shadow-xl border border-gray-200/50 dark:border-gray-700/50 p-8">
                
                <!-- Section Header -->
                <div class="flex items-center justify-between mb-8">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-500 rounded-xl flex items-center justify-center">
                            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
                            </svg>
                        </div>
                        <h2 class="text-2xl font-bold text-gray-900 dark:text-white">Your Job Listings</h2>
                    </div>
                    
                    <!-- Filter/Sort Controls -->
                    <div class="flex items-center gap-3">
                        <select class="bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500">
                            <option>All Jobs</option>
                            <option>Active Only</option>
                            <option>Inactive Only</option>
                            <option>Recent</option>
                        </select>
                        <button class="p-2 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors duration-200">
                            <svg class="w-5 h-5 text-gray-600 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"></path>
                            </svg>
                        </button>
                    </div>
                </div>

                <!-- No Jobs State -->
                <div v-if="jobs.length === 0" class="text-center py-20">
                    <div class="w-20 h-20 mx-auto mb-6 bg-gradient-to-r from-blue-100 to-purple-100 dark:from-gray-800 dark:to-gray-700 rounded-2xl flex items-center justify-center">
                        <svg class="w-10 h-10 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2-2v2m8 0H8m8 0v2a2 2 0 01-2 2H10a2 2 0 01-2-2V6"></path>
                        </svg>
                    </div>
                    <h3 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">No Jobs Posted Yet</h3>
                    <p class="text-gray-500 dark:text-gray-400 text-lg mb-8 max-w-md mx-auto">
                        Start building your talent pipeline by posting your first job opportunity.
                    </p>
                    <NuxtLink 
                        to="/createjob"
                        class="inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-2xl hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 hover:-translate-y-1 transition-all duration-300 shadow-xl"
                    >
                        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                        </svg>
                        Create Your First Job
                    </NuxtLink>
                </div>

                <!-- Jobs List -->
                <div v-else class="space-y-6">
                    <job v-for="job in jobs" 
                         :key="job.id" 
                         :job="job" 
                         :Myjobs="true" 
                         @deleteJob="deleteJob(job.id)"
                         class="transform hover:scale-[1.02] hover:-translate-y-1 transition-all duration-300"/>
                    
                    <!-- Add New Job Card -->
                    <div class="bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 border-2 border-dashed border-blue-300 dark:border-blue-700 rounded-2xl p-8 text-center hover:border-blue-400 dark:hover:border-blue-600 transition-colors duration-200">
                        <div class="w-16 h-16 mx-auto mb-4 bg-gradient-to-r from-blue-500 to-purple-500 rounded-2xl flex items-center justify-center">
                            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                            </svg>
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">Ready to hire more talent?</h3>
                        <p class="text-gray-600 dark:text-gray-400 mb-6">Post another job and continue building your team.</p>
                        <NuxtLink 
                            to="/createjob"
                            class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
                        >
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                            </svg>
                            Post Another Job
                        </NuxtLink>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>