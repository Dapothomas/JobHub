<template>
    <Menu as="div" class="relative w-10 flex justify-center text-center z-12">
      <div>
        <MenuButton class="flex justify-center mt-3" >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />
</svg>

        </MenuButton>
      </div>
  
      <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
        <MenuItems class="absolute right-6 top-[-10px] z-20 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 dark:bg-gray-700 backdrop-filter dark:bg-opacity-50 dark:backdrop-blur-md ring-black/5 focus:outline-none">
          <div class="py-1">
            <MenuItem v-slot="{ active }">
              <a 
               
                @click="router.push(`/editjob/${props.job.id}`)"
                :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'dark:text-gray-200', 'dark:hover:bg-gray-700', 'dark:hover:text-gray-200', 'block px-4 py-2 text-sm']"
              >
                Edit
              </a>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <a href="#" @click="onDelete" :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'dark:text-gray-200', 'dark:hover:bg-gray-700', 'dark:hover:text-gray-200', 'block px-4 py-2 text-sm']">Delete</a>
            </MenuItem>
          </div>
        </MenuItems>
      </transition>
    </Menu>
  </template>
  
  <script setup>
  import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const props = defineProps({
    onDelete: Function,
    job: {
      type: Object,
      required: true,
      default: () => ({})
    }
  })
  </script>