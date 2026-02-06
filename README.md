# Crime Rate Analysis and Prediction

A comprehensive data-driven system to analyze historical crime data and predict future crime rates for Indian cities using multiple machine learning techniques.

## 🎯 Project Overview

This project analyzes NCRB (National Crime Records Bureau) crime data to identify patterns, trends, and crime-influencing factors across major Indian cities. It employs various machine learning approaches to forecast future crime rates and provides insights to support proactive decision-making for public safety and policy planning.

## ✨ Features

- **Multi-Model Approach**: Time series forecasting (ARIMA, Prophet, LSTM), regression (Random Forest, XGBoost), and classification models
- **Interactive UI**: Simple web interface for crime rate predictions
- **Jupyter Notebooks**: Complete analysis pipeline from data acquisition to model evaluation
- **Indian Cities Focus**: Specialized analysis for 20+ major Indian cities

## 📊 Deliverables

1. **Data Analysis Notebooks** (7 notebooks):
   - Data acquisition and exploration
   - Exploratory data analysis (EDA)
   - Data preprocessing and feature engineering
   - Time series models (ARIMA, Prophet, LSTM)
   - Regression models (Random Forest, XGBoost)
   - Classification models
   - Model comparison and evaluation

2. **Prediction UI** (Streamlit):
   - City-wise crime rate predictions
   - Model selection and comparison
   - Interactive visualizations
   - Batch prediction capabilities

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
cd d:/5-Projects/Grad_Final

# Install dependencies
pip install -r requirements.txt

# Generate crime data (first time only)
python generate_data.py
```

### Usage

#### 1. Run Jupyter Notebooks

```bash
jupyter notebook
```

Navigate to the `notebooks/` folder and run notebooks in order (01-07).

#### 2. Launch Prediction UI

```bash
streamlit run app.py
```

Access the UI at `http://localhost:8501`

## 📁 Project Structure

```
Grad_Final/
├── data/
│   ├── raw/              # Original datasets
│   ├── processed/        # Cleaned data
│   └── external/         # Additional reference data
├── notebooks/
│   ├── 01_data_acquisition.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_time_series_models.ipynb
│   ├── 05_regression_models.ipynb
│   ├── 06_classification_models.ipynb
│   └── 07_model_evaluation.ipynb
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── predictor.py
│   ├── utils.py
│   └── models/
│       ├── arima_model.py
│       ├── prophet_model.py
│       ├── lstm_model.py
│       ├── rf_model.py
│       └── xgb_model.py
├── models/               # Saved trained models
├── tests/                # Unit tests
├── app.py               # Streamlit UI
├── config.py            # Configuration settings
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## 🛠️ Technologies Used

- **Data Analysis**: Pandas, NumPy, Scipy
- **Visualization**: Matplotlib, Seaborn, Plotly, Folium
- **Machine Learning**: Scikit-learn, XGBoost, Statsmodels, Prophet
- **Deep Learning**: TensorFlow
- **Web Framework**: Streamlit
- **Geospatial**: GeoPandas

## 📈 Models

### Time Series Forecasting
- **ARIMA**: For linear temporal patterns
- **Prophet**: Seasonal decomposition with Indian holidays
- **LSTM**: Complex non-linear pattern recognition

### Regression
- **Random Forest**: Feature importance analysis
- **XGBoost**: High-accuracy gradient boosting

### Classification
- Crime type prediction
- High/low crime rate zone classification

## 📊 Data Sources

- NCRB (National Crime Records Bureau) via data.gov.in
- State/UT-wise IPC crimes (2020-2022)
- Metro city-wise crime statistics
- Crimes against women and children

## 🎯 Key Insights

The analysis identifies:
- Temporal crime patterns (seasonal, monthly trends)
- Geographic crime hotspots across Indian cities
- Crime-influencing factors
- Future crime rate predictions with confidence intervals
- High-risk periods and locations

## 📝 License

This project is for educational and research purposes.

## 👨‍💻 Author

**Duration**: 3 Months  
**Platform**: Python

---

Built with ❤️ for safer cities
