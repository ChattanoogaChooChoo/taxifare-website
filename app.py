import streamlit as st
import requests
import pandas as pd
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

date = st.date_input('When?', value=datetime.date.fromisoformat("2013-07-06"))
time = st.time_input('When exactly?', value=datetime.time.fromisoformat("17:18:00"))
pickup_longitude = st.number_input('Where from longitude-wise?', min_value=-180.0, max_value=180.0, value=-73.950655)
pickup_latitude = st.number_input('Where from latitude-wise?', min_value=-90.0, max_value=90.0, value=40.783282)
dropoff_longitude = st.number_input('Where to longitude-wise?', min_value=-180.0, max_value=180.0, value=-73.984365)
dropoff_latitude = st.number_input('Where to latitude-wise?', min_value=-90.0, max_value=90.0, value=40.769802)
passenger_count = st.number_input('How many passengers?', min_value=1, max_value=3, step=1, value=1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare-108148011651.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = dict(
    pickup_datetime=[pd.Timestamp("2013-07-06 17:18:00", tz='UTC')],
    pickup_longitude=[-73.950655],
    pickup_latitude=[40.783282],
    dropoff_longitude=[-73.984365],
    dropoff_latitude=[40.769802],
    passenger_count=[1],
)
params = dict(
    pickup_datetime=[pd.Timestamp(f"{date} {time}", tz='UTC').strftime('%Y-%m-%d %X')],
    pickup_longitude=[pickup_longitude],
    pickup_latitude=[pickup_latitude],
    dropoff_longitude=[dropoff_longitude],
    dropoff_latitude=[dropoff_latitude],
    passenger_count=[passenger_count],
)

response = requests.get(url, params)
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
params
f"Le montant de la course sera de {round(float(response.json()['fare']), 2)} $"