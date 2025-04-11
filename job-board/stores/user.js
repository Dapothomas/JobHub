import { defineStore } from 'pinia'

export const useUserStore = defineStore({
    id: 'user',
    state: () => ({
        user: {
            isAuthenticated: false,
            token: null,
            email: null,
            userType: null,
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('token')) {
                this.user.token = localStorage.getItem('token')
                this.user.email = localStorage.getItem('email')
                this.user.isAuthenticated = true
                this.user.userType = localStorage.getItem('userType')
            }
        },
        setToken(token, email, userType = null) {
            this.user.token = token
            this.user.email = email
            this.user.isAuthenticated = true
            this.user.userType = userType

            localStorage.setItem('token', token)
            localStorage.setItem('email', email)
            localStorage.setItem('userType', userType)
        },
        removeToken() {
            this.user.token = null
            this.user.email = null
            this.user.isAuthenticated = false
            this.user.userType = null


            localStorage.removeItem('token')
            localStorage.removeItem('email')
            localStorage.removeItem('userType')
        }
    }
})