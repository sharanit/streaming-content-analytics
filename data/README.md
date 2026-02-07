# Data Directory

## Dataset Information

### Source
The dataset used in this project contains information about movies and TV shows available on a major streaming platform as of mid-2021.

### Dataset Download
Due to size constraints, the dataset is not included in this repository. You can obtain the dataset from:
- Kaggle: Search for "Netflix Movies and TV Shows"
- Alternative sources: Similar streaming platform datasets

### Required File
Place the downloaded CSV file in this directory with the name:
```
netflix_titles.csv
```

## Dataset Structure

The dataset should contain the following columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| show_id | String | Unique ID for every Movie/TV Show |
| type | String | Identifier - A Movie or TV Show |
| title | String | Title of the Movie/TV Show |
| director | String | Director of the Movie |
| cast | String | Actors involved in the movie/show |
| country | String | Country where the movie/show was produced |
| date_added | String | Date it was added on Netflix |
| release_year | Integer | Actual Release year of the movie/show |
| rating | String | TV Rating of the movie/show |
| duration | String | Total Duration - in minutes or number of seasons |
| listed_in | String | Genre |
| description | String | The summary description |

## Data Statistics

- **Total Records:** ~8,800 titles
- **Time Period:** Content from 1925 to 2021
- **Geographic Coverage:** 100+ countries
- **Content Types:** Movies and TV Shows

## Data Preprocessing Notes

The raw data requires cleaning and preprocessing:

1. **Missing Values:** 
   - Director: ~30% missing
   - Cast: ~10% missing
   - Country: ~5% missing

2. **Data Transformations:**
   - Convert `date_added` to datetime format
   - Split multi-value columns (cast, country, listed_in)
   - Parse `duration` into numeric values

3. **Derived Features:**
   - Time lag between release and platform addition
   - Content age
   - Season count (for TV shows)
   - Runtime (for movies)

## Privacy & Ethics

This is publicly available aggregated data about content titles and does not contain any personally identifiable information (PII) or user viewing data.

## Data Quality

**Known Issues:**
- Some entries have incomplete metadata
- Multi-country productions listed under primary country only
- Genre classifications may overlap

**Recommended Cleaning Steps:**
1. Handle missing values appropriately
2. Standardize country names
3. Parse and normalize duration values
4. Extract year from date_added
5. Create binary flags for content types

## Usage Example

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('data/netflix_titles.csv')

# Basic exploration
print(df.shape)
print(df.info())
print(df.head())
```

## Additional Resources

For detailed data exploration and cleaning procedures, refer to:
- `notebooks/01_data_exploration.ipynb`
- `notebooks/02_data_cleaning.ipynb`

---

**Last Updated:** February 2026
