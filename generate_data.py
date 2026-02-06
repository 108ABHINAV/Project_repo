"""
Data Generator for India Crime Analysis
Creates realistic synthetic crime data based on NCRB patterns for demonstration purposes
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Indian cities
CITIES = [
    "Delhi", "Mumbai", "Bangalore", "Hyderabad", "Ahmedabad",
    "Chennai", "Kolkata", "Surat", "Pune", "Jaipur",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane",
    "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara"
]

# Crime categories based on NCRB classification
CRIME_TYPES = [
    "Murder", "Attempt to Murder", "Rape", "Kidnapping & Abduction",
    "Robbery", "Dacoity", "Burglary", "Theft", "Motor Vehicle Theft",
    "Riots", "Cheating", "Criminal Breach of Trust", "Hurt",
    "Assault on Women", "Dowry Deaths", "Cybercrime", 
    "Economic Offences", "Forgery", "Arson"
]

# City population estimates (in millions) - affects base crime rate
CITY_POPULATIONS = {
    "Delhi": 32.9, "Mumbai": 20.7, "Bangalore": 13.6, "Hyderabad": 10.5,
    "Ahmedabad": 8.4, "Chennai": 11.5, "Kolkata": 15.1, "Surat": 6.5,
    "Pune": 7.7, "Jaipur": 3.9, "Lucknow": 3.6, "Kanpur": 3.2,
    "Nagpur": 2.8, "Indore": 3.3, "Thane": 2.2, "Bhopal": 2.4,
    "Visakhapatnam": 2.2, "Pimpri-Chinchwad": 2.1, "Patna": 2.5, "Vadodara": 2.2
}

def generate_crime_data(start_date="2019-01-01", end_date="2024-12-31"):
    """
    Generate synthetic crime data for Indian cities
    
    Parameters:
    - start_date: Start date for data generation
    - end_date: End date for data generation
    
    Returns:
    - DataFrame with crime records
    """
    
    data = []
    
    # Generate date range
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    current_date = start
    
    while current_date <= end:
        year = current_date.year
        month = current_date.month
        
        for city in CITIES:
            population = CITY_POPULATIONS[city]
            
            # Base crime rate per 100,000 population (varies by city)
            base_rate = np.random.uniform(200, 600) * (population / 10)
            
            # Apply seasonal factors
            seasonal_factor = 1.0
            if month in [3, 4, 5]:  # Summer months - slightly higher
                seasonal_factor = 1.15
            elif month in [10, 11]:  # Festival season - variable
                seasonal_factor = np.random.uniform(0.9, 1.2)
            elif month in [12, 1]:  # Winter - slightly lower
                seasonal_factor = 0.95
                
            # Apply year-wise trend (slight increase over years)
            year_factor = 1 + (year - 2019) * 0.03
            
            # Weekend effect (weekends might have different patterns)
            # day_of_week = current_date.weekday()
            # weekend_factor = 1.1 if day_of_week >= 5 else 1.0
            
            for crime_type in CRIME_TYPES:
                # Crime type specific factors
                crime_factor = 1.0
                
                if crime_type in ["Murder", "Dacoity", "Dowry Deaths"]:
                    crime_factor = 0.05  # Rare crimes
                elif crime_type in ["Rape", "Kidnapping & Abduction", "Robbery"]:
                    crime_factor = 0.15  # Serious crimes - moderate
                elif crime_type in ["Theft", "Motor Vehicle Theft", "Burglary"]:
                    crime_factor = 0.4  # Common property crimes
                elif crime_type in ["Cybercrime"]:
                    crime_factor = 0.2 * (1 + (year - 2019) * 0.3)  # Increasing trend
                elif crime_type in ["Hurt", "Assault on Women", "Cheating"]:
                    crime_factor = 0.25
                else:
                    crime_factor = 0.1
                
                # Calculate number of incidents
                incidents = int(base_rate * seasonal_factor * year_factor * crime_factor)
                
                # Add random variation
                incidents = max(0, incidents + np.random.randint(-5, 6))
                
                # Calculate crime rate per 100,000 population
                crime_rate = (incidents / population) * 100
                
                data.append({
                    "Year": year,
                    "Month": month,
                    "Date": current_date.strftime("%Y-%m-%d"),
                    "City": city,
                    "State": get_state(city),
                    "Crime_Type": crime_type,
                    "Crime_Category": get_crime_category(crime_type),
                    "Incidents_Reported": incidents,
                    "Population_Lakhs": round(population * 10, 1),
                    "Crime_Rate_Per_100K": round(crime_rate, 2),
                    "Cases_Charge_Sheeted": int(incidents * np.random.uniform(0.6, 0.85)),
                    "Cases_Convicted": int(incidents * np.random.uniform(0.15, 0.35)),
                })
        
        # Move to next month
        if current_date.month == 12:
            current_date = datetime(current_date.year + 1, 1, 1)
        else:
            current_date = datetime(current_date.year, current_date.month + 1, 1)
    
    df = pd.DataFrame(data)
    return df

def get_state(city):
    """Map city to state"""
    state_mapping = {
        "Delhi": "Delhi", "Mumbai": "Maharashtra", "Bangalore": "Karnataka",
        "Hyderabad": "Telangana", "Ahmedabad": "Gujarat", "Chennai": "Tamil Nadu",
        "Kolkata": "West Bengal", "Surat": "Gujarat", "Pune": "Maharashtra",
        "Jaipur": "Rajasthan", "Lucknow": "Uttar Pradesh", "Kanpur": "Uttar Pradesh",
        "Nagpur": "Maharashtra", "Indore": "Madhya Pradesh", "Thane": "Maharashtra",
        "Bhopal": "Madhya Pradesh", "Visakhapatnam": "Andhra Pradesh",
        "Pimpri-Chinchwad": "Maharashtra", "Patna": "Bihar", "Vadodara": "Gujarat"
    }
    return state_mapping.get(city, "Unknown")

def get_crime_category(crime_type):
    """Categorize crime types"""
    if crime_type in ["Murder", "Attempt to Murder", "Rape", "Dowry Deaths"]:
        return "Violent Crimes"
    elif crime_type in ["Kidnapping & Abduction", "Robbery", "Dacoity"]:
        return "Crimes Against Person"
    elif crime_type in ["Burglary", "Theft", "Motor Vehicle Theft"]:
        return "Property Crimes"
    elif crime_type in ["Cybercrime", "Economic Offences", "Forgery", "Cheating", "Criminal Breach of Trust"]:
        return "Economic Crimes"
    elif crime_type in ["Assault on Women"]:
        return "Crimes Against Women"
    else:
        return "Other Crimes"

if __name__ == "__main__":
    print("Generating synthetic crime data for Indian cities...")
    
    # Generate data from 2019 to 2024
    df = generate_crime_data("2019-01-01", "2024-12-31")
    
    print(f"\nGenerated {len(df)} records")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"Cities: {df['City'].nunique()}")
    print(f"Crime types: {df['Crime_Type'].nunique()}")
    
    # Save to CSV
    output_path = "data/raw/india_crime_data_2019_2024.csv"
    df.to_csv(output_path, index=False)
    print(f"\nData saved to: {output_path}")
    
    # Display summary statistics
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    
    print("\nTotal crimes by year:")
    print(df.groupby("Year")["Incidents_Reported"].sum().sort_index())
    
    print("\nTop 5 cities by total crime count:")
    print(df.groupby("City")["Incidents_Reported"].sum().sort_values(ascending=False).head())
    
    print("\nTop 10 crime types by frequency:")
    print(df.groupby("Crime_Type")["Incidents_Reported"].sum().sort_values(ascending=False).head(10))
    
    print("\nCrime distribution by category:")
    print(df.groupby("Crime_Category")["Incidents_Reported"].sum().sort_values(ascending=False))
    
    print("\nSample data:")
    print(df.head(10))
