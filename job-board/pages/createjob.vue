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
    <div class="pt-24 px-12 pb-12 w-1/2screen  dark:bg-gray-900 text-gray-800 dark:text-gray-200 transition duration-1000">
      <div v-if="errors.length" class="mb-5 text-white bg-red-600 py-2 px-4 rounded-sm">
          <p v-for="error in errors" :key="error">
            {{ error }}
          </p>
        </div>
      <h1 class="font-poppins text-2xl font-sm text-gray-700 dark:text-gray-200">Create Jobs</h1>
      <div class="flex md:flex-row flex-col justify-between mt-5 md:gap-12 gap-5">
        <div class="flex-col w-full flex space-y-5">
          <!-- Category -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Category</label>
            <dropdown
                v-model="selectedCategory"
                :options="categories"
                placeholder="Select a category"
            />
          </div>
          <!-- Title -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Title</label>
            <input
              v-model="title"
              type="text"
              id="title"
              class="inline-flex w-full justify-between gap-x-1.5 rounded-md bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:placeholder-gray-500 px-3 py-4 font-poppins text-sm font-light text-gray-800 shadow-sm"
              placeholder="Input Title..."
              required
            />
          </div>
          <!-- Description -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Description</label>
            <input
              v-model="description"
              type="text"
              id="description"
              class="inline-flex w-full justify-between gap-x-1.5 rounded-md bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:placeholder-gray-500 px-3 py-4 font-poppins text-sm font-light text-gray-800 shadow-sm"
              placeholder="Input Description..."
              required
            />
          </div>
          <!-- Salary -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Salary</label>
            <input
              v-model="position_salary"
                  type="text"
              id="salary"
              class="inline-flex w-full justify-between gap-x-1.5 rounded-md bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:placeholder-gray-500 px-3 py-4 font-poppins text-sm font-light text-gray-800 shadow-sm"
              placeholder="Input Salary..."
              required
            />
          </div>
        </div>
        <div class="flex-col w-full flex space-y-5">
          <!-- Location -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Location</label>
            <input
              v-model="position_location"
              type="text"
              id="location"
              class="inline-flex w-full justify-between gap-x-1.5 rounded-md bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:placeholder-gray-500 px-3 py-4 font-poppins text-sm font-light text-gray-800 shadow-sm"
              placeholder="Input Location..."
              required
            />
          </div>
          <!-- Company Name -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Company Name</label>
            <input
              v-model="company_name"
              type="text"
              id="company-name"
              class="inline-flex w-full justify-between gap-x-1.5 rounded-md bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:placeholder-gray-500 px-3 py-4 font-poppins text-sm font-light text-gray-800 shadow-sm"
              placeholder="Input Company Name..."
              required
            />
          </div>
          <!-- Company Location -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Position Location</label>
            <input
              v-model="company_location"
              type="text"
              id="company-location"
              class="inline-flex w-full justify-between gap-x-1.5 rounded-md bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:placeholder-gray-500 px-3 py-4 font-poppins text-sm font-light text-gray-800 shadow-sm"
              placeholder="Input Company Location..."
              required
            />
          </div>
          <!-- Company Email -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Company Email</label>
            <input
              v-model="company_email"
              type="email"
              id="company-email"
              class="inline-flex w-full justify-between gap-x-1.5 rounded-md bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:placeholder-gray-500 px-3 py-4 font-poppins text-sm font-light text-gray-800 shadow-sm"
              placeholder="Input Company Email..."
              required
            />
          </div>
        </div>
      </div>
      <!-- Submit Button -->
      <div class="flex justify-center">
        <button 
          @click="createJob"
          class="inline-flex md:w-1/2 w-full font-poppins py-3 justify-center mb-3 mt-16 text-white bg-blue-950 dark:text-slate-100 rounded-sm hover:bg-slate-950 focus:outline-none focus:ring focus:ring-indigo-300"
        >
          Create
        </button>
      </div>
    </div>
  </template>
  