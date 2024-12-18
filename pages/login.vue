<script setup lang="ts">
definePageMeta({
  layout: 'blank'
})
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
      <form class="mt-4">
        <div class="mb-4">
          <input 
            type="email" 
            id="email" 
            class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
            placeholder="Email"
            required
          />
        </div>
        
        <div class="mb-4">
          <input 
            type="password" 
            id="password" 
            class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
            placeholder="Password"
            required
          />
        </div>

        <div class="flex items-center justify-between mb-4">
          <label class="inline-flex items-center">
            <input type="checkbox" class="form-checkbox text-indigo-600 border-gray-300 rounded">
            <span class="ml-2 text-sm text-gray-600">Remember me</span>
          </label>
          <a href="#" class="text-sm text-indigo-600 hover:underline">Forgot Password?</a>
        </div>

        <button 
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