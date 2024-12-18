import { defineStore } from "pinia";

export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            isAuthenticated: false,
            email: null,
            token: null
        }
    })
})