import streamlit as st
import requests
import datetime
import pytz

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

date = st.date_input("Insert a date", value=datetime.date(2021, 5, 30))
time = st.time_input("Insert a time", value=datetime.time(10, 12))

pickup_datetime = f"{str(date)} {str(time)}"
pickup_longitude = st.number_input('Insert pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('Insert pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('Insert dropoff longitude', value=40.6513111)
dropoff_latitude = st.number_input('Insert dropoff latitude', value=-73.8803331)
passenger_count = st.number_input('Insert passenger count', value=2)


'''

## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}
response = requests.get(url, params).json()


st.markdown(f'''
The fare will be {round(response['fare'], 2)}$
''')
