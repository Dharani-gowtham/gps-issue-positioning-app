import streamlit as st
import requests
from streamlit_extras.grid import grid
import pandas as pd

ip = "172.43.0.22"
st.set_page_config(layout="wide")

lats = []
longs = []

# data_frame = {
#     "latitude": lats,
#     "lonngitude": longs
# }
def exp(history):
    with st.expander(history['issue']):
        layout_grid = grid([5, 1])
        layout_grid.write(f"#### Name: {history['name']}")
        layout_grid.write(f"#### Age: {history['age']}")
        st.write(history['issue'])

col1, col2 = st.columns([1, 1])

with col1:
    # GET   - http://127.0.0.1:5000/details -> return the list of data
    url_get_details = f"http://{ip}:5000/details"

    history = requests.get(url_get_details)
    st.markdown("## History of Issues")
    data = history.json()
    for i in data:
        exp(i)

with col2:
    st.markdown("## History Locations")
    url_get_co_ordinates = f"http://{ip}:5000/view-issue"
    coordinate_data = requests.get(url_get_co_ordinates).json()

    for i in coordinate_data:
        if 'location' in i and 'latitude' in i['location'] and 'longitude' in i['location']:
            lats.append(i['location']['latitude'])
            longs.append(i['location']['longitude'])

    df = pd.DataFrame({
        "latitude": lats,
        "longitude": longs
    })

    st.map(df, use_container_width=True)
