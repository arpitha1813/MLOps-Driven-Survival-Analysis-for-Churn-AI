MLOps-Driven Survival Analysis for Churn AI combines survival analysis, AI, and MLOps practices to predict customer churn and segment customers based on risk. 
This project provides valuable insights into customer lifetimes and helps businesses develop targeted retention strategies. By using machine learning models, 
we can predict when customers are likely to leave and segment them accordingly. The MLOps integration ensures that models are scalable, automated, and efficiently deployed.

Features
Survival Analysis: Predicts the time until churn for each customer based on historical data.
Customer Segmentation: Classifies customers into different segments based on churn risk (e.g., high-risk vs. low-risk).
AI & ML: Uses machine learning models for churn prediction and customer lifetime analysis.
MLOps: Ensures efficient model deployment, monitoring, and automation through MLOps pipelines.
Automated Predictions using web app: Predict churn likelihood using input data for future customer behavior analysis.
 
Requirements
Python 3.6+
Required libraries:
scikit-learn
pandas
matplotlib
seaborn
mlflow
joblib
streamlit

1. Data Collection and Preprocessing
Data Collection: Customer data (e.g., demographics, usage history, engagement) is gathered from kaggle.
Preprocessing: Raw data is cleaned and transformed into a format suitable for modeling, including handling missing values, encoding categorical features, and scaling numerical features.
2. Feature Engineering
Feature Selection: Identify and select the most relevant features that impact churn prediction.
Feature Creation: New features may be derived from existing data.
3. Model Development
Model Selection: Choose appropriate machine learning algorithms for survival analysis and churn prediction. For example, Cox Proportional Hazards Model for survival analysis.
We have used Ensemble model which includes Logistic Regression,Random Forest, XGBoost model. Voting Classifier is used for prediction.
Model Training: The selected model is trained on the preprocessed data to learn patterns and predict churn likelihood.
5. Model Evaluation
Performance Metrics: Evaluate the model using metrics like accuracy,f1,precision and do survival analysis. Hyperparameter tuning is also  performed during this phase.
Cross-Validation: Ensure the model generalizes well across different subsets of data by using techniques like cross-validation.
6. Model Deployment
Model Packaging: Once the model is trained and evaluated, it is saved (e.g., using joblib).
Model Deployment: Deploy the model to production using  web app (e.g., Streamlit) making it accessible for real-time predictions.
7. Monitoring and Maintenance
Model Monitoring: Continuously monitor the model’s performance over time to ensure it still performs well as new data arrives.
Model Retraining: If the model’s performance drops (due to concept drift or changes in customer behavior), it is retrained with new data to maintain accuracy.
8. MLOps Integration
Pipeline Automation: The entire ML lifecycle (from training to deployment) is automated using MLOps pipelines, ensuring scalability and consistency.
Versioning: Keep track of model versions, code changes, and datasets to ensure reproducibility and transparency.
Collaboration: Multiple team members can collaborate efficiently on model development, deployment, and maintenance through version control and CI/CD integration.



