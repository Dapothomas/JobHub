import { defineStore } from 'pinia'

export const useThemeStore = defineStore({
    id: 'theme',
    state: () => ({
        darkMode: false
    }),
    actions: {
        initTheme() {
            const savedMode = localStorage.getItem('darkMode')
            if (savedMode !== null) {
                this.darkMode = savedMode === 'true'
                document.documentElement.classList.toggle('dark', this.darkMode)
            }
        },
        setDarkMode(isDark) {
            this.darkMode = isDark
            localStorage.setItem('darkMode', isDark)
            document.documentElement.classList.toggle('dark', isDark)
        }
    }
}) 