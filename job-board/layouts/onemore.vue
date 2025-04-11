<template>
  <div class="min-h-screen flex flex-col">
    <nav id="navbar" class="p-6 flex items-center justify-between bg-white dark:bg-gray-900 fixed top-0 left-0 w-full z-50 transition duration-1000">
      <NuxtLink to="/" class="text-blue-950 dark:text-white font-poppins md:ml-6 ml-0 font-bold text-xl">JobHub</NuxtLink>
      <div class="flex items-center mr-6 space-x-4">
        <label class="inline-flex items-center cursor-pointer">
          <input type="checkbox" class="sr-only peer" @change="toggleDarkMode" :checked="$colorMode.value === 'dark'" />
          <div class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
          <!-- <span class="ms-3 text-sm font-medium text-gray-900 dark:text-gray-300">
            {{ $colorMode.value === 'dark' ? 'Dark Mode On' : 'Dark Mode Off' }}
          </span> -->
        </label>
        <NuxtLink to="/" class="text-blue-950 dark:text-white font-poppins text-l hover:text-blue-300">Home</NuxtLink>
        <NuxtLink to="/browse" class="text-blue-950 dark:text-white font-poppins text-l hover:text-blue-300">Browse</NuxtLink>
        <template v-if="userStore.user.isAuthenticated">
          <UserDropdown />
        </template>
        <template v-else>
          <NuxtLink to="/login" class="text-blue-950 dark:text-white font-poppins text-l hover:text-blue-300">Login</NuxtLink>
        </template>
      </div>
    </nav>
    <main class="flex-grow">
      <slot />
    </main>
    <footer class="p-6 flex flex-wrap items-center justify-between bg-gray-900 mt-auto">
      <p class="text-gray-300 ml-6 font-poppins">Copyright (c) - Job Hub</p>
      <template v-if="userStore.user.isAuthenticated">
        <div class="flex mt-6 md:mt-0 items-center mr-6 space-x-4">
          <NuxtLink to="/myjobs" class="text-blue-950 font-poppins rounded-md bg-white text-md py-3 px-10 hover:text-white hover:bg-gray-950">My Jobs</NuxtLink>
          <NuxtLink to="/createjob" class="text-white font-poppins rounded-md bg-indigo-900 text-md py-3 px-10 hover:bg-gray-950">Create Jobs</NuxtLink>
          <a v-on:click="logout" class="text-white font-poppins rounded-md bg-red-500 text-md py-3 px-10 hover:bg-gray-950">Log Out</a>
        </div>
      </template>
      <template v-else>
        <div class="flex mt-6 md:mt-0 items-center mr-6 space-x-4">
          <NuxtLink to="/login" class="text-blue-950 font-poppins rounded-md bg-white text-md py-3 px-10 hover:text-white hover:bg-gray-950">Log In</NuxtLink>
          <NuxtLink to="/signup" class="text-white font-poppins rounded-md bg-indigo-900 text-md py-3 px-10 hover:bg-gray-950">Sign Up</NuxtLink>
        </div>
      </template>
    </footer>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useUserStore } from '@/stores/user';
import { useThemeStore } from '@/stores/theme';

const userStore = useUserStore();
const themeStore = useThemeStore();
const colorMode = useColorMode(); 

onMounted(() => {
  userStore.initStore();
  themeStore.initTheme();
  colorMode.value = themeStore.darkMode ? 'dark' : 'light';

  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
      navbar.classList.add('shadow-custom2');
    } else {
      navbar.classList.remove('shadow-custom2');
    }
  });
});

function logout() {
  userStore.removeToken();
}

function toggleDarkMode(event) {
  const isDark = event.target.checked;
  colorMode.value = isDark ? 'dark' : 'light';
  themeStore.setDarkMode(isDark);
}
</script>
