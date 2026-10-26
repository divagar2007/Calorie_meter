# 🍎 Calorie Tracker Dashboard

## 📌 Project Overview

The **Calorie Tracker Dashboard** is a web-based application designed to track daily food calorie intake and display food history in a visually appealing dashboard. It helps users monitor calorie consumption, view calorie trends, and understand the distribution of calories across different food entries.

The dashboard features a modern interface with dark and light modes, summary cards, interactive charts, and a food history table.

## 🎯 Objectives

- Track calorie intake for different food items.
- Display the total number of food entries.
- Calculate total and average calorie consumption.
- Visualize calorie trends using charts.
- Display food history with dates and calorie values.
- Provide a responsive and user-friendly dashboard.

## ✨ Features

- **Total Entries:** Displays the number of recorded food entries.
- **Total Calories:** Shows the total calories consumed across all entries.
- **Average Calories:** Calculates the average calories per food entry.
- **Calorie Trend Chart:** Displays calorie values using a line chart.
- **Food Distribution Chart:** Visualizes calorie distribution using a pie chart.
- **Food History Table:** Displays the date, food name, and calorie count.
- **Dark and Light Mode:** Allows users to switch between themes.
- **Responsive Design:** Adjusts the dashboard layout for different screen sizes.
- **JSON Data Integration:** Loads food history from a local JSON file.

## 🛠️ Technologies Used

- **HTML5** – Structures the dashboard.
- **CSS3** – Provides styling, layout, gradients, and responsive design.
- **JavaScript** – Handles calculations, data loading, and theme switching.
- **Chart.js** – Creates interactive line and pie charts.
- **JSON** – Stores food history data.

## 📂 Project Structure

```text
CalorieTracker/
│
├── index.html
├── history.json
└── README.md
```

## ⚙️ Installation and Setup

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Create a folder named `CalorieTracker`.
3. Create an `index.html` file and add the dashboard code.
4. Create a `history.json` file containing food history data.
5. Create this `README.md` file in the same folder.
6. Install the **Live Server** extension in VS Code.
7. Right-click `index.html` and select **Open with Live Server**.

**Note:** An internet connection is required to load the Chart.js library from the CDN used in the HTML file.

## 📊 Sample Data

The `history.json` file should contain data in the following format:

```json
[
  {
    "date": "2026-10-24",
    "food": "Idli",
    "calories": 150
  },
  {
    "date": "2026-10-25",
    "food": "Dosa",
    "calories": 220
  },
  {
    "date": "2026-10-26",
    "food": "Rice",
    "calories": 300
  }
]
```

## 🖥️ Dashboard Components

### 1. Summary Cards
Displays total food entries, total calories, and average calories.

### 2. Calorie Trend
A line chart that visualizes calorie values for recorded food entries.

### 3. Food Distribution
A pie chart that represents the calorie contribution of individual food entries.

### 4. Food History
A table that lists the date, food item, and corresponding calorie value.

### 5. Theme Toggle
Switches between dark and light display modes.

## 🚀 Future Enhancements

- Add a form to enter food items and calorie values.
- Store food history using a database or browser storage.
- Add daily and weekly calorie summaries.
- Include calorie goals and progress tracking.
- Add food search, filtering, and deletion options.
- Display nutritional information such as protein, carbohydrates, and fats.
- Add user authentication and personalized dashboards.

## 🔒 Limitations

- Food history is currently loaded from a JSON file.
- The dashboard does not currently save new entries automatically.
- Calorie estimates depend on the accuracy of the supplied data.
- The current average represents calories per recorded food entry, not necessarily the average daily calorie intake.

## 🎓 Conclusion

The Calorie Tracker Dashboard provides a simple and interactive way to monitor food calorie information. By combining HTML, CSS, JavaScript, JSON, and Chart.js, the project demonstrates data visualization, dynamic content updates, responsive web design, and basic nutritional tracking.

---

**Project Name:** Calorie Tracker Dashboard  
**Project Type:** Web Development  
**Frontend:** HTML, CSS, JavaScript  
**Data Format:** JSON  
**Chart Library:** Chart.js
