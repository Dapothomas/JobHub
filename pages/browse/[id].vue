<template>
    <div class="flex flex-col md:flex-row mb-16">
        <div class="mt-32 md:mx-12 mx-6">
            <h1 class="font-poppins text-3xl font-medium">Title</h1>
            <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2">Company name</h1>
            <div class="border border-x-0 border-t-1 py-6 mt-5 pb-20">
                <p class="font-poppins text-sm text-gray-700 font-thin mt-2">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
                 tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
                 laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                  cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
                  deserunt mollit anim id est laborum.
                </p>
            </div>
        </div>
        <div class="md:mx-20 mx-7 md:w-1/2 mt-20 md:mt-32 border md:shadow-custom3 p-10 rounded-md divide-y">
            <div class="pb-5">
                <h1 class="font-poppins text-2xl font-medium">Company</h1>
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2">Company name</h1>
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2">Company location</h1>
            </div>
            <div class="py-5">
                <h1 class="font-poppins text-2xl font-medium">Position</h1>
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2">Position location</h1>
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2">Salary</h1>
            </div>
            <div class="py-5 mb-4">
                <h1 class="font-poppins text-sm text-gray-600 font-thin mt-2">Posted at July 15. 2004</h1>
            </div>
            <a href="#" class="md:w-1/2 px-28 py-2 mb-3 mt-2 text-white bg-blue-950 rounded-sm hover:bg-slate-950 focus:outline-none focus:ring focus:ring-indigo-300">Apply</a>
        </div>
    </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'onemore'
})
</script>