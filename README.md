
# ⚽ Football Stats Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![StatsBomb](https://img.shields.io/badge/Data-StatsBomb%20Open%20Data-green)
![License](https://img.shields.io/badge/Status-Completed-success)

An interactive football analytics dashboard built using **Python**, **Streamlit**, **StatsBomb Open Data**, and **mplsoccer**. The application transforms raw football event data into meaningful visualizations that help analyze team and player performance.

---

# 🚀 Live Demo

### Working Prototype

👉 https://footballstatsanalysis-chandrsekharboddeboina28.streamlit.app/

---

# 📖 Project Overview

Football matches generate thousands of event records including passes, shots, dribbles, tackles, substitutions, and player movements. Reading this raw data is difficult and provides little tactical insight.

This project converts those events into an interactive analytics dashboard where users can explore matches visually and compare team performances using advanced football metrics.

The dashboard is completely dynamic. Selecting another competition, season, match, or team automatically updates every visualization and statistical summary.

---

# 🎯 Objectives

The primary objectives of this project are to:

- Transform raw football event data into visual insights.
- Compare home and away team performances.
- Analyze player positioning and involvement.
- Visualize passing networks.
- Evaluate shooting quality using Expected Goals (xG).
- Create an interactive dashboard accessible through any web browser.

---

# ✨ Features

## Match Selection

- Select different seasons.
- Choose any available match.

---

## Match Summary Dashboard

Displays key statistics for both teams.

Metrics include:

- Total Shots
- Expected Goals (xG)
- Pass Accuracy
- Possession Percentage
- Final Match Score

These statistics update automatically whenever another match is selected.

---

## Shot Map

Visualizes every shot taken by the selected team.

Features:

- Goal locations
- Missed shots
- Shot quality
- Expected Goals (xG)
- Shot positions

Circle size represents Expected Goals.

Larger circles indicate higher-quality chances.

---

## Passing Network

Displays passing relationships between players.

Shows:

- Average player positions
- Successful passing combinations
- Frequently connected players
- Team passing structure

Only passing combinations occurring at least three times are displayed for better readability.

---

## Player Heatmap

Select any player to visualize where they spent most of the match.

The heatmap highlights:

- Touch density
- Positioning
- Areas of influence
- Overall movement

---

## Interactive Dashboard

Users can interactively change:

- Competition
- Season
- Match
- Team
- Player

Every chart updates instantly.

---

## Custom User Interface

The application includes a custom CSS theme featuring:

- Modern dark interface
- Styled metric cards
- Improved typography
- Responsive layout
- Professional football dashboard appearance

---

# 📊 Dashboard Workflow

```
Select Competition
        │
        ▼
Select Season
        │
        ▼
Choose Match
        │
        ▼
Download Match Events
        │
        ▼
Generate Match Summary
        │
        ▼
Choose Team
        │
        ▼
Choose Player
        │
        ▼
Visualize

• Match Summary
• Shot Map
• Passing Network
• Player Heatmap
```

---

# 🏗 Project Structure

```
FootballStatsAnalysis
│
├── app.py
├── data.py
├── charts.py
├── css.py
├── requirements.txt
├── README.md
```

---

# ⚙ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Interactive Web Dashboard |
| StatsBombPy | Football Event Data |
| mplsoccer | Football Pitch Visualizations |
| Pandas | Data Cleaning |
| NumPy | Numerical Operations |
| Matplotlib | Graph Plotting |
| CSS | Dashboard Styling |

---

# 📂 Core Functions

## get_competition()

Retrieves all available football competitions from StatsBomb.

Returns

- Competition DataFrame

---

## get_matches()

Retrieves all matches for the selected competition and season.

Returns

- Match DataFrame

---

## get_clean_events()

Downloads raw event data.

Processes

- Shot events
- Pass events
- Player touches

Returns

- Shots DataFrame
- Passes DataFrame
- Touches DataFrame

---

## plot_shot()

Creates the Shot Map.

Displays

- Goals
- Missed shots
- Expected Goals
- Total xG

---

## plot_passes()

Creates the Passing Network.

Calculates

- Average player positions
- Passing links
- Pass frequency

---

## plot_mostTime()

Creates the Player Heatmap.

Displays

- Touch density
- Areas of influence
- Player positioning

---

## load_events()

Caches event data using Streamlit.

Benefits

- Faster loading
- Reduced API requests
- Improved dashboard performance

---

# 📈 Match Statistics Calculated

The dashboard calculates several performance metrics directly from StatsBomb event data.

### Total Shots

Number of shots attempted by each team.

### Expected Goals (xG)

Measures the probability that a shot results in a goal.

Higher xG indicates better scoring opportunities.

### Pass Accuracy

Calculated using:

```
Completed Passes / Total Passes × 100
```

Shows passing efficiency.

### Possession

Calculated using player touch events.

```
Team Touches / Total Match Touches × 100
```

Provides an estimate of match possession.

---

# 📊 Insights Generated

The dashboard helps answer questions such as:

- Which team created better scoring opportunities?
- Which players controlled possession?
- Which passing combinations occurred most frequently?
- Where did a player spend most of the match?
- Which team maintained better passing accuracy?
- How balanced was possession?
- Which players were most involved in the game?

---

# 🔮 Future Development

The project can be extended with advanced football analytics including:

- Progressive Pass Analysis
- Defensive Action Maps
- Pressure Maps
- Ball Recovery Analysis
- Player Comparison Dashboard
- Team Comparison Dashboard
- Goalkeeper Analysis
- Passing Accuracy Heatmaps
- Shot Statistics by Player
- Interactive Plotly Charts
- Match Filtering by Team and Player
- Performance optimization with additional caching

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

Move into the project directory

```bash
cd <repository-name>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🌍 Working Prototype

https://footballstatsanalysis-chandrsekharboddeboina28.streamlit.app/

---

# 📚 Data Source

This project uses the official **StatsBomb Open Data** dataset.

https://github.com/statsbomb/open-data

---


# 👨‍💻 Author

### Chandrasekhar Boddeboina

Python Developer • Data Analytics Enthusiast • Football Analytics Learner

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
