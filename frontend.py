import streamlit as st
import plotly.express as px
from backend import get_data

st.header("Weather Forecast for the Next Days")
place = st.text_input("Enter City or Place")
days = st.slider('Forecast Days', min_value=1, max_value=5)
option = st.selectbox('Select data to view', ['Temperature', 'Sky'])

if place:
    filtered_data = get_data(place, days)

    if option == 'Temperature':
        temperature = [content['main']['temp'] for content in filtered_data]
        dates = [content['dt_txt'] for content in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature(C)'})
        st.plotly_chart(figure)

    if option == 'Sky':
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                  'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        sky = [content['weather'][0]['main'] for content in filtered_data]
        image_path = [images[condition] for condition in sky]

        st.image(image_path, width=115)