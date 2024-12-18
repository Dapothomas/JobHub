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

  <div class="relative flex w-full md:max-w-2xl max-w-sm bg-white rounded-sm shadow-lg z-10">
    
    <div 
      class="hidden md:block md:w-1/2 w-1/2 bg-cover bg-center bg-JobImg3 "
    >
    <div class="flex gr justify-center items-center py-32 ">
        <h1 class="font-poppins text-white text-3xl pb-2 pt-32 font-semibold">JobHub</h1>
    </div>
    </div>
    <div class="w-full md:w-1/1 p-12">
      <h2 class="text-2xl font-bold text-center font-poppins text-gray-700">Sign Up</h2>
      <form class="mt-4">
        <div class="mb-4">
            <label for="name" class="block text-sm font-sm font-poppins text-gray-700">Full Name</label>
          <input 
            type="name" 
            id="fname" 
            class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
            placeholder=" "
            required
          />
        </div>
        <div class="mb-4">
            <label for="email" class="block text-sm font-sm font-poppins text-gray-700">Email</label>
          <input 
            type="email" 
            id="email" 
            class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
            placeholder=" "
            required
          />
        </div>
        <div class="mb-4">
            <label for="password" class="block text-sm font-sm font-poppins text-gray-700">Password</label>
          <input 
            type="password" 
            id="password" 
            class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
            placeholder=""
            required
          />
        </div>
        <div class="mb-4">
            <label for="password" class="block text-sm font-sm font-poppins text-gray-700">Repeat Password</label>
          <input 
            type="password" 
            id="password" 
            class="w-full px-4 py-2 mt-2 bg-gray-100 rounded-sm focus:outline-none focus:ring focus:ring-indigo-300"
            placeholder=""
            required
          />
        </div>
        <div class="md:flex md:gap-5">
            <button 
          type="submit" 
          class="md:w-1/3 w-full px-4 py-2 mb-3 mt-2 text-white bg-blue-950 rounded-sm hover:bg-slate-950 focus:outline-none focus:ring focus:ring-indigo-300"
        >
          Sign Up
        </button>
        <p class="mt-4 text-sm text-center text-gray-600">
       Already have an account? 
        <a href="/login" class="text-indigo-600 hover:underline">Login</a>
      </p>
        </div>
        
      </form>
      
    </div>

  </div>
</div>



</template>