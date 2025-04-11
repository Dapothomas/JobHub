<script setup>
import { useUserStore } from '@/stores/user'
import { useThemeStore } from '@/stores/theme'
import { onMounted, watch } from 'vue'

const userStore = useUserStore()
const themeStore = useThemeStore()
const colorMode = useColorMode()

// Initialize on client side only
if (process.client) {
  userStore.initStore()
  themeStore.initTheme()
  colorMode.preference = themeStore.darkMode ? 'dark' : 'light'
}

// Watch for theme changes
watch(() => themeStore.darkMode, (newValue) => {
  colorMode.preference = newValue ? 'dark' : 'light'
}, { immediate: true })

onMounted(() => {
  themeStore.initTheme()
})
</script>

<template>
  <div>
    <NuxtLayout>
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </Head>
      <NuxtPage/>
    </NuxtLayout>
  </div>
</template>
