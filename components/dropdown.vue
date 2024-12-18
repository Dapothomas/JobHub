<template>
    <Menu as="div" class="relative w-full inline-block text-left">
      <div>
        <MenuButton class="inline-flex w-full justify-between gap-x-1.5 dark:bg-gray-800 rounded-md bg-gray-100 px-3 py-4 font-poppins text-sm font-light text-gray-400 shadow-sm  hover:bg-gray-50">
          Select a category...
          <ChevronDownIcon class="-mr-1 size-5 text-gray-400" aria-hidden="true" />
        </MenuButton>
      </div>
  
      <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
        <MenuItems class="absolute left-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 dark:bg-gray-800 ring-black/5 focus:outline-none">
          <div class="py-1">
            <MenuItem v-slot="{ active }">
              <a href="#" :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'dark:text-gray-200', 'dark:hover:text-gray-600', 'block px-4 py-2 text-sm']">Account settings</a>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <a href="#" :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'dark:text-gray-200', 'dark:hover:text-gray-600', 'block px-4 py-2 text-sm']">Support</a>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <a href="#" :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'dark:text-gray-200', 'dark:hover:text-gray-600', 'block px-4 py-2 text-sm']">License</a>
            </MenuItem>
            <form method="POST" action="#">
              <MenuItem v-slot="{ active }">
                <button type="submit" :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'dark:text-gray-200', 'dark:hover:text-gray-600', 'block w-full px-4 py-2 text-left text-sm']">Sign out</button>
              </MenuItem>
            </form>
          </div>
        </MenuItems>
      </transition>
    </Menu>
  </template>
  
  <script setup>
  import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
  import { ChevronDownIcon } from '@heroicons/vue/20/solid'
  </script>