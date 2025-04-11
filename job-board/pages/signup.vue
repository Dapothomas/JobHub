<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';

definePageMeta({
  layout: 'blank'
});

const router = useRouter();
const userStore = useUserStore();
const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;

const formData = ref({
  email: '',
  username: '',
  password: '',
  re_password: '',
  user_type: '',
  company_name: '',
  phone_number: ''
});
const errors = ref([]);

async function submitForm() {
  errors.value = [];
  
  if (formData.value.password !== formData.value.re_password) {
    errors.value.push('Passwords do not match');
    return;
  }

  try {
    const response = await axios.post(`${API_URL}/api/v1/users/`, {
      email: formData.value.email,
      username: formData.value.email,
      password: formData.value.password,
      re_password: formData.value.re_password,
      user_type: formData.value.user_type,
      company_name: formData.value.company_name,
      phone_number: formData.value.phone_number
    });

    console.log('Registration successful:', response.data);
    router.push('/login');
  } catch (error) {
    if (error.response) {
      for (const property in error.response.data) {
        errors.value.push(`${property}: ${error.response.data[property]}`);
      }
    } else {
      errors.value.push('An unexpected error occurred');
      console.log(JSON.stringify(error));
    }
  }
}
</script>

<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="absolute inset-0 bg-JobImg bg-cover bg-center opacity-55 z-0"></div>
    
    <div class="relative flex justify-center items-center w-full md:max-w-2xl max-w-sm bg-white rounded-sm shadow-lg z-10">
      <div class="w-full md:w-9/12 p-12">
        <h2 class="text-2xl font-bold text-center font-poppins text-gray-700">Sign Up</h2>
        
        <form @submit.prevent="submitForm" class="mt-4">
          <!-- User Type Selection -->
          <div class="mb-6">
            <label class="block text-sm font-sm font-poppins text-gray-700 mb-2">I am a:</label>
            <div class="grid grid-cols-2 gap-4">
              <button 
                type="button"
                @click="formData.user_type = 'jobseeker'"
                :class="[
                  'p-4 rounded-lg border-2 text-center transition-all duration-200',
                  formData.user_type === 'jobseeker' 
                    ? 'border-blue-600 bg-blue-50 text-blue-700' 
                    : 'border-gray-200 hover:border-gray-300'
                ]"
              >
                <div class="font-medium">Job Seeker</div>
                <div class="text-sm text-gray-500 mt-1">Looking for opportunities</div>
              </button>
              <button 
                type="button"
                @click="formData.user_type = 'employer'"
                :class="[
                  'p-4 rounded-lg border-2 text-center transition-all duration-200',
                  formData.user_type === 'employer' 
                    ? 'border-blue-600 bg-blue-50 text-blue-700' 
                    : 'border-gray-200 hover:border-gray-300'
                ]"
              >
                <div class="font-medium">Employer</div>
                <div class="text-sm text-gray-500 mt-1">Hiring talent</div>
              </button>
            </div>
          </div>

          <!-- Email -->
          <div class="flex flex-row gap-6">
          <div class="mb-4 ">
            <label class="block text-sm font-sm font-poppins text-gray-700">Email</label>
            <input 
              v-model="formData.email"
              type="email" 
              class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
              required
            />
          </div>
          <div>
              <label class="block text-sm font-sm font-poppins text-gray-700">Phone Number</label>
              <input 
                v-model="formData.phone_number"
                type="tel"
                class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
              />
            </div>
        </div>

          <!-- Password -->
          <div class="mb-4">
            <label class="block text-sm font-sm font-poppins text-gray-700">Password</label>
            <input 
              v-model="formData.password"
              type="password" 
              class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
              required
            />
          </div>

          <!-- Confirm Password -->
          <div class="mb-4">
            <label class="block text-sm font-sm font-poppins text-gray-700">Confirm Password</label>
            <input 
              v-model="formData.re_password"
              type="password" 
              class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
              required
            />
          </div>

          <!-- Employer-specific fields -->
          <div v-if="formData.user_type === 'employer'" class="space-y-4 mb-5">
              <label class="block text-sm font-sm font-poppins text-gray-700">Company Name</label>
              <input 
                v-model="formData.company_name"
                type="text"
                class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
              />
              
            
          </div>

          <!-- Error Messages -->
          <div v-if="errors.length" class="mb-5 text-white bg-red-600 py-2 px-4 rounded-sm">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

          <!-- Submit Button -->
          <button 
            type="submit"
            class="w-full px-4 py-2 mb-3 mt-2 text-white bg-blue-950 rounded-sm hover:bg-slate-950 focus:outline-none focus:ring focus:ring-indigo-300"
          >
            Sign Up
          </button>

          <p class="mt-4 text-sm text-center text-gray-600">
            Already have an account? 
            <a href="/login" class="text-indigo-600 hover:underline">Login</a>
          </p>
        </form>
      </div>

      <!-- <div class="hidden md:block md:w-1/2 bg-cover bg-center bg-JobImg3">
        <div class="flex flex-col justify-center items-center py-28 px-20">
          <h1 class="font-poppins text-white text-3xl pb-2 font-semibold">JobHub</h1>
          <p class="font-sans text-center text-sm text-white font-thin">
            Explore endless opportunities and connect with top employers worldwide. 
            Your journey to a successful career begins with Job Hub today!
          </p>
        </div>
      </div> -->
    </div>
  </div>
</template>