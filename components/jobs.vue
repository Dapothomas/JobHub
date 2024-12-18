<script setup>
const props = defineProps({
  Myjobs: {
    type: [Boolean],
  },
});
</script>

<template>
  <div class="py-2 z-1">
    <div
      class="p-6 rounded-md z-1 hover:bg-slate-100 dark:hover:bg-gray-800 backdrop-blur-lg bg-opacity-40  cursor-pointer space-y-4 md:flex md:items-center md:justify-between md:space-y-0 dark:bg-gray-900 dark:text-gray-100"
    >
      <div>
        <h3
          class="mb-2 text-xl font-poppins text-slate-800 dark:text-gray-100 font-semibold"
        >
          The Job Position
        </h3>
        <p class="text-gray-600 dark:text-gray-400 font-poppins">
          Company Name
        </p>
      </div>

      <div class="md:text-right">
        <h3
          class="mb-2 text-lg font-poppins text-slate-800 dark:text-gray-100"
        >
          Worldwide
        </h3>
        <p class="text-gray-600 dark:text-gray-400 font-poppins">
          $90k - $120k
        </p>
      </div>

      <div class="md:text-right">
        <p class="text-gray-600 dark:text-gray-400 font-poppins">
          Posted Dec. 01, 2024
        </p>
      </div>

      <div class="flex gap-5">
        <NuxtLink
          to="/browse/1"
          class="bg-slate-700 hover:bg-slate-800 dark:bg-slate-600 dark:hover:bg-slate-700 rounded-md py-3 px-8 text-center font-semibold text-white inline-block text-lg"
        >
          Details
        </NuxtLink>
        <dropdown2 v-if="Myjobs"/>
      </div>
    </div>
  </div>
</template>
