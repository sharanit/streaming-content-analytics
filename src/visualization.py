"""
Visualization Module
Utilities for creating insightful visualizations of streaming content data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import warnings

warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10


def create_content_distribution_plot(df, save_path=None):
    """
    Create a bar plot showing distribution of Movies vs TV Shows
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'type' column
    save_path : str, optional
        Path to save the figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    type_counts = df['type'].value_counts()
    colors = ['#E50914', '#221F1F']
    
    ax.bar(type_counts.index, type_counts.values, color=colors, edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Content Type', fontsize=12, fontweight='bold')
    ax.set_ylabel('Count', fontsize=12, fontweight='bold')
    ax.set_title('Distribution of Content Types', fontsize=14, fontweight='bold', pad=20)
    
    # Add value labels on bars
    for i, v in enumerate(type_counts.values):
        ax.text(i, v + 50, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_top_countries_plot(df, n=10, save_path=None):
    """
    Create a horizontal bar plot of top content-producing countries
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'country' column
    n : int
        Number of top countries to display
    save_path : str, optional
        Path to save the figure
    """
    # Get top countries
    top_countries = df['country'].value_counts().head(n)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    ax.barh(top_countries.index[::-1], top_countries.values[::-1], color='#E50914', edgecolor='black')
    ax.set_xlabel('Number of Titles', fontsize=12, fontweight='bold')
    ax.set_ylabel('Country', fontsize=12, fontweight='bold')
    ax.set_title(f'Top {n} Content Producing Countries', fontsize=14, fontweight='bold', pad=20)
    
    # Add value labels
    for i, v in enumerate(top_countries.values[::-1]):
        ax.text(v + 10, i, str(v), va='center', fontweight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_genre_distribution_plot(df, n=15, save_path=None):
    """
    Create a plot showing top genres
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'listed_in' column
    n : int
        Number of top genres to display
    save_path : str, optional
        Path to save the figure
    """
    # Explode genres and get counts
    genres = df['listed_in'].str.split(', ').explode()
    top_genres = genres.value_counts().head(n)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    ax.barh(top_genres.index[::-1], top_genres.values[::-1], color='#B20710', edgecolor='black')
    ax.set_xlabel('Number of Titles', fontsize=12, fontweight='bold')
    ax.set_ylabel('Genre', fontsize=12, fontweight='bold')
    ax.set_title(f'Top {n} Genres', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_release_year_trend(df, save_path=None):
    """
    Create a line plot showing content release trends over years
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'release_year' and 'type' columns
    save_path : str, optional
        Path to save the figure
    """
    # Filter for recent years (last 30 years)
    current_year = pd.Timestamp.now().year
    df_recent = df[df['release_year'] >= current_year - 30]
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Create data for movies and TV shows
    movies_by_year = df_recent[df_recent['type'] == 'Movie']['release_year'].value_counts().sort_index()
    tv_by_year = df_recent[df_recent['type'] == 'TV Show']['release_year'].value_counts().sort_index()
    
    ax.plot(movies_by_year.index, movies_by_year.values, marker='o', label='Movies', color='#E50914', linewidth=2)
    ax.plot(tv_by_year.index, tv_by_year.values, marker='s', label='TV Shows', color='#221F1F', linewidth=2)
    
    ax.set_xlabel('Release Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Titles', fontsize=12, fontweight='bold')
    ax.set_title('Content Release Trends (Last 30 Years)', fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_addition_by_month_plot(df, save_path=None):
    """
    Create a bar plot showing content additions by month
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'month_name' column
    save_path : str, optional
        Path to save the figure
    """
    # Define month order
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    month_counts = df['month_name'].value_counts().reindex(month_order)
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    colors = ['#E50914' if x == month_counts.max() else '#B20710' for x in month_counts.values]
    ax.bar(month_counts.index, month_counts.values, color=colors, edgecolor='black')
    
    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Additions', fontsize=12, fontweight='bold')
    ax.set_title('Content Additions by Month', fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_addition_by_day_plot(df, save_path=None):
    """
    Create a bar plot showing content additions by day of week
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'day_of_week' column
    save_path : str, optional
        Path to save the figure
    """
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    day_counts = df['day_of_week'].value_counts().reindex(day_order)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    colors = ['#E50914' if x == day_counts.max() else '#B20710' for x in day_counts.values]
    ax.bar(day_counts.index, day_counts.values, color=colors, edgecolor='black')
    
    ax.set_xlabel('Day of Week', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Additions', fontsize=12, fontweight='bold')
    ax.set_title('Content Additions by Day of Week', fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_rating_distribution_plot(df, save_path=None):
    """
    Create a pie chart showing distribution of content ratings
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'rating' column
    save_path : str, optional
        Path to save the figure
    """
    rating_counts = df['rating'].value_counts().head(10)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = sns.color_palette('Reds_r', len(rating_counts))
    
    wedges, texts, autotexts = ax.pie(rating_counts.values, labels=rating_counts.index, 
                                        autopct='%1.1f%%', startangle=90, colors=colors,
                                        textprops={'fontsize': 10, 'fontweight': 'bold'})
    
    ax.set_title('Distribution of Content Ratings', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_duration_distribution_plot(df, content_type='TV Show', save_path=None):
    """
    Create a histogram of duration distribution
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    content_type : str
        'Movie' or 'TV Show'
    save_path : str, optional
        Path to save the figure
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    if content_type == 'Movie':
        data = df[df['type'] == 'Movie']['duration_minutes'].dropna()
        ax.hist(data, bins=30, color='#E50914', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Duration (Minutes)', fontsize=12, fontweight='bold')
        ax.set_title('Distribution of Movie Durations', fontsize=14, fontweight='bold', pad=20)
    else:
        data = df[df['type'] == 'TV Show']['duration_seasons'].dropna()
        ax.hist(data, bins=range(1, int(data.max()) + 2), color='#E50914', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Number of Seasons', fontsize=12, fontweight='bold')
        ax.set_title('Distribution of TV Show Seasons', fontsize=14, fontweight='bold', pad=20)
    
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_content_lag_plot(df, save_path=None):
    """
    Create a histogram showing lag between release and platform addition
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'content_lag_years' column
    save_path : str, optional
        Path to save the figure
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    data = df['content_lag_years'].dropna()
    data = data[data <= 50]  # Filter outliers
    
    ax.hist(data, bins=30, color='#E50914', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Years Between Release and Addition', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title('Content Lag Distribution', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_wordcloud(df, column='description', save_path=None):
    """
    Create a word cloud from text data
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name containing text data
    save_path : str, optional
        Path to save the figure
    """
    text = ' '.join(df[column].dropna().astype(str))
    
    wordcloud = WordCloud(width=1600, height=800, 
                          background_color='white',
                          colormap='Reds',
                          max_words=100).generate(text)
    
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title(f'Word Cloud - {column.title()}', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_interactive_geographic_plot(df):
    """
    Create an interactive geographic plot using plotly
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with 'country' column
        
    Returns:
    --------
    plotly figure object
    """
    country_counts = df['country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']
    
    fig = px.choropleth(country_counts, 
                        locations='country',
                        locationmode='country names',
                        color='count',
                        hover_name='country',
                        color_continuous_scale='Reds',
                        title='Geographic Distribution of Content')
    
    fig.update_layout(height=600)
    
    return fig


if __name__ == "__main__":
    print("Visualization Module")
    print("Import this module to use visualization functions")
