import os
import streamlit as st
import pandas as pd

path = os.path.join("..", "data", "st10_data.csv")
data = pd.read_csv(path)
data['year'] = data['year'].astype(str)

st.set_page_config(layout="wide")

st.header('2023 to Present Day Climate Change Article Pageviews')


choice = st.selectbox(
    'Select years', ['All','2023','2024', '2025']
)
if choice == 'All':
  st.write(f'Full data:')
  chart_data = data
else:
  chart_data = data[data['year']==choice]
  st.write(f'Data for year {choice}')


#st.write(chart_data.head())
st.line_chart(data=chart_data, x='month-day', y='z_score', color='year', x_label = 'Time', y_label='Z_Score')
# st.line_chart(data=chart_data, x='month-day', y='z_score', color='year', x_label = 'Time', y_label='Z_score\nCC Pageviews')