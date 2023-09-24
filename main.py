import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('master_team_list.csv')
df = pd.DataFrame(data)

# Data Analysis
print("Data Overview:")
print(df.describe())

# Data Visualization
plt.figure(figsize=(12, 6))

# Bar plot of Team_name by Season
plt.bar(df['season'], df['team_name'])
plt.xlabel('Season')
plt.ylabel('Team Name')
plt.title('Bar Plot of Team Names by Season')
plt.xticks(rotation=90)
plt.show()
