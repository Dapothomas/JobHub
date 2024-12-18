<template>
    <div class="dark:bg-gray-900 dark:text-gray-100 transition duration-1000">
      <!-- Hero Section -->
      <div class="relative py-72 bg-white dark:bg-gray-800">
        <div
          class="absolute inset-0 bg-JobImg2 transition duration-1000 dark:bg-JobImg3 bg-cover bg-center opacity-95 z-0"
        ></div>
        <div
          class="relative z-10 px-16 mt-[-40px] text-gray-900 dark:text-gray-100 flex w-full md:w-1/2 items-left justify-left h-full"
        >
          <div>
            <h1 class="text-gray-900 dark:text-gray-100 text-xl md:text-2xl font-poppins font-normal">
              Welcome to Job Hub!
            </h1>
            <p
              class="text-blue-950 dark:text-gray-300 text-3xl pb-2 pt-2 md:text-5xl font-semibold font-poppins"
            >
              Find a Job Anywhere
            </p>
            <p
              class="text-gray-800 dark:text-gray-400 text-sm pb-12 pt-2 md:text-md font-light font-poppins"
            >
              Explore endless opportunities and connect with top employers <br />
              worldwide. Your journey to a successful <br />
              career begins with Job Hub today!
            </p>
  
            <div class="flex justify-left gap-4 items-left">
              <NuxtLink
                to="/browse"
                class="bg-blue-950 dark:bg-white dark:text-blue-950 hover:bg-slate-900 dark:hover:bg-blue-950 dark:hover:text-white rounded-sm py-3 font-poppins justify-left font-bold px-8 text-white inline-block text-md"
              >
                Browse
              </NuxtLink>
              <NuxtLink
                to="/login"
                class="bg-white dark:bg-gray-700 border border-blue-950  hover:bg-slate-900 dark:hover:bg-blue-700 hover:text-white dark:hover:text-gray-200 rounded-sm py-3 font-poppins justify-left font-bold px-8 text-blue-950 dark:text-gray-100 inline-block text-md"
              >
                Log in
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Jobs Section -->
      <div class="py-16 px-6 mx-2 md:mx-10 dark:bg-gray-900 dark:text-gray-100">
        <h1
          class="font-poppins text-3xl text-center text-slate-800 dark:text-gray-200 pb-10"
        >
          Latest Jobs
        </h1>
        <div class="w-full divide-y dark:divide-gray-700">
          <jobs />
          <jobs />
          <jobs />
        </div>
      </div>
    </div>
  </template>
  