import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Sample function for feature engineering
def feature_engineering(df):
    # Handle missing values (e.g., fill NaNs with median)
    df.fillna(df.median(), inplace=True)
    
    # Feature scaling (example: standardizing features)
    scaler = StandardScaler()
    df[['feature1', 'feature2']] = scaler.fit_transform(df[['feature1', 'feature2']])
    
    # Label encoding (example: converting categorical to numerical)
    le = LabelEncoder()
    df['category'] = le.fit_transform(df['category'])
    
    return df

@pytest.fixture
def load_data():
    # Load your actual dataset
    df = pd.read_excel("C:/Users/sindh/OneDrive/Desktop/MTech Sem-2/Customer Churn Analysis 4/telco-customer-churn-ibm-dataset/Telco_customer_churn.xlsx")  # Update with actual file path
    return df

def test_missing_value_imputation(load_data):
    df = load_data
    df_with_missing_values = df.copy()
    df_with_missing_values['Churn Score'] = None  # Introduce some missing values
    df_filled = feature_engineering(df_with_missing_values)
    assert df_filled['Churn Score'].isnull().sum() == 0, "Missing values in Churn Score were not handled."

def test_feature_scaling(load_data):
    df = load_data
    df_scaled = feature_engineering(df)
    # Check if the feature1 and feature2 are scaled (mean close to 0 and std close to 1)
    assert abs(df_scaled['Churn Score'].mean()) < 1e-1, "Feature1 scaling failed."
    assert abs(df_scaled['Churn Score'].std() - 1) < 1e-1, "Feature1 scaling (std) failed."
    

def test_label_encoding(load_data):
    df = load_data
    df_encoded = feature_engineering(df)
    # Check that the category column has been transformed to numerical values
    assert df_encoded['Tenure Months'].dtype == 'int64', "Label encoding failed for the 'category' column."
    assert df_encoded['Churn Value'].dtype == 'int64', "Label encoding failed for the 'category' column."
    assert df_encoded['Churn Score'].dtype == 'int64', "Label encoding failed for the 'category' column."
   

def test_feature_engineering_pipeline(load_data):
    df = load_data
    # Test if the entire pipeline runs without issues
    df_transformed = feature_engineering(df)
    
    
    
    # Check that 'category' column is label-encoded
    assert df_transformed['Churn Score'].dtype == 'int64', "Label encoding failed."
    
    # Ensure there are no missing values after feature engineering
    assert df_transformed.isnull().sum().sum() == 0, "There are missing values after feature engineering."

