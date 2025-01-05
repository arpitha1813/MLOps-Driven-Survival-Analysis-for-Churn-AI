# Use the official Python image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your requirements file into the container
COPY requirements.txt .

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .


# Add the dataset into the container
# Make sure the path to your dataset is correct
COPY telco-customer-churn-ibm-dataset/Telco_customer_churn.xlsx /app/dataset/Telco_customer_churn.xlsx

# Expose the port (optional, if you have a web service or app running)
EXPOSE 8081

# Set environment variables (optional, for debugging)
ENV PYTHONUNBUFFERED=1

# Run the tests when the container starts (you can customize this command)
CMD ["pytest", "--maxfail=1", "--disable-warnings", "--junitxml=test_report.xml"]

  
