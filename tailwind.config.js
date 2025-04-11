module.exports = {
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
      }
    }
  }
} 