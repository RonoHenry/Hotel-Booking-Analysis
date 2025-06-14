# 🏨 Hotel Booking Analysis

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-success)
![Data Status](https://img.shields.io/badge/data-cleaned-blue)
![Model Status](https://img.shields.io/badge/model-trained-green)
![Visuals](https://img.shields.io/badge/visualizations-created-orange)
![Analysis](https://img.shields.io/badge/analysis-creative-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📌 Project Overview

This project explores and models hotel booking behavior using the `hotel_bookings.csv` dataset (sourced from [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)). It focuses on:

- Understanding booking trends and cancellation patterns  
- Cleaning and preparing the dataset for analysis  
- Performing in-depth Exploratory Data Analysis (EDA)  
- Visualizing key business insights for stakeholders  
- Building a predictive model to forecast booking cancellations  


### 🎯 Objectives
- Understand cancellation rates by hotel type, market segment, and lead time.
- Identify key factors driving cancellations.
- Create professional-grade visualizations to share with stakeholders.
- Build and evaluate a machine learning model to predict cancellations.

### 📊 Dataset
- **Source**: `data/hotel_bookings.csv` (Kaggle Hotel Booking Demand dataset).
- **Key Columns**: `hotel`, `is_canceled`, `lead_time`, `children`, `country`, `adr`, `market_segment`, etc.

## 🛠️ Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/RonoHenry/Hotel-Booking-Analysis.git
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 🚀 Usage Instructions
1. **Data Preprocessing**:
   - Run the preprocessing script to clean and prepare the data:
     ```bash
     python src/preprocess.py
     ```
2. **Exploratory Data Analysis and Visualization**:
   - Open the notebook `Hotelbooking.ipynb` and execute the cells to perform EDA and generate visualizations.
3. **Model Training and Evaluation**:
   - Run the model training script:
     ```bash
     python src/model.py
     ```
   - Review the metrics and saved model in the `outputs/models` folder.

## 🔍 Key Insights
- **Cancellation Trends**: Resort hotels have higher cancellation rates compared to city hotels.
- **Lead Time**: Longer lead times are associated with higher cancellation rates.
- **Market Segment**: Online bookings show distinct cancellation patterns.

## 🌟 Future Improvements
- Enhance the predictive model with hyperparameter tuning.
- Deploy the model using a web application (e.g., Flask or Streamlit).
- Integrate additional datasets for deeper insights.
