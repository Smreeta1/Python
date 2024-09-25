import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load JSON
with open('province_wise.json', 'r') as json_file:
    data = json.load(json_file)

# convert JSON data to df
df = pd.DataFrame(data)

melted_df = df.melt(id_vars="Province", value_vars=["Female", "Male"], var_name="Gender", value_name="Count")

palette = sns.color_palette(["teal", "deepskyblue"])

#bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=melted_df, x='Province', y='Count', hue='Gender', palette=palette)

# Customize the plot
plt.title('Male vs Female in STEM Province-wise data', fontsize=20)
plt.xlabel('Province', fontsize=12)
plt.ylabel('No. of Students', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Male_vs_Female_Province.png', dpi=300)
plt.show()
