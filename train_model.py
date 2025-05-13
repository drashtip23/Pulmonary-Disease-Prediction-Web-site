import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your dataset
# Replace the filename and target column as needed
# Example: df = pd.read_csv('Pulmonary Disease- Lung Cancer Dataset.csv')
df = pd.read_csv('Pulmonary Disease- Lung Cancer Dataset.csv')
X = df.drop('target_column', axis=1)  # Replace with your actual target column
y = df['target_column']

# Train your model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f) 