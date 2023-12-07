
import pandas as pd
import plotly.express as px
import csv

csv_file_path = 'data.csv'

df = pd.read_csv(csv_file_path)

mean_attempts = df.groupby(['student_id', 'level'], as_index = False)['attempt'].mean()

fig = px.scatter(mean_attempts, x='student_id', y='level', size='attempt', color='attempt',
                 labels={'mean': 'Mean Attempts', 'level': 'Level'},
                 title='Mean Attempts of Each Student in Each Level')

fig.show()
