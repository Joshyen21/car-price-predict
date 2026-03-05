import joblib
import pandas as pd

def predict_car():
    print("--- Car Price Estimator ---")
    try:
        model = joblib.load('kenya_car_price_model.pkl')
    except Exception as e:
        print("Error loading model. Did you run train_model.py first?")
        return

    # A sample car to test if it works
    sample_data = {
        'Model': ['Toyota Prado'],
        'Year': [2017],
        'Mileage_km': [85000],
        'Fuel_Type': ['Diesel'],
        'Transmission': ['Automatic'],
        'Usage_Type': ['Locally Used'],
        'Engine_Size_cc': [2700]
    }
    
    df = pd.DataFrame(sample_data)
    prediction = model.predict(df)[0]
    
    print(f"\n Vehicle: 2017 Toyota Prado (85k km)")
    print(f" Estimated Value: KES {prediction:,.2f}\n")

if __name__ == "__main__":
    predict_car()