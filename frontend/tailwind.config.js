module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        positive: '#22c55e',  // Green
        negative: '#ef4444',  // Red
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
  darkMode: 'class',
  plugins: [],
}