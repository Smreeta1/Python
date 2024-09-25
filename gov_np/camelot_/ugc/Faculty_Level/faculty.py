import pandas as pd
import json

df = pd.read_csv('faculty.csv', skiprows=1)

df.columns = ['Faculty', 'Male', 'Female', 'Number of Students', 'Percentage of Students'] + list(df.columns[5:])

df_cleaned = df.dropna(how='all')

df_cleaned = df_cleaned.drop(columns=[col for col in df_cleaned.columns if 'Unnamed' in col])

df_cleaned['Faculty'] = df_cleaned['Faculty'].str.strip()

filtered = df_cleaned[df_cleaned['Faculty'].isin(['Engineering', 'S&T'])].tail(3)

# filtered result
print(filtered)

with open('faculty.json', 'w') as json_file:
    json.dump(json.loads(filtered.to_json(orient='records')), json_file, indent=4)




