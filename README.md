# Knowledge-Based Restaurant Recommender System

## 📌 Project Overview

The **Knowledge-Based Restaurant Recommender System** is a web application built using **Streamlit**. It leverages the **Zomato Restaurant Dataset** to provide personalized dining recommendations based on user preferences like cuisine, location, and budget. Users can filter their preferences, get restaurant suggestions, and participate in A/B testing to refine the recommendation logic.

---

## ✨ Features

* **Cuisine, Budget, and Location Filtering**: Easily find the best restaurants that match your taste and budget.
* **Real-time Recommendations**: Displays top restaurant suggestions with essential details.
* **A/B Testing**: Allows users to compare two recommendation lists and pick the better one.
* **User Feedback Collection**: Gathers user satisfaction, relevance, and usability feedback.

---

## ⚙️ Installation Guide

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Mezo-555/Knowledge-Based-Restaurant-Recommender-System.git
   cd Knowledge-Based-Restaurant-Recommender-System
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Zomato Dataset:**

   * Place the dataset in a folder named `data` with the filename `zomato.csv`.

4. **Run the application:**

   ```bash
   streamlit run streamlit_ui.py
   ```

5. **Access the app at:**

   ```
   http://localhost:8501
   ```

---

## 🌐 Deployed Application

The application is live and can be accessed [here](https://knowledge-based-restaurant-recommender-system-q4dwpzb7msffd3ep.streamlit.app/).

---

## 🚀 Usage Instructions

1. Enter your preferred **Cuisine**, **Budget**, and **Location** in the sidebar.
2. Select the **Number of Recommendations** you want.
3. Click `Get Recommendations` to display restaurant options.
4. Provide your **feedback** on the recommendations.
5. Participate in **A/B Testing** to improve the recommendation logic.

---

## 📌 Application Logic

The application consists of three main logic components:

### 1️⃣ **Data Preprocessing**

The `load_and_preprocess_data` function handles the following:

* **Loading Data:**

  * Reads the dataset using `pandas.read_csv` with proper encoding.

* **Data Cleaning:**

  * Removes duplicates and irrelevant columns (`Switch to order menu`, `Rating color`, `Rating text`, `Locality Verbose`).
  * Handles missing values using **forward fill**.

* **Feature Engineering:**

  * Converts cuisine names to lowercase for consistency.
  * Price and rating fields are cast to numeric types.
  * A `Price Bucket` column is generated based on the `Price range` column.
  * Extracts the primary cuisine from the list of cuisines.

* **Feature Scaling:**

  * `MinMaxScaler` normalizes the `Aggregate rating` to a scale of **1 to 5**.

---

### 2️⃣ **Recommendation Logic**

The recommendation logic is handled by the `filter_and_rank` function, which includes:

* **Filtering:**

  * Applies user preferences for cuisine, budget, and location.
  * Filters the dataset using case-insensitive string matching.

* **Ranking Strategy:**

  * Ranks restaurants by **Aggregate rating**, weighted by the natural logarithm of their number of votes.
  * If votes are not available, the ranking relies solely on the rating.

* **Explanation Generation:**

  * Generates a justification for each recommendation based on user preferences and restaurant attributes.

* **Final Selection:**

  * The top-N restaurants are displayed in the app.

---

### 3️⃣ **Evaluation Logic**

The evaluation logic consists of:

* **User Feedback Collection:**

  * After displaying recommendations, a survey is presented to gather feedback on **Satisfaction**, **Relevance**, and **Usability**.

* **A/B Testing:**

  * Two recommendation lists are generated, and the user is asked to pick the preferred one.

---

## 🚀 Future Enhancements

* Add **restaurant images** for better visualization.
* Implement **location-based suggestions** using geolocation.
* Improve **A/B testing logic** with deeper statistical analysis.
* Store user feedback for long-term improvement and analytics.

Feel free to reach out for any issues or feature requests!