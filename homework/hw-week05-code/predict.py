
import pickle

input_file_pipeline = "data/hw5-pipeline.bin"

### Load model
# Character Meaning:
# 'r'       open for reading the file
with open(input_file_pipeline, 'rb') as f_in: 
    pipeline = pickle.load(f_in)

# example
datapoint = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

y_pred = pipeline.predict_proba([datapoint])[0, 1]

print('input:', datapoint)
print('output:', y_pred)