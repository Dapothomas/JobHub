<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();
const router = useRouter();
const jobs = ref([]);
const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;

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
    <div class="pt-28 pb-10 px-12 min-h-screen bg-white dark:bg-gray-900 transition duration-1000">
        <h1 class="font-poppins text-2xl text-gray-700 dark:text-gray-200 font-sm">My Jobs</h1>
        
        <!-- No Jobs Message -->
        <div v-if="jobs.length === 0" class="flex flex-col items-center justify-center min-h-[50vh]">
            <p class="text-xl text-gray-600 dark:text-gray-400 font-poppins">
                You have no jobs yet
            </p>
            <NuxtLink 
                to="/createjob"
                class="mt-4 px-6 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition-colors font-poppins"
            >
                Create Your First Job
            </NuxtLink>
        </div>

        <!-- Jobs List -->
        <div v-else class="w-full divide-y pt-5 pb-12">
            <job v-for="job in jobs" :key="job.id" :job="job" :Myjobs="true" @deleteJob="deleteJob(job.id)"/>
            <NuxtLink 
                to="/createjob"
                class="mt-6 ml-5 px-6 py-2 bg-gray-700 text-white rounded-md hover:bg-indigo-700 transition-colors font-poppins"
            >
                Add New Job +
            </NuxtLink>
        </div> 
    </div>
</template>