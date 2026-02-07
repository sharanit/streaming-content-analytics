"""
Analysis Module
Utilities for performing statistical analysis and deriving insights
"""

import pandas as pd
import numpy as np
from collections import Counter


def get_top_genres(df, n=10):
    """
    Get top N genres by count
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'listed_in' column
    n : int
        Number of top genres to return
        
    Returns:
    --------
    pd.Series
        Top genres with counts
    """
    genres = df['listed_in'].str.split(', ').explode()
    return genres.value_counts().head(n)


def get_top_countries(df, n=10):
    """
    Get top N countries by content count
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'country' column
    n : int
        Number of top countries to return
        
    Returns:
    --------
    pd.Series
        Top countries with counts
    """
    return df['country'].value_counts().head(n)


def get_top_directors(df, n=10):
    """
    Get top N directors by content count
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'director' column
    n : int
        Number of top directors to return
        
    Returns:
    --------
    pd.Series
        Top directors with counts
    """
    directors = df['director'].str.split(', ').explode()
    directors = directors[directors != 'Not Available']
    return directors.value_counts().head(n)


def get_top_actors(df, n=10):
    """
    Get top N actors by appearances
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'cast' column
    n : int
        Number of top actors to return
        
    Returns:
    --------
    pd.Series
        Top actors with counts
    """
    actors = df['cast'].str.split(', ').explode()
    actors = actors[actors != 'Not Available']
    return actors.value_counts().head(n)


def analyze_content_by_year(df):
    """
    Analyze content additions and releases by year
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with temporal columns
        
    Returns:
    --------
    dict
        Dictionary containing yearly analysis
    """
    analysis = {
        'releases_by_year': df.groupby('release_year').size().to_dict(),
        'additions_by_year': df.groupby('year_added').size().to_dict(),
        'avg_content_lag': df.groupby('year_added')['content_lag_years'].mean().to_dict(),
        'content_type_by_year': df.groupby(['year_added', 'type']).size().unstack(fill_value=0).to_dict()
    }
    
    return analysis


def analyze_content_by_country(df, country):
    """
    Analyze content for a specific country
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    country : str
        Country name to analyze
        
    Returns:
    --------
    dict
        Dictionary containing country-specific analysis
    """
    country_df = df[df['country'] == country]
    
    analysis = {
        'total_content': len(country_df),
        'movies': len(country_df[country_df['type'] == 'Movie']),
        'tv_shows': len(country_df[country_df['type'] == 'TV Show']),
        'top_genres': get_top_genres(country_df, n=5).to_dict(),
        'top_directors': get_top_directors(country_df, n=5).to_dict(),
        'avg_release_year': country_df['release_year'].mean(),
        'rating_distribution': country_df['rating'].value_counts().to_dict()
    }
    
    return analysis


def analyze_genre_trends(df):
    """
    Analyze genre trends over time
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Genre trends by year
    """
    # Explode genres
    df_exploded = df.copy()
    df_exploded['listed_in'] = df_exploded['listed_in'].str.split(', ')
    df_exploded = df_exploded.explode('listed_in')
    
    # Get top genres
    top_genres = df_exploded['listed_in'].value_counts().head(10).index
    
    # Filter for top genres
    df_top_genres = df_exploded[df_exploded['listed_in'].isin(top_genres)]
    
    # Create pivot table
    genre_trends = pd.crosstab(df_top_genres['year_added'], df_top_genres['listed_in'])
    
    return genre_trends


def calculate_diversity_metrics(df):
    """
    Calculate content diversity metrics
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    dict
        Dictionary containing diversity metrics
    """
    metrics = {
        'unique_countries': df['country'].nunique(),
        'unique_directors': df['director'].str.split(', ').explode().nunique(),
        'unique_actors': df['cast'].str.split(', ').explode().nunique(),
        'unique_genres': df['listed_in'].str.split(', ').explode().nunique(),
        'unique_ratings': df['rating'].nunique(),
        'movie_tv_ratio': len(df[df['type'] == 'Movie']) / len(df[df['type'] == 'TV Show'])
    }
    
    return metrics


def analyze_optimal_launch_timing(df):
    """
    Analyze optimal launch timing based on historical data
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with temporal columns
        
    Returns:
    --------
    dict
        Dictionary containing launch timing insights
    """
    timing = {
        'best_month': df['month_name'].value_counts().idxmax(),
        'best_day': df['day_of_week'].value_counts().idxmax(),
        'best_quarter': df['quarter_added'].value_counts().idxmax(),
        'month_distribution': df['month_name'].value_counts().to_dict(),
        'day_distribution': df['day_of_week'].value_counts().to_dict(),
        'quarter_distribution': df['quarter_added'].value_counts().to_dict()
    }
    
    return timing


def compare_movies_vs_tv_shows(df):
    """
    Compare characteristics of movies vs TV shows
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    dict
        Dictionary containing comparison metrics
    """
    movies = df[df['type'] == 'Movie']
    tv_shows = df[df['type'] == 'TV Show']
    
    comparison = {
        'count': {
            'movies': len(movies),
            'tv_shows': len(tv_shows)
        },
        'avg_release_year': {
            'movies': movies['release_year'].mean(),
            'tv_shows': tv_shows['release_year'].mean()
        },
        'avg_content_lag': {
            'movies': movies['content_lag_years'].mean(),
            'tv_shows': tv_shows['content_lag_years'].mean()
        },
        'top_countries': {
            'movies': movies['country'].value_counts().head(5).to_dict(),
            'tv_shows': tv_shows['country'].value_counts().head(5).to_dict()
        },
        'top_ratings': {
            'movies': movies['rating'].value_counts().head(5).to_dict(),
            'tv_shows': tv_shows['rating'].value_counts().head(5).to_dict()
        }
    }
    
    return comparison


def identify_content_gaps(df):
    """
    Identify potential content gaps and opportunities
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    dict
        Dictionary containing gap analysis
    """
    # Get all genres
    all_genres = df['listed_in'].str.split(', ').explode().value_counts()
    
    # Identify underrepresented genres (bottom 25%)
    threshold = all_genres.quantile(0.25)
    underrepresented = all_genres[all_genres <= threshold]
    
    # Analyze recent trends
    recent_df = df[df['year_added'] >= df['year_added'].max() - 2]
    recent_genres = recent_df['listed_in'].str.split(', ').explode().value_counts()
    
    gaps = {
        'underrepresented_genres': underrepresented.to_dict(),
        'emerging_genres': recent_genres.head(10).to_dict(),
        'declining_genres': (all_genres.head(10).index.difference(recent_genres.head(10).index)).tolist()
    }
    
    return gaps


def generate_business_recommendations(df):
    """
    Generate data-driven business recommendations
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    list
        List of recommendation dictionaries
    """
    recommendations = []
    
    # Content type recommendation
    movie_ratio = len(df[df['type'] == 'Movie']) / len(df)
    if movie_ratio > 0.7:
        recommendations.append({
            'category': 'Content Balance',
            'finding': f'Movies comprise {movie_ratio*100:.1f}% of catalog',
            'recommendation': 'Increase TV show production to improve subscriber retention',
            'priority': 'High'
        })
    
    # Geographic expansion
    top_countries = df['country'].value_counts().head(3)
    if 'India' in top_countries.index or 'South Korea' in top_countries.index:
        recommendations.append({
            'category': 'Geographic Expansion',
            'finding': 'Strong presence in high-growth Asian markets',
            'recommendation': 'Triple investment in Indian and Korean content',
            'priority': 'Very High'
        })
    
    # Launch timing
    timing = analyze_optimal_launch_timing(df)
    recommendations.append({
        'category': 'Launch Strategy',
        'finding': f"Peak additions in {timing['best_month']} on {timing['best_day']}",
        'recommendation': f"Schedule major releases for {timing['best_day']}s in {timing['best_month']}",
        'priority': 'Medium'
    })
    
    # Content freshness
    avg_lag = df['content_lag_years'].mean()
    if avg_lag > 3:
        recommendations.append({
            'category': 'Content Freshness',
            'finding': f'Average content lag is {avg_lag:.1f} years',
            'recommendation': 'Increase original content production to reduce dependency on catalog acquisitions',
            'priority': 'High'
        })
    
    # Rating diversity
    mature_content = df[df['rating'].isin(['TV-MA', 'R', 'TV-14'])].shape[0] / len(df)
    if mature_content > 0.75:
        recommendations.append({
            'category': 'Audience Diversification',
            'finding': f'{mature_content*100:.1f}% of content targets mature audiences',
            'recommendation': 'Expand family-friendly content to capture broader demographic',
            'priority': 'Medium'
        })
    
    return recommendations


def create_executive_summary(df):
    """
    Create an executive summary of key metrics
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    dict
        Dictionary containing executive summary
    """
    summary = {
        'total_titles': len(df),
        'content_split': {
            'movies': f"{len(df[df['type'] == 'Movie']) / len(df) * 100:.1f}%",
            'tv_shows': f"{len(df[df['type'] == 'TV Show']) / len(df) * 100:.1f}%"
        },
        'geographic_reach': {
            'countries': df['country'].nunique(),
            'top_market': df['country'].value_counts().index[0]
        },
        'content_recency': {
            'avg_release_year': int(df['release_year'].mean()),
            'avg_content_age': f"{df['content_age'].mean():.1f} years"
        },
        'top_genre': df['listed_in'].str.split(', ').explode().value_counts().index[0],
        'primary_rating': df['rating'].value_counts().index[0],
        'key_insight': generate_key_insight(df)
    }
    
    return summary


def generate_key_insight(df):
    """
    Generate a key insight from the data
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    str
        Key insight statement
    """
    # Analyze growth trend
    recent_years = df[df['year_added'] >= df['year_added'].max() - 3]
    tv_growth = len(recent_years[recent_years['type'] == 'TV Show']) / len(recent_years)
    
    if tv_growth > 0.4:
        return "Platform shifting focus toward TV shows with 40%+ of recent additions being series content"
    else:
        return "Platform maintaining traditional movie-focused strategy with selective TV show additions"


if __name__ == "__main__":
    print("Analysis Module")
    print("Import this module to use analysis functions")
