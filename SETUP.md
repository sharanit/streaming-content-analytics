# Project Setup Guide

Complete guide to setting up the Streaming Content Analytics project on your local machine.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Data Setup](#data-setup)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software

1. **Python 3.8 or higher**
   ```bash
   # Check your Python version
   python --version
   # or
   python3 --version
   ```

2. **pip (Python package manager)**
   ```bash
   # Check pip version
   pip --version
   ```

3. **Git** (for cloning the repository)
   ```bash
   # Check Git version
   git --version
   ```

4. **Jupyter Notebook or JupyterLab**
   ```bash
   # Will be installed with requirements
   ```

### Recommended Software

- **Virtual environment tool** (venv, conda, or virtualenv)
- **VS Code** or **PyCharm** for code editing
- **GitHub Desktop** (optional, for easier Git management)

---

## Installation

### Step 1: Clone the Repository

```bash
# Using HTTPS
git clone https://github.com/sharanit/streaming-content-analytics.git

# Or using SSH
git clone git@github.com:sharanit/streaming-content-analytics.git

# Navigate to project directory
cd streaming-content-analytics
```

### Step 2: Create Virtual Environment

**Option A: Using venv (recommended)**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

**Option B: Using conda**
```bash
# Create conda environment
conda create -n streaming-analytics python=3.8

# Activate environment
conda activate streaming-analytics
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 4: Install Project as Package (Optional)

```bash
# Install in development mode
pip install -e .

# This allows you to import from src/ anywhere
```

---

## Data Setup

### Step 1: Obtain Dataset

The dataset is not included in the repository due to size constraints.

**Option A: Download from Kaggle**
1. Go to [Kaggle Netflix Dataset](https://www.kaggle.com/)
2. Search for "Netflix Movies and TV Shows"
3. Download the CSV file

**Option B: Use Alternative Source**
- Search for "Netflix titles dataset" 
- Ensure it has the required columns (see data/README.md)

### Step 2: Place Dataset in Project

```bash
# Create data directory if it doesn't exist
mkdir -p data

# Move downloaded file to data directory
mv ~/Downloads/netflix_titles.csv data/

# Verify file exists
ls -lh data/netflix_titles.csv
```

### Step 3: Verify Data Format

```bash
# Quick check using Python
python -c "import pandas as pd; df = pd.read_csv('data/netflix_titles.csv'); print(df.shape)"
```

Expected output: `(~8800, 12)` or similar

---

## Verification

### Verify Installation

**1. Check Python Environment**
```bash
# Should show your virtual environment path
which python  # macOS/Linux
where python  # Windows
```

**2. Test Imports**
```python
# Run Python interactive shell
python

# Test imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("✓ All imports successful")
exit()
```

**3. Test Jupyter**
```bash
# Start Jupyter Notebook
jupyter notebook

# Or JupyterLab
jupyter lab
```

### Verify Project Structure

```bash
# Check directory structure
tree -L 2  # macOS/Linux with tree installed

# Or list directories
ls -R
```

Expected structure:
```
streaming-content-analytics/
├── data/
├── notebooks/
├── src/
├── reports/
├── README.md
├── requirements.txt
└── ...
```

### Run Quick Test

```bash
# Test data loading
python -c "
from src.data_processing import load_data
df = load_data('data/netflix_titles.csv')
print(f'✓ Data loaded: {df.shape}')
"
```

---

## Troubleshooting

### Common Issues

#### Issue 1: Python Version Error
```
ERROR: Python 3.8 or higher required
```

**Solution:**
```bash
# Install Python 3.8+ from python.org
# Or use pyenv to manage versions
pyenv install 3.8.0
pyenv local 3.8.0
```

#### Issue 2: pip Installation Fails
```
ERROR: Could not install packages due to an EnvironmentError
```

**Solution:**
```bash
# Try with --user flag
pip install --user -r requirements.txt

# Or upgrade pip first
python -m pip install --upgrade pip
```

#### Issue 3: Jupyter Kernel Not Found
```
ERROR: Kernel not found
```

**Solution:**
```bash
# Install ipykernel
pip install ipykernel

# Add kernel to Jupyter
python -m ipykernel install --user --name=streaming-analytics
```

#### Issue 4: Module Import Errors
```
ModuleNotFoundError: No module named 'src'
```

**Solution:**
```python
# Add to top of notebook
import sys
sys.path.append('../src')
```

#### Issue 5: Data File Not Found
```
FileNotFoundError: data/netflix_titles.csv
```

**Solution:**
```bash
# Check file location
ls data/

# Verify path in code
pwd  # Print working directory
```

#### Issue 6: Memory Error with Large Dataset
```
MemoryError: Unable to allocate array
```

**Solution:**
```python
# Use chunking for large files
chunks = pd.read_csv('data/netflix_titles.csv', chunksize=1000)
df = pd.concat(chunks, ignore_index=True)
```

### Platform-Specific Issues

#### macOS
- Install Xcode Command Line Tools: `xcode-select --install`
- Use Homebrew for Python: `brew install python@3.8`

#### Windows
- Use Anaconda distribution for easier setup
- Add Python to PATH during installation
- Use Git Bash or WSL for Unix commands

#### Linux
- Install Python dev packages: `sudo apt-get install python3-dev`
- Install build essentials: `sudo apt-get install build-essential`

---

## Next Steps

After successful setup:

1. ✅ **Explore the notebooks**
   ```bash
   cd notebooks
   jupyter notebook
   ```

2. ✅ **Read the documentation**
   - Review `README.md`
   - Check `CASE_STUDY.md`
   - Read `data/README.md`

3. ✅ **Run the analysis**
   - Start with `01_data_exploration.ipynb`
   - Follow the numbered sequence

4. ✅ **Customize and extend**
   - Add your own analysis
   - Create new visualizations
   - Derive additional insights

---

## Getting Help

If you encounter issues:

1. **Check Documentation**
   - README.md
   - This SETUP.md file
   - Individual notebook READMEs

2. **Search Issues**
   - GitHub Issues page
   - Stack Overflow
   - Python/Pandas forums

3. **Create Issue**
   - Provide error messages
   - Include system information
   - Show what you've tried

4. **Community Support**
   - Python Discord servers
   - r/learnpython subreddit
   - Data science communities

---

## Additional Configuration

### VS Code Setup

```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black"
}
```

### Jupyter Extensions

```bash
# Install useful extensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

### Git Configuration

```bash
# Set up Git ignore
cp .gitignore.example .gitignore

# Configure Git
git config --local user.name "Shran"
git config --local user.email "haranvoracareers@gmail.com"
```

---

**Setup Complete! Happy Analyzing! 🎉**
