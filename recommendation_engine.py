import numpy as np

def filter_and_rank(df, cuisine=None, budget=None, location=None, top_n=20):
    '''
    Filter and rank restaurants based on user preferences.
    
    Parameters:
        df (pd.DataFrame): Preprocessed DataFrame containing restaurant data.
        cuisine (str): Preferred cuisine type.
        budget (str): Price bucket ('low', 'medium', 'high').
        location (str): Preferred location or city.
        top_n (int): Number of top recommendations to return.
    
    Returns:
        pd.DataFrame: Top-N ranked restaurant recommendations.
    '''
    
    # Apply filters
    if cuisine:
        df = df[df['Primary Cuisine'].str.contains(cuisine.lower(), na=False)]
    if budget:
        df = df[df['Price Bucket'] == budget.lower()]
    if location:
        df = df[df['City'].str.contains(location, na=False)]
    
    # Ranking Strategy: Rating weighted by number of votes (if available)
    if 'Votes' in df.columns:
        df['Score'] = df['Aggregate rating'] * np.log1p(df['Votes'])
    else:
        df['Score'] = df['Aggregate rating']

    # Sort by score and select top N
    recommendations = df.sort_values(by='Score', ascending=False).head(top_n)

    # Add explanation for each recommendation
    recommendations['Explanation'] = recommendations.apply(
        lambda x: f"Matched on {x['Primary Cuisine']} cuisine and {x['Average Cost for two']} budget with {x['Aggregate rating']} rating.",
        axis=1
    )

    # Return only relevant columns
    return recommendations[['Restaurant Name', 'Primary Cuisine', 'Price Bucket', 'Average Cost for two', 'Aggregate rating', 'Address', 'City', 'Explanation']]
