<template>
    <div class="pt-24 px-12 pb-12 w-1/2screen  dark:bg-gray-900 text-gray-800 dark:text-gray-200 transition duration-1000">
      <h1 class="font-poppins text-2xl font-sm text-gray-700 dark:text-gray-200">Create Jobs</h1>
      <div class="flex md:flex-row flex-col justify-between mt-5 md:gap-12 gap-5">
        <div class="flex-col w-full flex space-y-5">
          <!-- Category -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Category</label>
            <dropdown />
          </div>
          <!-- Title -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Title</label>
            <input
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
              type="text"
              id="company-name"
              class="inline-flex w-full justify-between gap-x-1.5 rounded-md bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:placeholder-gray-500 px-3 py-4 font-poppins text-sm font-light text-gray-800 shadow-sm"
              placeholder="Input Company Name..."
              required
            />
          </div>
          <!-- Company Location -->
          <div class="flex-col flex">
            <label class="font-poppins text-sm text-gray-500 dark:text-gray-400 mb-2 font-sm">Company Location</label>
            <input
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
        <a
          href="#"
          class="inline-flex md:w-1/2 w-full font-poppins py-3 justify-center mb-3 mt-16 text-white bg-blue-950 dark:text-slate-100 rounded-sm hover:bg-slate-950 focus:outline-none focus:ring focus:ring-indigo-300"
        >
          Create
        </a>
      </div>
    </div>
  </template>
  