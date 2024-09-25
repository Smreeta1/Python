import pandas as pd
import json

# Load the CSV file, skipping the first row of headers
df = pd.read_csv("MF_college.csv", header=1)

# Drop columns and rows that are completely empty
df_cleaned = df.dropna(axis=1, how="all")
df_cleaned = df_cleaned.dropna(axis=0, how="all")

# Print the cleaned DataFrame for debugging
print(df_cleaned)

# Filter for specific columns
df_filtered = df_cleaned[["Campus Name", "Province", "Faculty", "Level", "Female", "Male"]]

# Fill NaN values in 'Level' with an empty string for safety
df_filtered['Level'] = df_filtered['Level'].fillna('')

# Further filter based on specific criteria
df_filtered = df_filtered[
    df_filtered["Faculty"].isin(["S&T", "Engineering"]) &
    (df_filtered["Level"].str.contains("Bachelor", case=False) | df_filtered["Level"].str.contains("Master", case=False)) &
    (~df_filtered["Level"].str.contains(" ", case=False))  # Exclude any Level with additional program names
]

# Print the filtered DataFrame
print(df_filtered)

# Convert 'Female' and 'Male' columns to numeric
df_filtered['Female'] = pd.to_numeric(df_filtered['Female'], errors='coerce')
df_filtered['Male'] = pd.to_numeric(df_filtered['Male'], errors='coerce')

# Group by 'Level' and sum up 'Female' and 'Male' counts
summary = df_filtered.groupby('Level')[['Female', 'Male']].sum().reset_index()

print("Summary:")
print(summary)

# Save the filtered DataFrame to a JSON file
with open('MF_BM_stem.json', 'w') as json_file:
    json.dump(json.loads(df_filtered.to_json(orient='records')), json_file, indent=4)
