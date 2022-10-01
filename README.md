# BottlePy-Final-Project
module.exports = {
  mode : "jit",
  content: [
    "../views/*.html"
  ],
  theme: {
    extend: {
      colors:{
        "blue1": "#1DA1F2",
        "blue2": "#2795D9",
        "blue": "#EFF9FF",
        "dark": "#657786",
        "light": "#AAB8C2",
        "lighter": "#E1E8ED",
        "lightest": "#F5F8FA",
      }  
    },
  },
  plugins: [],
}


# Install tailwind
create tailwindcss dir and follow the following steps
- cd tailwindcss
- npm install -d tailwindcss@latest postcss@latest autoprefixer@latest
- npx tailwindcss init

Set these 3 lines in the tailwindcss.css file:
@tailwind base;
@tailwind components;
@tailwind utilities;

npx tailwindcss -i tailwindcss.css -o ../app.css --watch