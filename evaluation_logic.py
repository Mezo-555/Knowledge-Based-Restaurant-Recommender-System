import streamlit as st
import pandas as pd
import numpy as np

# === Qualitative Evaluation ===
def collect_user_feedback():
    """
    Displays a short survey to collect user feedback after recommendation.
    
    Returns:
        dict: User feedback with scores for satisfaction, relevance, and usability.
    """
    st.write("### We would love to hear your feedback!")
    
    satisfaction = st.slider("How satisfied are you with the recommendations?", 1, 5, 3)
    relevance = st.slider("How relevant were the restaurant suggestions?", 1, 5, 3)
    usability = st.slider("How easy was it to use the recommendation system?", 1, 5, 3)
    
    if st.button("Submit Feedback"):
        feedback = {
            'Satisfaction': satisfaction,
            'Relevance': relevance,
            'Usability': usability
        }
        st.success("Thank you for your feedback!")
        return feedback
    return None

# === A/B Testing ===
def ab_test(recommendations_a, recommendations_b):
    """
    Compare two sets of recommendations and collect user preference.
    
    Parameters:
        recommendations_a (pd.DataFrame): First set of recommendations.
        recommendations_b (pd.DataFrame): Second set of recommendations.
    
    Returns:
        str: User's preferred recommendation set.
    """
    st.write("### A/B Test - Which list do you prefer?")
    st.write("**List A**")
    st.table(recommendations_a.head(5))
    
    st.write("**List B**")
    st.table(recommendations_b.head(5))

    choice = st.radio("Which list is more relevant?", ('List A', 'List B'))

    if st.button("Submit Choice"):
        st.success(f"You selected {choice}. Thank you!")
        return choice
    return None