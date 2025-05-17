import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess_data(filepath):
    '''
    Load and preprocess the Zomato dataset.
    
    Parameters:
        filepath (str): Path to the Zomato.csv file.
    
    Returns:
        pd.DataFrame: Cleaned and preprocessed DataFrame.
    '''
    # Load the dataset
    df = pd.read_csv(filepath, encoding='ISO-8859-1')

    # Drop duplicates and irrelevant columns
    df.drop_duplicates(inplace=True)
    columns_to_drop = ['Switch to order menu', 'Rating color', 'Rating text', 'Locality Verbose']
    df.drop(columns=columns_to_drop, inplace=True)

    # Handle missing values
    df.fillna(method='ffill', inplace=True)

    # Normalize categorical values
    df['Cuisines'] = df['Cuisines'].str.lower()

    # Convert price and rating fields to numerical formats
    df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'], errors='coerce')
    df['Price range'] = pd.to_numeric(df['Price range'], errors='coerce')
    df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

    # Feature Engineering
    price_mapping = {1: 'low', 2: 'medium', 3: 'high', 4: 'luxury'}
    df['Price Bucket'] = df['Price range'].map(price_mapping)
    df['Primary Cuisine'] = df['Cuisines'].apply(lambda x: x.split(',')[0] if pd.notna(x) else x)

    # Map user ratings to a consistent scale (1–5)
    scaler = MinMaxScaler(feature_range=(1, 5))
    df[['Aggregate rating']] = scaler.fit_transform(df[['Aggregate rating']]).round(1)

    return df