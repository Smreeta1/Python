import json
import pandas as pd
import matplotlib.pyplot as plt

with open('level.json', 'r') as file:
    faculty_data = json.load(file)

# convert to df
df_faculty = pd.DataFrame(faculty_data)

def parse_number(num_str):
    return int(num_str.replace(',', ''))

df_faculty['Male'] = df_faculty['Male'].apply(parse_number)
df_faculty['Female'] = df_faculty['Female'].apply(parse_number)

# visualization 
labels = df_faculty['Level']
male_counts = df_faculty['Male']
female_counts = df_faculty['Female']

x = range(len(labels))

#bar chart
plt.figure(figsize=(10, 5))
plt.bar(x, male_counts, width=0.4, label='Male', color='teal', align='center')
plt.bar(x, female_counts, width=0.4, label='Female', color='deepskyblue', align='edge')

plt.xlabel('Levels')
plt.ylabel('Number of Students')
plt.title('Male vs Female Students in Bachelor and Master(All Faculties) ')
plt.xticks(x, labels)
plt.legend()
plt.tight_layout()

# Save the figure as a PNG file
plt.savefig('MF_level_comparison.png', format='png')

# Show the plot
plt.show()
