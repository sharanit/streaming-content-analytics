"""
Data Processing Module
Utilities for loading, cleaning, and preprocessing streaming content data
"""

import pandas as pd
import numpy as np
from datetime import datetime


def load_data(filepath):
    """
    Load streaming content dataset from CSV file
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    df = pd.read_csv(filepath)
    print(f"Data loaded successfully. Shape: {df.shape}")
    return df


def convert_date_added(df):
    """
    Convert date_added column to datetime format
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with converted date_added column
    """
    df = df.copy()
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    return df


def extract_duration_info(df):
    """
    Extract numeric duration for movies and seasons for TV shows
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with duration column
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with extracted duration_minutes and duration_seasons columns
    """
    df = df.copy()
    
    # Create duration columns
    df['duration_minutes'] = np.nan
    df['duration_seasons'] = np.nan
    
    # Extract minutes for movies
    mask_movies = df['type'] == 'Movie'
    df.loc[mask_movies, 'duration_minutes'] = df.loc[mask_movies, 'duration'].str.extract('(\d+)').astype(float)
    
    # Extract seasons for TV shows
    mask_tv = df['type'] == 'TV Show'
    df.loc[mask_tv, 'duration_seasons'] = df.loc[mask_tv, 'duration'].str.extract('(\d+)').astype(float)
    
    return df


def explode_column(df, column_name, delimiter=','):
    """
    Explode a column with delimited values into separate rows
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    column_name : str
        Name of column to explode
    delimiter : str
        Delimiter used in the column values
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with exploded column
    """
    df = df.copy()
    
    # Handle missing values
    df[column_name] = df[column_name].fillna('missing')
    
    # Split and explode
    df[column_name] = df[column_name].str.split(delimiter)
    df_exploded = df.explode(column_name)
    
    # Strip whitespace
    df_exploded[column_name] = df_exploded[column_name].str.strip()
    
    return df_exploded.reset_index(drop=True)


def calculate_content_lag(df):
    """
    Calculate the lag between release year and date added to platform
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with release_year and date_added columns
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with content_lag_years column
    """
    df = df.copy()
    
    # Extract year from date_added
    df['year_added'] = df['date_added'].dt.year
    
    # Calculate lag
    df['content_lag_years'] = df['year_added'] - df['release_year']
    
    # Handle negative or unrealistic values
    df.loc[df['content_lag_years'] < 0, 'content_lag_years'] = np.nan
    
    return df


def extract_temporal_features(df):
    """
    Extract temporal features from date_added column
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with date_added column
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with additional temporal columns
    """
    df = df.copy()
    
    # Extract features
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    df['month_name'] = df['date_added'].dt.month_name()
    df['day_of_week'] = df['date_added'].dt.day_name()
    df['quarter_added'] = df['date_added'].dt.quarter
    
    return df


def clean_country_column(df):
    """
    Clean and standardize country names
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with country column
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with cleaned country column
    """
    df = df.copy()
    
    # Common country name standardizations
    country_mapping = {
        'United States': 'United States',
        'India': 'India',
        'United Kingdom': 'United Kingdom',
        'Japan': 'Japan',
        'South Korea': 'South Korea',
        'Canada': 'Canada',
        'France': 'France',
        'Spain': 'Spain',
        'Germany': 'Germany',
        'Mexico': 'Mexico'
    }
    
    # Fill missing values
    df['country'] = df['country'].fillna('Unknown')
    
    return df


def handle_missing_values(df, strategy='default'):
    """
    Handle missing values in the dataframe
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    strategy : str
        Strategy for handling missing values ('default', 'drop', 'fill')
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with handled missing values
    """
    df = df.copy()
    
    if strategy == 'default':
        # Fill categorical columns with 'Unknown' or 'Not Available'
        df['director'] = df['director'].fillna('Not Available')
        df['cast'] = df['cast'].fillna('Not Available')
        df['country'] = df['country'].fillna('Unknown')
        df['rating'] = df['rating'].fillna('Not Rated')
        
    elif strategy == 'drop':
        # Drop rows with missing critical values
        df = df.dropna(subset=['title', 'type', 'release_year'])
        
    return df


def create_content_age(df):
    """
    Create content age feature (years since release)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with release_year column
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with content_age column
    """
    df = df.copy()
    current_year = datetime.now().year
    df['content_age'] = current_year - df['release_year']
    
    return df


def load_and_clean_data(filepath):
    """
    Complete pipeline to load and clean streaming content data
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Cleaned and processed dataframe
    """
    print("Loading data...")
    df = load_data(filepath)
    
    print("Converting date formats...")
    df = convert_date_added(df)
    
    print("Handling missing values...")
    df = handle_missing_values(df, strategy='default')
    
    print("Extracting duration information...")
    df = extract_duration_info(df)
    
    print("Extracting temporal features...")
    df = extract_temporal_features(df)
    
    print("Calculating content lag...")
    df = calculate_content_lag(df)
    
    print("Creating content age feature...")
    df = create_content_age(df)
    
    print(f"\nData cleaning complete! Final shape: {df.shape}")
    
    return df


def get_data_summary(df):
    """
    Generate a comprehensive summary of the dataframe
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    dict
        Dictionary containing various summary statistics
    """
    summary = {
        'total_records': len(df),
        'total_movies': len(df[df['type'] == 'Movie']),
        'total_tv_shows': len(df[df['type'] == 'TV Show']),
        'unique_countries': df['country'].nunique(),
        'unique_directors': df['director'].nunique(),
        'unique_genres': df['listed_in'].nunique(),
        'date_range': (df['date_added'].min(), df['date_added'].max()),
        'release_year_range': (df['release_year'].min(), df['release_year'].max()),
        'missing_values': df.isnull().sum().to_dict()
    }
    
    return summary


if __name__ == "__main__":
    # Example usage
    print("Data Processing Module")
    print("Import this module to use data processing functions")
