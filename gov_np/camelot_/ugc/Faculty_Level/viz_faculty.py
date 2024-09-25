import json
import pandas as pd
import matplotlib.pyplot as plt

with open('faculty.json', 'r') as file:
    faculty_data = json.load(file)
    
# convert to df
df_faculty = pd.DataFrame(faculty_data)

def parse_number(num_str):
    return int(num_str.replace(',', ''))

df_faculty['Male'] = df_faculty['Male'].apply(parse_number)
df_faculty['Female'] = df_faculty['Female'].apply(parse_number)

# visualization
labels = df_faculty['Faculty']
male_counts = df_faculty['Male']
female_counts = df_faculty['Female']

x = range(len(labels))

#bar chart
plt.figure(figsize=(10, 5))
plt.bar(x, male_counts, width=0.4, label='Male', color='blue', align='center')
plt.bar(x, female_counts, width=0.4, label='Female', color='pink', align='edge')

plt.xlabel('Faculties')
plt.ylabel('Number of Students')
plt.title('Male vs Female Students in Engineering and S&T Faculties')
plt.xticks(x, labels)
plt.legend()
plt.tight_layout()
plt.savefig('MF_faculty_comparison.png', format='png')
plt.show()
