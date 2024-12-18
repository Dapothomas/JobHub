<template>
    <div>
        <nav id="navbar" class="p-6 flex items-center justify-between bg-white dark:bg-gray-500 backdrop-filter dark:backdrop-blur-md backdrop-blur-md dark:bg-opacity-40 bg-opacity-40  fixed top-0 left-0 w-full z-50 transition duration-1000">
                <NuxtLink to="/" class="text-blue-950 dark:text-white font-poppins md:ml-6 ml-0 font-bold text-xl">JobHub</NuxtLink>

            <div class="flex items-center mr-6 space-x-4">
              <label class="inline-flex items-center cursor-pointer">
          <input type="checkbox" class="sr-only peer" @change="toggleDarkMode" :checked="$colorMode.value === 'dark'" />
          <div class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
          <span class="ms-3 text-sm font-medium text-gray-900 dark:text-gray-300">
            {{ $colorMode.value === 'dark' ? 'Dark Mode On' : 'Dark Mode Off' }}
          </span>
        </label>
                <NuxtLink to="/" class="text-blue-950 dark:text-white font-poppins text-l hover:text-blue-300">Home</NuxtLink>
                <NuxtLink to="/browse" class="text-blue-950 dark:text-white font-poppins text-l hover:text-blue-300">Browse</NuxtLink>
            </div>
        </nav>

        <slot/>

        <footer class="p-6 flex flex-wrap  items-center justify-between bg-gray-900">
            <p class="text-gray-300 ml-6 font-poppins">Copyright (c) - Job Hub</p>

            <div class="flex mt-6 md:mt-0 items-center mr-6 space-x-4">
                <NuxtLink to="/login" class="text-blue-950 font-poppins rounded-md bg-white text-md py-3 px-10 hover:text-white hover:bg-gray-950">Log In</NuxtLink>
                <NuxtLink to="/signup" class="text-white font-poppins rounded-md bg-indigo-900 text-md py-3 px-10 hover:bg-gray-950">Sign Up</NuxtLink>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
  methods: {
      toggleDarkMode(event) {
        this.$colorMode.preference = event.target.checked ? 'dark' : 'light';
      },
    },
  mounted() {
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
      if (window.scrollY > 0) {
        navbar.classList.add('shadow-custom2');
      } else {
        navbar.classList.remove('shadow-custom2');
      }
    });
  },
  beforeDestroy() {
    window.removeEventListener('scroll');
  }
}
</script>
