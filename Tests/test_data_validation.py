import pandas as pd
import pytest

@pytest.fixture
def load_data():
    # Load the actual dataset (ensure the file path is correct)
    return pd.read_excel('C:\Users\sindh\OneDrive\Desktop\MTech Sem-2\
Customer Churn Analysis 4\telco-customer-churn-ibm-dataset\Telco_customer_churn.xlsx')

def test_missing_value_handling(load_data):
    # Test if missing values are handled
    assert load_data.isnull().sum().sum() > 0  # Check for missing values
    load_data_cleaned = load_data.dropna()  # Dropping missing values as an example of handling
    assert load_data_cleaned.isnull().sum().sum() == 0  # Check no missing values after cleaning

def test_column_names(load_data):
    # Test if required columns are present
    expected_columns = {'CustomerID', 'Count', 'Country', 'State', 'City', 'Zip Code',
       'Lat Long', 'Latitude', 'Longitude', 'Gender', 'Senior Citizen',
       'Partner', 'Dependents', 'Tenure Months', 'Phone Service',
       'Multiple Lines', 'Internet Service', 'Online Security',
       'Online Backup', 'Device Protection', 'Tech Support', 'Streaming TV',
       'Streaming Movies', 'Contract', 'Paperless Billing', 'Payment Method',
       'Monthly Charges', 'Total Charges', 'Churn Label', 'Churn Value',
       'Churn Score', 'CLTV', 'Churn Reason'}  # Update with your actual column names
    assert set(load_data.columns) == expected_columns

def test_data_types(load_data):
    # Test if columns have the correct data types
    assert load_data['Churn Score'].dtype == 'int64'  # Update with the expected data type
    assert load_data['Tenure Months'].dtype == 'int64'  # Example: checking integer column
    assert load_data['CLTV'].dtype == 'int64'
