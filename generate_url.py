import pandas as pd

# URL of the dataset
dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/creditcard.csv"  # Replace with your actual dataset URL

# Load the dataset from the URL
df = pd.read_csv(dataset_url)

# Drop the "Class" column to get only feature columns
features_df = df.drop(columns=['Class'])

# Select a random row with exactly 29 features
random_row = features_df.sample(n=1)

# Convert row to a list of 29 feature values
features_list = random_row.values.flatten().tolist()

# Construct the URL for prediction
url = "http://127.0.0.1:5000/predict?" + "&".join([f"features={x}" for x in features_list])

# Print the generated URL
print("✅ Use this URL in your browser or API tool:")
print(url)
