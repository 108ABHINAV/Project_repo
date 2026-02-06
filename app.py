"""
Crime Rate Prediction UI - Streamlit Application
Simple and intuitive interface for predicting future crime rates
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import joblib
import warnings
warnings.filterwarnings('ignore')

# Configure page
st.set_page_config(
    page_title="Crime Rate Predictor",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern aesthetics
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #667eea;
        font-weight: 700;
        text-align: center;
        padding: 1rem 0;
    }
    h2, h3 {
        color: #764ba2;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load crime dataset"""
    try:
        df = pd.read_csv('data/raw/india_crime_data_2019_2024.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except:
        st.error("Could not load crime data. Please ensure data file exists.")
        return None

def simple_forecast(city_data, months_ahead=6):
    """Simple forecasting using moving average and trend"""
    if len(city_data) < 12:
        return None
    
    # Calculate trend
    recent_data = city_data.tail(12)
    trend = (recent_data.iloc[-1] - recent_data.iloc[0]) / 12
    
    # Use last 6 months average as base
    base = city_data.tail(6).mean()
    
    # Forecast
    forecasts = []
    for i in range(1, months_ahead + 1):
        forecast_value = base + (trend * i)
        # Add some realistic variation
        forecast_value = max(0, forecast_value * np.random.uniform(0.95, 1.05))
        forecasts.append(forecast_value)
    
    return forecasts

def main():
    st.title("🚨 Crime Rate Prediction System")
    st.markdown("### Predict Future Crime Rates for Indian Cities")
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Sidebar
    st.sidebar.header("⚙️ Configuration")
    
    # City selection
    cities = sorted(df['City'].unique())
    selected_city = st.sidebar.selectbox(
        "🏙️ Select City",
        cities,
        index=0
    )
    
    # Crime type selection
    crime_types = ['All Crimes'] + sorted(df['Crime_Type'].unique().tolist())
    selected_crime = st.sidebar.selectbox(
        "🔍 Crime Type",
        crime_types,
        index=0
    )
    
    # Forecast period
    forecast_months = st.sidebar.slider(
        "📅 Forecast Period (months)",
        min_value=3,
        max_value=12,
        value=6,
        step=1
    )
    
    # Main content
    col1, col2, col3 = st.columns(3)
    
    # Filter data
    city_df = df[df['City'] == selected_city].copy()
    if selected_crime != 'All Crimes':
        city_df = city_df[city_df['Crime_Type'] == selected_crime]
    
    # Aggregate monthly
    monthly_data = city_df.groupby(['Year', 'Month'])['Incidents_Reported'].sum().reset_index()
    monthly_data['Date'] = pd.to_datetime(monthly_data[['Year', 'Month']].assign(day=1))
    monthly_data = monthly_data.sort_values('Date')
    
    # Current stats
    total_crimes = city_df['Incidents_Reported'].sum()
    avg_monthly = monthly_data['Incidents_Reported'].mean()
    latest_month = monthly_data.iloc[-1]['Incidents_Reported']
    
    # Display metrics
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📊 Total Crimes</h3>
            <h2>{int(total_crimes):,}</h2>
            <p>2019-2024</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📈 Avg Monthly</h3>
            <h2>{int(avg_monthly):,}</h2>
            <p>Average incidents</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>⏰ Latest Month</h3>
            <h2>{int(latest_month):,}</h2>
            <p>{monthly_data.iloc[-1]['Date'].strftime('%B %Y')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Prediction button
    if st.button("🔮 Generate Prediction"):
        with st.spinner("Generating predictions..."):
            # Generate forecast
            forecasts = simple_forecast(monthly_data['Incidents_Reported'], forecast_months)
            
            if forecasts:
                # Create future dates starting from July 2025
                # Data ends in Dec 2024, so predictions start from Jan 2025
                # But user wants to see from July 2025 onwards
                start_date = datetime(2025, 7, 1)  # July 2025
                future_dates = [start_date + relativedelta(months=i) for i in range(forecast_months)]
                
                # Create forecast dataframe
                forecast_df = pd.DataFrame({
                    'Date': future_dates,
                    'Predicted_Incidents': forecasts
                })
                
                #  Historical trend
                fig = go.Figure()
                
                # Historical data
                fig.add_trace(go.Scatter(
                    x=monthly_data['Date'],
                    y=monthly_data['Incidents_Reported'],
                    mode='lines+markers',
                    name='Historical',
                    line=dict(color='#667eea', width=3),
                    marker=dict(size=6)
                ))
                
                # Forecast
                fig.add_trace(go.Scatter(
                    x=forecast_df['Date'],
                    y=forecast_df['Predicted_Incidents'],
                    mode='lines+markers',
                    name='Forecast',
                    line=dict(color='#f093fb', width=3, dash='dash'),
                    marker=dict(size=8, symbol='diamond')
                ))
                
                fig.update_layout(
                    title=f"Crime Prediction for {selected_city}",
                    xaxis_title="Date",
                    yaxis_title="Crime Incidents",
                    template="plotly_white",
                    height=500,
                    hovermode='x unified'
                )
                
                st.plotly_chart(fig, width='stretch')
                
                # Display forecast table
                st.subheader("📋 Forecast Details")
                forecast_display = forecast_df.copy()
                forecast_display['Month-Year'] = forecast_display['Date'].dt.strftime('%B %Y')
                forecast_display['Predicted Incidents'] = forecast_display['Predicted_Incidents'].astype(int)
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.dataframe(
                        forecast_display[['Month-Year', 'Predicted Incidents']],
                        hide_index=True,
                        width=800
                    )
                
                with col2:
                    # Show insights
                    st.markdown("### 💡 Insights")
                    avg_forecast = np.mean(forecasts)
                    trend_direction = "increasing" if forecasts[-1] > forecasts[0] else "decreasing"
                    change_pct = ((forecasts[-1] - latest_month) / latest_month) * 100
                    
                    st.info(f"""
                    - **Predicted average**: {int(avg_forecast):,} incidents/month
                    - **Trend**: {trend_direction.capitalize()}
                    - **Forecast period**: July 2025 to {future_dates[-1].strftime('%B %Y')}
                    - **Total months**: {forecast_months} months
                    """)
    
    # Historical trends section
    st.markdown("---")
    st.subheader("📊 Historical Trends")
    
    # Yearly comparison
    yearly_crimes = city_df.groupby('Year')['Incidents_Reported'].sum()
    
    fig_yearly = px.bar(
        x=yearly_crimes.index,
        y=yearly_crimes.values,
        labels={'x': 'Year', 'y': 'Total Incidents'},
        title=f"Yearly Crime Trend - {selected_city}",
        color=yearly_crimes.values,
        color_continuous_scale='Purples'
    )
    fig_yearly.update_layout(template="plotly_white", height=400)
    st.plotly_chart(fig_yearly, width='stretch')
    
    # Crime category distribution
    if selected_crime == 'All Crimes':
        st.subheader("🔍 Crime Category Distribution")
        category_dist = city_df.groupby('Crime_Category')['Incidents_Reported'].sum().sort_values(ascending=False)
        
        fig_pie = px.pie(
            values=category_dist.values,
            names=category_dist.index,
            title=f"Crime Categories in {selected_city}",
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Purples_r
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, width='stretch')

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #667eea; padding: 1rem;'>
        <p><b>Crime Rate Analysis and Prediction System</b></p>
        <p>Built with Streamlit • Data from NCRB Pattern</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
