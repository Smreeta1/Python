import pandas as pd
import json

df = pd.read_csv("level.csv", header=1)

df_cleaned = df.dropna(axis=1, how="all")

df_cleaned = df_cleaned.dropna(axis=0, how="all")

df_filtered = df_cleaned[["Level", "Male", "Female"]]

df_filtered = df_filtered[
    df_filtered["Level"].str.contains("Bachelor|Master", case=False)
]
print(df_filtered)

#save to json file
with open('level.json', 'w') as json_file:
    json.dump(json.loads(df_filtered.to_json(orient='records')), json_file, indent=4)

