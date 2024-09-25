import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

with open('MF_BM_stem.json', 'r') as json_file:
    data = json.load(json_file)

df = pd.DataFrame(data)

# Convert 'Female' & 'Male' columns to numeric
df['Female'] = pd.to_numeric(df['Female'], errors='coerce')
df['Male'] = pd.to_numeric(df['Male'], errors='coerce')

# filter for Bachelor and Master levels
bachelor_data = df[df['Level'].str.contains("Bachelor", case=False)]
master_data = df[df['Level'].str.contains("Master", case=False)]

# Group by 'Level' and sum up 'Female' and 'Male' counts
bachelor_summary = bachelor_data[['Level', 'Female', 'Male']].groupby('Level').sum().reset_index()
master_summary = master_data[['Level', 'Female', 'Male']].groupby('Level').sum().reset_index()

#JSON structure
output_data = {
    "Bachelor": bachelor_summary.to_dict(orient='records'),
    "Master": master_summary.to_dict(orient='records')
}

#save to JSON
with open('MF_level.json', 'w') as json_file:
    json.dump(output_data, json_file, indent=4)

print(output_data)

# Visualization
bachelor_summary['Level_Type'] = 'Bachelor'
master_summary['Level_Type'] = 'Master'

# Combine both dataframes
combined_summary = pd.concat([bachelor_summary, master_summary], ignore_index=True)

melted = combined_summary.melt(id_vars=['Level', 'Level_Type'], value_vars=['Male', 'Female'],
                                var_name='Gender', value_name='No. of Students')

custom_palette = ["deepblue","orange"] 

#bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=melted, x='Level_Type', y='No. of Students', hue='Gender', palette=custom_palette)

plt.title('Male vs Female in STEM Bachelor and Master Levels', fontsize=16)
plt.xlabel('Level Type', fontsize=14)
plt.ylabel('No. of Students', fontsize=14)
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig('MvsF_counts.png', format='png', dpi=300) #save as .png 
plt.show()