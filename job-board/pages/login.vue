<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router'; 

const userStore = useUserStore();
const router = useRouter();

const email = ref('');
const password1 = ref('');
const errors = ref([]); 
const config = useRuntimeConfig();
const API_URL = config.public.apiUrl;

async function submitForm() {
    errors.value = [];
    try {
        const response = await axios.post(`${API_URL}/api/v1/token/login/`, {
            username: email.value,
            password: password1.value,
        });
        
        console.log('Login successful, token:', response.data.auth_token);
        
        // Fetch user details to get user type
        const userResponse = await axios.get(`${API_URL}/api/v1/users/me/`, {
            headers: {
                'Authorization': `Token ${response.data.auth_token}`
            }
        });
        
        userStore.setToken(response.data.auth_token, email.value, userResponse.data.user_type);
        console.log('logged in user type', userResponse.data);
        // Redirect based on user type
        if (userResponse.data.user_type === 'employer') {
            router.push('/myjobs');
        } else {
            router.push('/myjobs');
        }
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
definePageMeta({
  layout: 'blank'
})

useSeoMeta({
    title: 'Login',
    description: 'Login',
    ogTitle: 'Login',
    ogDescription: 'Login',
    ogImage: '/logo.png',
});

</script>

<template>
    
    <div class="flex items-center justify-center min-h-screen ">
        <div class="absolute inset-0 
            bg-JobImg
             bg-cover bg-center opacity-55 z-0">
        </div>
  <div class="relative flex w-full md:max-w-3xl max-w-sm bg-white rounded-sm shadow-lg z-10">
    <div class="w-full md:w-1/2 p-12">
      <h2 class="text-2xl font-bold text-center font-poppins text-gray-700">Login</h2>
      <form @submit.prevent="submitForm" class="mt-4">
        <div class="mb-4">
          <input 
            v-model="email"
            type="email" 
            id="email" 
            class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
            placeholder="Email"
            required
          />
        </div>
        
        <div class="mb-4">
          <input 
            v-model="password1"
            type="password" 
            id="password" 
            class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
            placeholder="Password"
            required
          />
        </div>
        <div v-if="errors.length" class="mb-5 text-white bg-red-600 py-2 px-4 rounded-sm">
          <p v-for="error in errors" :key="error">
            {{ error }}
          </p>
        </div>
        <div class="flex items-center justify-between mb-4">
          <label class="inline-flex items-center">
            <input type="checkbox" class="form-checkbox text-indigo-600 border-gray-300 rounded">
            <span class="ml-2 text-sm text-gray-600">Remember me</span>
          </label>
          <a href="#" class="text-sm text-indigo-600 hover:underline">Forgot Password?</a>
        </div>

        <button 
          @click="submitForm"
          type="submit" 
          class="w-full px-4 py-2 mb-3 mt-2 text-white bg-blue-950 rounded-sm hover:bg-slate-950 focus:outline-none focus:ring focus:ring-indigo-300"
        >
          Login
        </button>
      </form>
      <p class="mt-4 text-sm text-center text-gray-600">
        Don't have an account? 
        <a href="/signup" class="text-indigo-600 hover:underline">Sign up</a>
      </p>
    </div>

    <div 
      class="hidden md:block md:w-1/2 w-1/2 bg-cover bg-center bg-JobImg3 "
    >
    <div class="flex flex-col justify-center items-center py-28 px-20">
        <h1 class="font-poppins text-white text-3xl pb-2 font-semibold">JobHub</h1>
        <p class="font-sans text-center text-sm text-white font-thin">Explore endless opportunities and connect with top employers
            worldwide. Your journey to a successful
            career begins with Job Hub today!</p>
    </div>
    </div>
  </div>
</div>



</template>