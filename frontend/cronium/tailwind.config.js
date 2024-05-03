/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      animation: {
				fade: 'fadeIn 0.8s ease-in-out',
			},
      keyframes: {
				fadeIn: {
					from: { opacity: 0 },
					to: { opacity: 1 },
				},
      },
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors : {
        "side-color": "#5F1DF9",
        "side-hover": "#521ad6",
        "purple-dark": "#4C17C7",
        "purple-dark": "#391195",
        "purple-xdark": "#2F0E7C",
        "purple-tint": "#6F33F9",
        "purple-tint-light": "#8F60FA"
      }
    },
  },
  plugins: [],
};
