import pandas as pd
import json

#load data from JSON
with open('MF_BM_stem.json', 'r') as json_file:
    data = json.load(json_file)

# convert JSON data to df
df = pd.DataFrame(data)

#cleaned df
print(df)

# Filter for specific columns if needed
#.copy:making a copy of df ;to not affect the original DataFrame & avoid warning 

df_filtered = df[[ "Province", "Faculty", "Level", "Female", "Male"]].copy()

#convert 'Female' and 'Male' columns to numeric using 
# .loc[] to avoid SettingWithCopyWarning

df_filtered.loc[:, 'Female'] = pd.to_numeric(df_filtered['Female'], errors='coerce')
df_filtered.loc[:, 'Male'] = pd.to_numeric(df_filtered['Male'], errors='coerce')

# Group by 'Province' and sum up 'Female' and 'Male' counts
summary = df_filtered.groupby('Province')[['Female', 'Male']].sum().reset_index()

# Print the summary
print("Summary:")
print(summary)

with open('province_wise.json', 'w') as json_file:
    json.dump(summary.to_dict(orient='records'), json_file, indent=4)
