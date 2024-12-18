<template>
    <div class="dark:bg-gray-900">
        <div class="relative py-16  mt-16 bg-blue-950">
        <div class="absolute inset-0 
            bg-JobSearch
            bg-cover bg-center opacity-70 z-0">
        </div>
        <div class="relative z-10 text-white flex 
            items-center justify-center h-full">
            <div>
                    <div class="relative w-full justify-center flex">
                        <input 
                            type="search" 
                            id="fname" 
                            class="w-full px-32 md:px-12 py-3 mt-2 text-black shadow-custom3 bg-gray-0 rounded-3xl focus:outline-none focus:ring focus:ring-indigo-300 pl-12"
                            placeholder="Find a Job..."
                            required
                        />
                        <button class="absolute right-0 px-10 py-6 mt-2 hover:text-white transition duration-500 rounded-r-3xl  hover:bg-slate-950">
                            <svg 
                            xmlns="http://www.w3.org/2000/svg" 
                            fill="none" 
                            viewBox="0 0 24 24" 
                            stroke-width="1.5" 
                            stroke="currentColor" 
                            class="absolute flex justify-center w-full items-center right-1 top-1/2 transform -translate-y-1/2 size-7 hover:text-white text-gray-500">
                            <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                        </svg>
                        </button>
                    </div>
                    <div class="hidden md:flex mt-5">
                        <h3 class="text-white font-poppins mr-6">Popular Searches: </h3>
                        <div class="flex flex-cols-3 divide-x">
                            <a href="" class="hover:underline px-2 text-white font-poppins">Software Developers</a>
                            <a href="" class="hover:underline px-2 text-white font-poppins">Graphic Designers</a>
                            <a href="" class="hover:underline px-2 text-white font-poppins">Video Editors</a>
                        </div>
                    </div>
            </div>
        </div>
    </div>
    <div class=" mx-5 md:mx-16 py-12 md:flex">
        <div class="mt-3 w-1/5 hidden md:block">
            <h3 class="text-gray-500 dark:text-gray-50 text-sm font-poppins font-light pt-5">
                Categories
            </h3>
            <div class="mt-6 space-y-4">
                <p class="text-gray-800 dark:text-gray-100 font-poppins text-sm font-light pt-5">Category 1</p>
                <p class="text-gray-800 dark:text-gray-100 font-poppins text-sm font-light pt-5">Category 1</p>
                <p class="text-gray-800 dark:text-gray-100 font-poppins text-sm font-light pt-5">Category 1</p>
            </div>
        </div> 
        <div class="w-full divide-y">
            <jobs/>
            <jobs/>
            <jobs/>
        </div> 
    </div>
    </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'onemore'
})
</script>