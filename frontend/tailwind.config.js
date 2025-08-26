module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Montserrat", "Arial", "sans-serif"],
      },
      colors: {
        accent: '#6fff57',
        dark: '#232323',
        card: '#2d2d2d',
      },
    },
  },
  plugins: [],
}; 