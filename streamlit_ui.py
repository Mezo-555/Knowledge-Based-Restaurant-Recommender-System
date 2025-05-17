import streamlit as st
import pandas as pd
from data_preprocessing import load_and_preprocess_data
from recommendation_engine import filter_and_rank
from evaluation_logic import collect_user_feedback, ab_test  # import functions from your module

# === Load Data ===
st.title("Knowledge-Based Restaurant Recommender System")
st.write("Find the best dining options based on your preferences.")

file_path = "data/zomato.csv"
df = load_and_preprocess_data(file_path)

# === User Input ===
st.sidebar.header("Filter your preferences:")
cuisine = st.sidebar.text_input("Cuisine (e.g., Italian, Chinese, Indian)")
budget = st.sidebar.selectbox("Select your Budget", ['low', 'medium', 'high', 'luxury'])
location = st.sidebar.text_input("Location (City or Locality)")
top_n = st.sidebar.slider("Number of Recommendations", 1, 20, 10)

if st.sidebar.button("Get Recommendations"):
    # Get recommendations (A)
    recommendations = filter_and_rank(df, cuisine, budget, location, top_n)

    if not recommendations.empty:
        st.write(f"Top {top_n} recommendations:")
        for _, row in recommendations.iterrows():
            st.subheader(row['Restaurant Name'])
            st.write(f"Cuisine: {row['Primary Cuisine']}")
            st.write(f"Budget: {row['Average Cost for two']}")
            st.write(f"Rating: {row['Aggregate rating']}")
            st.write(f"Location: {row['Address']}")
            st.caption(row.get('Explanation', ''))
            st.write("---")

        # Collect user feedback (imported function)
        feedback = collect_user_feedback()
        if feedback:
            st.json(feedback)

        # Generate another recommendation set (B) for A/B testing (example, could be different)
        recommendations_b = filter_and_rank(df, cuisine, budget, location, top_n)
        
        # A/B testing - user chooses preferred list (imported function)
        choice = ab_test(recommendations, recommendations_b)
        if choice:
            st.write(f"User preferred: {choice}")

    else:
        st.warning("No restaurants found matching your criteria.")
