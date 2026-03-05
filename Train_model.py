import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import joblib

print("1. Loading Kenyan car data...")
df = pd.read_csv('kenya_used_cars_cleaned.csv')

X = df.drop(columns=['Selling_Price_KES'])
y = df['Selling_Price_KES']

print("2. Building the preprocessing rules...")
numerical_cols = ['Year', 'Mileage_km', 'Engine_Size_cc']
categorical_cols = ['Model', 'Fuel_Type', 'Transmission', 'Usage_Type']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

print("3. Training the Random Forest AI...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor), 
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

pipeline.fit(X_train, y_train)

print("4. Saving the Brain...")
joblib.dump(pipeline, 'kenya_car_price_model.pkl')
print("SUCCESS! 'kenya_car_price_model.pkl' has been created.")