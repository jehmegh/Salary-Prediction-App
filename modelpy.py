import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Load dataset
dataset = pd.read_csv('hiring.csv')

# Fill missing values
dataset['experience'].fillna(0, inplace=True)
dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

# Prepare data
X = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

# Convert experience column to integers
def convert_to_int(word):
    word_dict = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'zero': 0, 0: 0
    }
    return word_dict[word]

X['experience'] = X['experience'].apply(lambda x: convert_to_int(x))

# Train model
regressor = LinearRegression()
regressor.fit(X, y)

# Save the model
pickle.dump(regressor, open('model.pkl', 'wb'))
