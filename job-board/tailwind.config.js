/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    './components/**/*.{vue,js}',
     './layouts/**/*.vue',
     './pages/**/*.vue',
     './plugins/**/*.{js,ts}',
     './nuxt.config.{js,ts}',
    //  './app.vue',
    ],
  theme: {
    extend: {
      keyframes: {
        throb: {
          '0%, 100%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.2)' },
        }
      },
      animation: {
        throb: 'throb 2s ease-in-out infinite',
      },
      backgroundImage: {
        JobImg: "url('/assets/Images/image.webp')",
        JobImg2: "url('/assets/Images/Job2.png')",
        JobImg3: "url('/assets/Images/Job.png')",
        JobSearch: "url('/assets/Images/JobSearch.webp')"
       },
       fontFamily: {
        poppins: ["Poppins", "sans-serif"],
      },
      boxShadow: {
        custom1: 'rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px',
        custom2: 'rgba(0, 0, 0, 0.05) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px;',
        custom3: 'rgba(0, 0, 0, 0.35) 0px 5px 15px;'
      },
    },
  },
  plugins: [],
}

