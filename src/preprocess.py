import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(df):
    """Clean hotel bookings data."""
    try:
        logging.info("Cleaning data...")
        df['children'] = df['children'].fillna(df['children'].median())
        df['country'] = df['country'].fillna('Unknown')
        df['agent'] = df['agent'].fillna(0)
        df['company'] = df['company'].fillna(0)
        df = df.drop(columns=['reservation_status'], errors='ignore')
        logging.info("Data cleaned successfully.")
        return df
    except Exception as e:
        logging.error(f"Error in clean_data: {e}")
        raise

def engineer_features(df):
    """Add derived features."""
    try:
        logging.info("Engineering features...")
        df['total_stay'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
        df['total_guests'] = df['adults'] + df['children'] + df['babies']
        df['is_long_lead'] = (df['lead_time'] > 90).astype(int)
        logging.info("Features engineered successfully.")
        return df
    except Exception as e:
        logging.error(f"Error in engineer_features: {e}")
        raise

# Save processed data
if __name__ == "__main__":
    try:
        logging.info("Starting preprocessing...")
        df = pd.read_csv('data/raw/hotel_bookings.csv')
        df_clean = clean_data(df)
        df_clean = engineer_features(df_clean)
        df_clean.to_csv('data/processed/hotel_bookings_clean.csv', index=False)
        logging.info("Preprocessing completed and data saved.")
    except Exception as e:
        logging.error(f"Error in preprocessing: {e}")
        raise