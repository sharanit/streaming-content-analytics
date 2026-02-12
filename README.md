# 🎬 Streaming Content Analytics

> A comprehensive data analysis project exploring content strategies for streaming platforms using Netflix data

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Business Problem](#business-problem)
- [Dataset](#dataset)
- [Key Insights](#key-insights)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Highlights](#analysis-highlights)
- [Recommendations](#recommendations)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project analyzes a comprehensive dataset of movies and TV shows available on a major streaming platform to derive actionable business insights. The analysis focuses on content distribution patterns, geographical trends, genre preferences, and temporal dynamics to inform strategic decisions about content production and market expansion.

**Analysis Date:** February 2026  
**Dataset Period:** Mid-2021 (10,000+ titles, 222M+ subscribers globally)

## 💼 Business Problem

The streaming industry is highly competitive, with platforms constantly seeking to optimize their content libraries. This project addresses critical business questions:

1. **Content Strategy**: What types of shows and movies should be produced?
2. **Market Expansion**: How can the platform grow its business in different countries?
3. **Production Timing**: When is the optimal time to release content?
4. **Resource Allocation**: Which directors, actors, and genres yield the best ROI?

## 📊 Dataset

The dataset comprises comprehensive information about streaming content:

| Feature | Description |
|---------|-------------|
| `show_id` | Unique identifier for each title |
| `type` | Content type (Movie or TV Show) |
| `title` | Name of the content |
| `director` | Director(s) of the content |
| `cast` | Main actors/actresses |
| `country` | Country of production |
| `date_added` | Date added to platform |
| `release_year` | Original release year |
| `rating` | Age/content rating |
| `duration` | Runtime (minutes) or number of seasons |
| `listed_in` | Genre categories |
| `description` | Brief synopsis |

**Dataset Size:** 10,000+ entries  
**Time Range:** Multiple decades of content

## 🔑 Key Insights

### Content Distribution
- **72%** of the catalog consists of movies vs. 28% TV shows
- Sharp increase in content additions post-2010 (expansion phase)
- Peak content releases around 2018

### Geographic Patterns
- **Top 3 Production Countries:**
  1. United States (dominant across all genres)
  2. India (strong in International Movies & Dramas)
  3. United Kingdom (notable in British TV Shows)

### Genre Analysis
- **Most Popular Genres:**
  1. Dramas
  2. International Movies
  3. Comedies

### Regional Specialization
- **Japan:** Anime Series & International TV Shows
- **South Korea:** Korean TV Shows, Romantic TV Shows, TV Dramas
- **India:** Bollywood content, International Movies

### Temporal Trends
- **Best Launch Months:** July shows highest content addition
- **Best Launch Day:** Friday preferred for new releases
- **Content Lag:** Significant delay between release year and platform addition

### Audience Targeting
- **Top Ratings:** TV-MA, TV-14, R (mature audience focus)
- **TV Show Duration:** Majority have 1-3 seasons

## 📁 Project Structure

```
streaming-content-analytics/
│
├── data/
│   └── README.md                    # Data source information
│
├── notebooks/
│   ├── 01_data_exploration.ipynb    # Initial data exploration
│   ├── 02_data_cleaning.ipynb       # Data preprocessing
│   ├── 03_eda_analysis.ipynb        # Exploratory Data Analysis
│   └── 04_insights_visualization.ipynb  # Final visualizations
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py           # Data cleaning functions
│   ├── visualization.py             # Plotting functions
│   └── analysis.py                  # Analysis utilities
│
├── reports/
│   ├── figures/                     # Generated visualizations
│   └── business_insights.md         # Detailed findings
│
├── requirements.txt                 # Python dependencies
├── .gitignore                      # Git ignore file
├── LICENSE                         # MIT License
└── README.md                       # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/sharanit/streaming-content-analytics.git
cd streaming-content-analytics
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download the dataset**
- Place the Netflix dataset CSV file in the `data/` directory
- Refer to `data/README.md` for data source information

## 💻 Usage

### Running the Analysis

1. **Start Jupyter Notebook**
```bash
jupyter notebook
```

2. **Execute notebooks in order**
   - Start with `01_data_exploration.ipynb`
   - Follow through the numbered sequence
   - Each notebook builds on the previous analysis

3. **Generate visualizations**
```python
from src.visualization import create_content_distribution_plot
create_content_distribution_plot(df)
```

### Quick Start Example

```python
import pandas as pd
from src.data_processing import load_and_clean_data
from src.analysis import get_top_genres

# Load data
df = load_and_clean_data('data/netflix_titles.csv')

# Quick analysis
top_genres = get_top_genres(df, n=10)
print(top_genres)
```

## 📈 Analysis Highlights

### 1. Content Type Analysis
- Visual comparison of Movies vs. TV Shows
- Temporal trends in content production
- Genre distribution across content types

### 2. Geographic Intelligence
- Country-wise content contribution
- Regional genre preferences
- Market saturation analysis

### 3. Temporal Patterns
- Year-over-year content growth
- Seasonal addition patterns
- Release timing optimization

### 4. Talent Analytics
- Top directors by content volume
- Most featured actors
- Director-genre specialization

### 5. Audience Segmentation
- Rating distribution analysis
- Duration preferences
- Genre-audience alignment

## 🎯 Recommendations

### Strategic Initiatives

#### 1. Content Production Strategy
- **Increase TV Show Production**: Recent data shows growing focus on serialized content
- **Focus on Mature Content**: TV-MA and TV-14 ratings dominate the catalog
- **Short-Season Format**: Prioritize 1-3 season shows for faster ROI

#### 2. Geographic Expansion
- **India**: Invest heavily in Bollywood content and International Dramas
- **South Korea**: Expand Korean drama and romantic series catalog
- **Japan**: Strengthen anime and international show offerings
- **UK**: Develop more British TV shows and international content

#### 3. Genre Optimization
- **Double down on Dramas**: Most popular across all regions
- **International Content**: High demand for cross-border productions
- **Comedy**: Consistent performer across demographics

#### 4. Launch Timing
- **Optimal Release Month**: July for maximum visibility
- **Preferred Day**: Friday releases capture weekend viewership
- **Content Planning**: Account for 12-24 month lag between production and release

#### 5. Talent Acquisition
- **Partner with prolific directors**: Focus on Martin Scorsese, Steven Spielberg caliber
- **Multi-region actors**: Prioritize talent with cross-market appeal
- **Emerging markets**: Invest in Indian and Korean talent for regional growth

### Tactical Actions

1. **Q1-Q2**: Develop content pipeline for July releases
2. **Q2-Q3**: Expand partnerships in India, South Korea, and Japan
3. **Q3-Q4**: Launch 3-5 new drama series (1-2 seasons each)
4. **Ongoing**: Monitor genre trends and adjust production quarterly

## 🛠 Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical data visualization
- **Plotly**: Interactive visualizations
- **WordCloud**: Text analysis and visualization
- **Jupyter**: Interactive development environment

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/sharanit)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/sharanvora)

## 🙏 Acknowledgments

- Dataset provided by Netflix public data
- Inspiration from streaming platform analytics
- Community contributions and feedback

---

⭐ If you found this project helpful, please consider giving it a star!

**Last Updated:** February 2026
