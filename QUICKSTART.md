# Quick Start Guide

This guide helps you get the Crime Rate Analysis and Prediction system running quickly.

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

1. **Navigate to project directory:**
   ```bash
   cd d:/5-Projects/Grad_Final
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Applications

### 1. Generate Data (First Time Only)

If crime data doesn't exist, generate it:
```bash
python generate_data.py
```

This creates synthetic crime data for 20 Indian cities (2019-2024).

### 2. Run Jupyter Notebooks

Explore and analyze data:
```bash
jupyter notebook
```

Then open notebooks in order:
- `01_data_acquisition.ipynb` - Load and inspect data
- `02_eda.ipynb` - Exploratory analysis
- `03_preprocessing.ipynb` - Data preprocessing
- `04_time_series_models.ipynb` - Time series models

### 3. Launch Prediction UI

Start the Streamlit web application:
```bash
streamlit run app.py
```

Access at: **http://localhost:8501**

Features:
- Select city and crime type
- Set forecast period (3-12 months)
- Generate predictions **starting from July 2025**
- View historical trends (2019-2024)
- Interactive visualizations

## Troubleshooting

### Port Already in Use

If port 8501 is in use:

**For Streamlit:**
```bash
streamlit run app.py --server.port 8502
```

### Missing Data

If you see "Data file not found":
```bash
python generate_data.py
```

### Module Not Found Errors

Reinstall dependencies:
```bash
pip install -r requirements.txt --upgrade
```

## Quick Demo

1. Generate data: `python generate_data.py`
2. Start UI: `streamlit run app.py`
3. Select "Delhi" city
4. Choose "All Crimes"
5. Set forecast to 6 months
6. Click "Generate Prediction"
7. View predictions from **July 2025 to December 2025**

## Project Structure

```
Grad_Final/
├── data/               # Crime datasets
├── notebooks/          # Analysis notebooks
├── src/               # Python modules
├── models/            # Saved ML models
├── app.py             # Prediction UI
└── requirements.txt   # Dependencies
```

## Next Steps

- Explore notebooks for detailed analysis
- Try different cities and crime types
- Adjust forecast periods
- Filter dashboard by state/category
- Export data and predictions

## Support

For issues, check:
1. Python version (3.8+)
2. All dependencies installed
3. Data files exist in `data/raw/`
4. No port conflicts

Enjoy analyzing crime trends! 🚨
