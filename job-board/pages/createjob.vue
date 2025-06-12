<script setup>
import { onMounted, ref } from 'vue';
import { useUserStore } from '../stores/user';
import { useRouter } from 'vue-router';
import axios from 'axios';


const userStore = useUserStore();
const router = useRouter();

const categories = ref([]);
const selectedCategory = ref('');
const title = ref('');
const description = ref('');
const position_salary = ref('');
const position_location = ref('');
const company_name = ref('');
const company_location = ref('');
const company_email = ref('');
const errors = ref([]);
const isLoading = ref(false);

const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;

onMounted(() => {
    userStore.initStore();  // Initialize the store first
    if (!userStore.user.isAuthenticated) {
        router.push('/login');
    } else {
        getCategories();  // Only fetch categories if authenticated
    }
});

// Separate function for getting categories
async function getCategories() {
    try {
        const response = await axios.get(`${API_URL}/api/v1/jobapp/categories/`, {
            headers: {
                'Authorization': `Token ${userStore.user.token}`,
                'Content-Type': 'application/json'
            }
        });
        categories.value = response.data;
    } catch (error) {
        console.error('Error fetching categories:', error);
        if (error.response?.status === 401) {
            router.push('/login');
        }
    }
}

function clearErrors() {
  setTimeout(() => {
    errors.value = [];
  }, 10000); // 10 seconds
}

async function createJob() {
  errors.value = [];
  isLoading.value = true;

  if (selectedCategory.value === '') {
    errors.value.push('Category is required');
  }
  if (title.value === '') {
    errors.value.push('Title is required');
  }
  if (description.value === '') {
    errors.value.push('Description is required');
  }
  if (position_salary.value === '') {
    errors.value.push('Salary is required');
  }
  if (position_location.value === '') {
    errors.value.push('Location is required');
  }
  if (company_name.value === '') {
    errors.value.push('Company Name is required');
  }
  if (company_location.value === '') {
    errors.value.push('Company Location is required');
  }
  if (company_email.value === '') {
    errors.value.push('Company Email is required');
  }

  if (errors.value.length > 0) {
    isLoading.value = false;
    clearErrors();  // Clear validation errors after 10s
    return;
  }

  try {
    const response = await axios.post(`${API_URL}/api/v1/jobapp/create/`, {
      category: selectedCategory.value,
      title: title.value,
      description: description.value,
      position_salary: position_salary.value,
      position_location: position_location.value,
      company_name: company_name.value,
      company_location: company_location.value,
      company_email: company_email.value,
    }, {
      headers: {
        'Authorization': `Token ${userStore.user.token}`,
        'Content-Type': 'application/json'
      }
    });
    console.log(response.data);
    router.push('/myjobs');
  } catch (error) {
    if (error.response) {
      for (const property in error.response.data) {
        errors.value.push(`${property}: ${error.response.data[property]}`);
      }
    } else {
      errors.value.push('An unexpected error occurred');
    }
    clearErrors(); 
  } finally {
    isLoading.value = false;
  }
}

useSeoMeta({
    title: 'Create Job',
    description: 'Create Job',
    ogTitle: 'Create Job',
    ogDescription: 'Create Job',
    ogImage: '/logo.png',
});

</script>

<template>
    <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-blue-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 py-8 sm:py-12">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-20">
        
        <!-- Header Section -->
        <div class="text-center mb-12">
          <div class="inline-flex items-center px-6 py-3 rounded-full bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm border border-white/20 dark:border-gray-700/50 shadow-lg mb-6">
            <div class="w-2 h-2 bg-blue-500 rounded-full mr-3"></div>
            <span class="text-gray-700 dark:text-gray-300 text-sm font-medium">Employer Dashboard</span>
          </div>
          
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 dark:text-white mb-4">
            Post a New 
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">
              Job Opening
            </span>
          </h1>
          <p class="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto">
            Attract top talent by creating a compelling job listing that showcases your company and role
          </p>
        </div>

        <!-- Error Messages -->
        <div v-if="errors.length" class="max-w-4xl mx-auto mb-8">
          <div class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-2xl p-6">
            <div class="flex items-start">
              <svg class="w-6 h-6 text-red-500 mt-0.5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"></path>
              </svg>
              <div>
                <h3 class="text-lg font-semibold text-red-800 dark:text-red-200 mb-2">Please fix the following errors:</h3>
                <ul class="space-y-1">
                  <li v-for="error in errors" :key="error" class="text-red-700 dark:text-red-300">
                    • {{ error }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- Form Container -->
        <div class="max-w-4xl mx-auto">
          <div class="bg-white/70 dark:bg-gray-800/70 backdrop-blur-sm rounded-3xl p-8 sm:p-12 shadow-xl border border-white/20 dark:border-gray-700/50">
            
            <form @submit.prevent="createJob" class="space-y-8">
              
              <!-- Job Information Section -->
              <div class="space-y-6">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6 flex items-center">
                  <div class="w-8 h-8 bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg flex items-center justify-center mr-3">
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2-2v2m8 0H8m8 0v2a2 2 0 01-2 2H10a2 2 0 01-2-2V6"></path>
                    </svg>
                  </div>
                  Job Details
                </h2>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  <!-- Category -->
                  <div class="lg:col-span-2">
                    <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                      Job Category *
                    </label>
                    <dropdown
                        v-model="selectedCategory"
                        :options="categories"
                        placeholder="Select a category"
                        class="w-full"
                    />
                  </div>

                  <!-- Title -->
                  <div class="lg:col-span-2">
                    <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                      Job Title *
                    </label>
                    <input
                      v-model="title"
                      type="text"
                      placeholder="e.g. Senior Software Engineer"
                      class="w-full px-6 py-4 text-lg dark:text-white bg-white/90 dark:bg-gray-900/90 border border-gray-200 dark:border-gray-700 rounded-2xl focus:outline-none focus:ring-4 focus:ring-blue-500/30 focus:border-blue-500 dark:focus:border-blue-400 transition-all duration-300 placeholder-gray-400 dark:placeholder-gray-500"
                      required
                    />
                  </div>

                  <!-- Description -->
                  <div class="lg:col-span-2">
                    <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                      Job Description *
                    </label>
                    <textarea
                      v-model="description"
                      rows="5"
                      placeholder="Describe the role, responsibilities, requirements, and what makes your company great..."
                      class="w-full px-6 py-4 text-lg bg-white/90 dark:text-white dark:bg-gray-900/90 border border-gray-200 dark:border-gray-700 rounded-2xl focus:outline-none focus:ring-4 focus:ring-blue-500/30 focus:border-blue-500 dark:focus:border-blue-400 transition-all duration-300 placeholder-gray-400 dark:placeholder-gray-500 resize-none"
                      required
                    ></textarea>
                  </div>

                  <!-- Salary -->
                  <div>
                    <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                      Salary Range *
                    </label>
                    <input
                      v-model="position_salary"
                      type="text"
                      placeholder="e.g. $80,000 - $120,000 per year"
                      class="w-full px-6 py-4 text-lg bg-white/90 dark:text-white dark:bg-gray-900/90 border border-gray-200 dark:border-gray-700 rounded-2xl focus:outline-none focus:ring-4 focus:ring-blue-500/30 focus:border-blue-500 dark:focus:border-blue-400 transition-all duration-300 placeholder-gray-400 dark:placeholder-gray-500"
                      required
                    />
                  </div>

                  <!-- Location -->
                  <div>
                    <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                      Job Location *
                    </label>
                    <input
                      v-model="position_location"
                      type="text"
                      placeholder="e.g. New York, NY or Remote"
                      class="w-full px-6 py-4 text-lg bg-white/90 dark:text-white dark:bg-gray-900/90 border border-gray-200 dark:border-gray-700 rounded-2xl focus:outline-none focus:ring-4 focus:ring-blue-500/30 focus:border-blue-500 dark:focus:border-blue-400 transition-all duration-300 placeholder-gray-400 dark:placeholder-gray-500"
                      required
                    />
                  </div>
                </div>
              </div>

              <!-- Company Information Section -->
              <div class="space-y-6 pt-8 border-t border-gray-200 dark:border-gray-700">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6 flex items-center">
                  <div class="w-8 h-8 bg-gradient-to-r from-purple-500 to-purple-600 rounded-lg flex items-center justify-center mr-3">
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
                    </svg>
                  </div>
                  Company Information
                </h2>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  <!-- Company Name -->
                  <div>
                    <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                      Company Name *
                    </label>
                    <input
                      v-model="company_name"
                      type="text"
                      placeholder="e.g. TechCorp Inc."
                      class="w-full px-6 py-4 text-lg dark:text-white bg-white/90 dark:bg-gray-900/90 border border-gray-200 dark:border-gray-700 rounded-2xl focus:outline-none focus:ring-4 focus:ring-blue-500/30 focus:border-blue-500 dark:focus:border-blue-400 transition-all duration-300 placeholder-gray-400 dark:placeholder-gray-500"
                      required
                    />
                  </div>

                  <!-- Company Location -->
                  <div>
                    <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                      Company Location *
                    </label>
                    <input
                      v-model="company_location"
                      type="text"
                      placeholder="e.g. San Francisco, CA"
                      class="w-full px-6 py-4 text-lg dark:text-white bg-white/90 dark:bg-gray-900/90 border border-gray-200 dark:border-gray-700 rounded-2xl focus:outline-none focus:ring-4 focus:ring-blue-500/30 focus:border-blue-500 dark:focus:border-blue-400 transition-all duration-300 placeholder-gray-400 dark:placeholder-gray-500"
                      required
                    />
                  </div>

                  <!-- Company Email -->
                  <div class="lg:col-span-2">
                    <label class="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
                      Contact Email *
                    </label>
                    <input
                      v-model="company_email"
                      type="email"
                      placeholder="e.g. jobs@techcorp.com"
                      class="w-full px-6 py-4 text-lg dark:text-white bg-white/90 dark:bg-gray-900/90 border border-gray-200 dark:border-gray-700 rounded-2xl focus:outline-none focus:ring-4 focus:ring-blue-500/30 focus:border-blue-500 dark:focus:border-blue-400 transition-all duration-300 placeholder-gray-400 dark:placeholder-gray-500"
                      required
                    />
                  </div>
                </div>
              </div>

              <!-- Submit Button -->
              <div class="flex justify-center pt-8">
                <button 
                  type="submit"
                  :disabled="isLoading"
                  class="relative inline-flex items-center justify-center px-12 py-5 text-xl font-semibold text-white bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl hover:from-blue-700 hover:to-purple-700 focus:outline-none focus:ring-4 focus:ring-blue-500/30 transform hover:scale-105 hover:-translate-y-1 transition-all duration-300 shadow-lg hover:shadow-2xl disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                >
                  <span v-if="!isLoading" class="flex items-center">
                    <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                    </svg>
                    Publish Job Opening
                  </span>
                  <span v-else class="flex items-center">
                    <svg class="animate-spin -ml-1 mr-3 h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Publishing...
                  </span>
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
</template>
  