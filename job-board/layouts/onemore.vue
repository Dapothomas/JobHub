<template>
  <div class="min-h-screen flex flex-col">
    <nav id="navbar" class="bg-white/90 dark:bg-gray-900/90 backdrop-blur-md border-b border-gray-200/50 dark:border-gray-700/50 fixed top-0 left-0 w-full z-50 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16 sm:h-20">
          <!-- Logo -->
          <NuxtLink to="/" class="text-2xl sm:text-3xl font-bold">
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">JobHub</span>
          </NuxtLink>

          <!-- Desktop Navigation -->
          <div class="hidden lg:flex items-center space-x-8">
            <NuxtLink to="/" class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 font-medium transition-colors duration-200">
              Home
            </NuxtLink>
            <NuxtLink to="/browse" class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 font-medium transition-colors duration-200">
              Browse Jobs
            </NuxtLink>
            
            <!-- User Role Badge -->
            <div v-if="userStore.user.isAuthenticated" class="px-3 py-1 rounded-full text-sm font-medium" 
                 :class="userStore.user.userType === 'employer' ? 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200' : 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'">
              {{ userStore.user.userType === 'employer' ? 'Employer' : 'Job Seeker' }}
            </div>

            <!-- Theme Toggle -->
            <label class="inline-flex items-center cursor-pointer">
              <input type="checkbox" class="sr-only peer" @change="toggleDarkMode" :checked="$colorMode.value === 'dark'" />
              <div class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
            </label>

            <!-- Auth Actions -->
            <template v-if="userStore.user.isAuthenticated">
              <UserDropdown />
            </template>
            <template v-else>
              <NuxtLink to="/login" class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 font-medium transition-colors duration-200">
                Sign In
              </NuxtLink>
              <NuxtLink to="/signup" class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2 rounded-xl font-semibold hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-lg">
                Sign Up
              </NuxtLink>
            </template>
          </div>

          <!-- Mobile Navigation -->
          <div class="lg:hidden flex items-center space-x-4">
            <!-- Theme Toggle (Mobile) -->
            <label class="inline-flex items-center cursor-pointer">
              <input type="checkbox" class="sr-only peer" @change="toggleDarkMode" :checked="$colorMode.value === 'dark'" />
              <div class="relative w-10 h-5 bg-gray-200 peer-focus:outline-none rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
            </label>

            <!-- Mobile Menu Button -->
            <button @click="toggleMobileMenu" class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 p-2">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
        </div>

        <!-- Mobile Menu -->
        <div v-if="mobileMenuOpen" class="lg:hidden border-t border-gray-200 dark:border-gray-700 py-4">
          <div class="space-y-4">
            <NuxtLink to="/" @click="closeMobileMenu" class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 font-medium py-2">
              Home
            </NuxtLink>
            <NuxtLink to="/browse" @click="closeMobileMenu" class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 font-medium py-2">
              Browse Jobs
            </NuxtLink>
            
            <!-- User Role Badge (Mobile) -->
            <div v-if="userStore.user.isAuthenticated" class="inline-block px-3 py-1 rounded-full text-sm font-medium" 
                 :class="userStore.user.userType === 'employer' ? 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200' : 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'">
              {{ userStore.user.userType === 'employer' ? 'Employer' : 'Job Seeker' }}
            </div>

            <!-- Auth Actions (Mobile) -->
            <template v-if="userStore.user.isAuthenticated">
              <div class="border-t border-gray-200 dark:border-gray-700 pt-4 space-y-2">
                <NuxtLink v-if="userStore.user.userType === 'employer'" to="/myjobs" @click="closeMobileMenu" class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 font-medium py-2">
                  My Jobs
                </NuxtLink>
                <NuxtLink v-if="userStore.user.userType === 'employer'" to="/createjob" @click="closeMobileMenu" class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 font-medium py-2">
                  Post a Job
                </NuxtLink>
                <button @click="logout" class="block w-full text-left text-red-600 dark:text-red-400 font-medium py-2">
                  Sign Out
                </button>
              </div>
            </template>
            <template v-else>
              <div class="border-t border-gray-200 dark:border-gray-700 pt-4 space-y-4">
                <NuxtLink to="/login" @click="closeMobileMenu" class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 font-medium py-2">
                  Sign In
                </NuxtLink>
                <NuxtLink to="/signup" @click="closeMobileMenu" class="block bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-3 rounded-xl font-semibold text-center">
                  Sign Up
                </NuxtLink>
              </div>
            </template>
          </div>
        </div>
      </div>
    </nav>

    <main class="flex-grow pt-16 sm:pt-20">
      <slot />
    </main>
    
    <footer class="bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 text-white py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Main Footer Content -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
          
          <!-- Brand Section -->
          <div class="md:col-span-1">
            <div class="text-3xl font-bold mb-4">
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">JobHub</span>
            </div>
            <p class="text-gray-400 mb-6 leading-relaxed">
              Connecting talented professionals with innovative companies worldwide. Your career journey starts here.
            </p>
            <!-- Social Links -->
            <div class="flex space-x-4">
              <a href="#" class="w-10 h-10 bg-gray-800 hover:bg-blue-600 rounded-full flex items-center justify-center transition-colors duration-200">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
                </svg>
              </a>
              <a href="#" class="w-10 h-10 bg-gray-800 hover:bg-blue-600 rounded-full flex items-center justify-center transition-colors duration-200">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
              </a>
              <a href="#" class="w-10 h-10 bg-gray-800 hover:bg-blue-600 rounded-full flex items-center justify-center transition-colors duration-200">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.174-.105-.949-.199-2.403.041-3.439.219-.937 1.406-5.957 1.406-5.957s-.359-.72-.359-1.781c0-1.663.967-2.911 2.168-2.911 1.024 0 1.518.769 1.518 1.688 0 1.029-.653 2.567-.992 3.992-.285 1.193.6 2.165 1.775 2.165 2.128 0 3.768-2.245 3.768-5.487 0-2.861-2.063-4.869-5.008-4.869-3.41 0-5.409 2.562-5.409 5.199 0 1.033.394 2.143.889 2.741.097.118.112.222.082.343-.09.375-.293 1.199-.334 1.363-.053.225-.172.271-.402.165-1.495-.69-2.433-2.878-2.433-4.646 0-3.776 2.748-7.252 7.92-7.252 4.158 0 7.392 2.967 7.392 6.923 0 4.135-2.607 7.462-6.233 7.462-1.214 0-2.357-.629-2.74-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24.009 12.017 24c6.624 0 11.99-5.367 11.99-11.988C24.007 5.367 18.641.001 12.017.001z"/>
                </svg>
              </a>
            </div>
          </div>

          <!-- Quick Links -->
          <div>
            <h3 class="text-lg font-semibold mb-6">Quick Links</h3>
            <ul class="space-y-3">
              <li><NuxtLink to="/" class="text-gray-400 hover:text-white transition-colors duration-200">Home</NuxtLink></li>
              <li><NuxtLink to="/browse" class="text-gray-400 hover:text-white transition-colors duration-200">Browse Jobs</NuxtLink></li>
              <li><NuxtLink to="/about" class="text-gray-400 hover:text-white transition-colors duration-200">About Us</NuxtLink></li>
              <li><NuxtLink to="/contact" class="text-gray-400 hover:text-white transition-colors duration-200">Contact</NuxtLink></li>
            </ul>
          </div>

          <!-- For Job Seekers -->
          <div>
            <h3 class="text-lg font-semibold mb-6">For Job Seekers</h3>
            <ul class="space-y-3">
              <li><NuxtLink to="/browse" class="text-gray-400 hover:text-white transition-colors duration-200">Search Jobs</NuxtLink></li>
              <li><NuxtLink to="/login" class="text-gray-400 hover:text-white transition-colors duration-200">Sign In</NuxtLink></li>
              <li><NuxtLink to="/signup" class="text-gray-400 hover:text-white transition-colors duration-200">Create Account</NuxtLink></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors duration-200">Career Tips (Coming Soon)</a></li>
            </ul>
          </div>

          <!-- For Employers -->
          <div>
            <h3 class="text-lg font-semibold mb-6">For Employers</h3>
            <ul class="space-y-3">
              <li><NuxtLink to="/createjob" class="text-gray-400 hover:text-white transition-colors duration-200">Post a Job</NuxtLink></li>
              <li><NuxtLink to="/myjobs" class="text-gray-400 hover:text-white transition-colors duration-200">Manage Jobs</NuxtLink></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors duration-200">Hiring Solutions (Coming Soon)</a></li>
            </ul>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="border-t border-gray-700 pt-8 mb-8">
          <div class="flex flex-col sm:flex-row items-center justify-center space-y-4 sm:space-y-0 sm:space-x-6">
            <template v-if="userStore.user.isAuthenticated">
              <NuxtLink to="/myjobs" class="bg-white text-gray-900 px-8 py-3 rounded-xl font-semibold hover:bg-gray-100 transform hover:scale-105 transition-all duration-200 shadow-lg">
                My Dashboard
              </NuxtLink>
              <NuxtLink to="/createjob" class="bg-gradient-to-r from-blue-600 to-purple-600 px-8 py-3 rounded-xl font-semibold hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-lg">
                Post a Job
              </NuxtLink>
            </template>
            <template v-else>
              <NuxtLink to="/browse" class="bg-white text-gray-900 px-8 py-3 rounded-xl font-semibold hover:bg-gray-100 transform hover:scale-105 transition-all duration-200 shadow-lg">
                Find Jobs
              </NuxtLink>
              <NuxtLink to="/signup" class="bg-gradient-to-r from-blue-600 to-purple-600 px-8 py-3 rounded-xl font-semibold hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-lg">
                Get Started
              </NuxtLink>
            </template>
          </div>
        </div>
        
        <!-- Bottom Footer -->
        <div class="border-t border-gray-700 pt-8 flex flex-col md:flex-row items-center justify-between">
          <div class="flex flex-wrap items-center justify-center md:justify-start space-x-6 mb-4 md:mb-0">
            <a href="#" class="text-gray-400 hover:text-white text-sm transition-colors duration-200">Privacy Policy</a>
            <a href="#" class="text-gray-400 hover:text-white text-sm transition-colors duration-200">Terms of Service</a>
            <a href="#" class="text-gray-400 hover:text-white text-sm transition-colors duration-200">Cookie Policy</a>
          </div>
          <p class="text-gray-400 text-sm text-center md:text-right">
            © 2025 JobHub. All rights reserved. Designed by <span class="text-white">Dapo-Thomas</span> 
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useUserStore } from '@/stores/user';
import { useThemeStore } from '@/stores/theme';
import UserDropdown from '@/components/UserDropdown.vue';

const userStore = useUserStore();
const themeStore = useThemeStore();
const colorMode = useColorMode(); 
const mobileMenuOpen = ref(false);

onMounted(() => {
  userStore.initStore();
  themeStore.initTheme();
  colorMode.value = themeStore.darkMode ? 'dark' : 'light';

  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
      navbar.classList.add('shadow-lg');
    } else {
      navbar.classList.remove('shadow-lg');
    }
  });
});

function logout() {
  userStore.removeToken();
  mobileMenuOpen.value = false;
}

function toggleDarkMode(event) {
  themeStore.setDarkMode(event.target.checked);
}

function toggleMobileMenu() {
  mobileMenuOpen.value = !mobileMenuOpen.value;
}

function closeMobileMenu() {
  mobileMenuOpen.value = false;
}
</script>
