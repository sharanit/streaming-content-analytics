# Analysis Notebooks

This directory contains Jupyter notebooks for the streaming content analytics project.

## Notebook Sequence

Execute the notebooks in the following order for best results:

### 1. `01_data_exploration.ipynb`
**Purpose:** Initial data exploration and understanding

**Contents:**
- Load and inspect raw data
- Check data types and structure
- Identify missing values
- Generate statistical summaries
- Document initial findings

**Output:** Understanding of data quality and structure

---

### 2. `02_data_cleaning.ipynb`
**Purpose:** Data preprocessing and cleaning

**Contents:**
- Handle missing values
- Parse and convert data types
- Explode multi-value columns (cast, director, country)
- Create derived features
- Standardize formats

**Output:** Clean, analysis-ready dataset

---

### 3. `03_eda_analysis.ipynb`
**Purpose:** Comprehensive exploratory data analysis

**Contents:**
- Univariate analysis (distributions, frequencies)
- Bivariate analysis (relationships, correlations)
- Content type analysis (Movies vs TV Shows)
- Geographic analysis
- Temporal trends
- Genre patterns
- Rating distributions

**Output:** Statistical insights and patterns

---

### 4. `04_insights_visualization.ipynb`
**Purpose:** Final visualizations and business insights

**Contents:**
- Create publication-quality visualizations
- Generate interactive plots
- Synthesize findings
- Derive business recommendations
- Create executive summary

**Output:** Business insights and recommendations

---

## How to Use

### Prerequisites
```bash
# Install dependencies
pip install -r ../requirements.txt
```

### Running the Notebooks

1. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Open notebooks in sequence**
   - Begin with `01_data_exploration.ipynb`
   - Progress through each notebook
   - Review outputs before proceeding

3. **Execute all cells**
   - Use "Run All" for complete execution
   - Or run cells individually for detailed review

### Using the Source Modules

The notebooks can leverage pre-built functions from the `src/` directory:

```python
# Import custom modules
import sys
sys.path.append('../src')

from data_processing import load_and_clean_data
from visualization import create_content_distribution_plot
from analysis import get_top_genres

# Use functions
df = load_and_clean_data('../data/netflix_titles.csv')
create_content_distribution_plot(df)
top_genres = get_top_genres(df)
```

## Notebook Structure

Each notebook follows this structure:

1. **Introduction**
   - Objective
   - Context
   - Expected outcomes

2. **Setup**
   - Imports
   - Configuration
   - Data loading

3. **Analysis**
   - Exploratory code
   - Visualizations
   - Statistical tests

4. **Findings**
   - Key insights
   - Patterns observed
   - Anomalies noted

5. **Conclusions**
   - Summary
   - Next steps
   - Recommendations

## Tips for Best Results

### Code Quality
- ✅ Comment your code
- ✅ Use meaningful variable names
- ✅ Break complex operations into steps
- ✅ Document assumptions

### Visualizations
- ✅ Use consistent color schemes
- ✅ Add clear titles and labels
- ✅ Include legends where appropriate
- ✅ Save important plots

### Analysis
- ✅ State your hypothesis
- ✅ Show your work
- ✅ Interpret results
- ✅ Connect to business questions

### Documentation
- ✅ Use markdown cells
- ✅ Explain your reasoning
- ✅ Document key findings
- ✅ Highlight insights

## Common Issues and Solutions

### Issue: Kernel won't start
**Solution:** Check Python version and dependencies
```bash
python --version  # Should be 3.8+
pip install -r requirements.txt
```

### Issue: Module not found
**Solution:** Ensure correct path to src/
```python
import sys
sys.path.append('../src')
```

### Issue: Data file not found
**Solution:** Verify data file location
```python
import os
print(os.path.exists('../data/netflix_titles.csv'))
```

### Issue: Memory error with large plots
**Solution:** Reduce data size or use sampling
```python
df_sample = df.sample(n=1000, random_state=42)
```

## Exporting Notebooks

### Export to HTML
```bash
jupyter nbconvert --to html notebook_name.ipynb
```

### Export to PDF
```bash
jupyter nbconvert --to pdf notebook_name.ipynb
```

### Export to Python Script
```bash
jupyter nbconvert --to script notebook_name.ipynb
```

## Additional Resources

- **Pandas Documentation:** https://pandas.pydata.org/docs/
- **Matplotlib Gallery:** https://matplotlib.org/stable/gallery/
- **Seaborn Tutorial:** https://seaborn.pydata.org/tutorial.html
- **Plotly Examples:** https://plotly.com/python/

---

**Happy Analyzing! 📊**
