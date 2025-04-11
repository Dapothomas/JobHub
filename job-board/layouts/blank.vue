<template>
    <div>
        <nav id="navbar" class="p-6 flex items-center justify-between bg-white-0  fixed top-0 left-0 w-full z-50 transition duration-1000">
                <NuxtLink to="/" class="text-white font-poppins font-bold text-xl">JobHub</NuxtLink>

        </nav>

        <slot/>

        <footer class="p-6 flex flex-wrap items-center justify-between bg-gray-900">
            <p class="text-gray-300 font-poppins">Copyright (c) - Job Hub</p>

            <div class="flex mt-6 md:mt-0 items-center space-x-4">
                <NuxtLink to="/login" class="text-blue-950 font-poppins rounded-md bg-white text-md py-3 px-10 hover:text-white hover:bg-gray-950">Log In</NuxtLink>
                <NuxtLink to="/signup" class="text-white font-poppins rounded-md bg-indigo-900 text-md py-3 px-10 hover:bg-gray-950">Sign Up</NuxtLink>
            </div>
        </footer>
    </div>
</template>
  