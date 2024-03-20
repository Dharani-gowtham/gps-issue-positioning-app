import streamlit as st
import pandas as pd
from streamlit_js_eval import get_geolocation
from streamlit_extras.grid import grid
import requests

ip = "172.43.0.22"

# GET   - http://127.0.0.1:5000/view-issue -> list of co-ordinates
url_view_issue = f"http://{ip}:5000/view-issue"

# POST  - http://127.0.0.1:5000/add-issue -> Add data to the db
url_add_issue = f"http://{ip}:5000/add-issue"



# page configuration
st.set_page_config(layout="wide")

gps_location = get_geolocation()

if gps_location is not None:
    lats = gps_location["coords"]["latitude"]
    longs = gps_location["coords"]["longitude"]

    df = pd.DataFrame({
            "LATITUDE": [lats],
            "LONGITUDE": [longs]
        })


    # layout
    col1, col2 = st.columns([1, 1])

    # column 1
    with col1:
        # title
        st.title("Crimes Level Indicator using GPS")
        layout_grid = grid([4, 1])
        name = layout_grid.text_input("name")
        age = layout_grid.text_input("age")
        issue = st.text_area("Issue", height=300)

        payload = {
            "name": f"{name}",
            "age": age,
            "issue": f"{issue}",
            "location": {
                "latitude": lats,
                "longitude": longs
            }
        }
        if st.button("Add issue", use_container_width=True):
            try:
                response = requests.post(url=url_add_issue, json=payload)
                st.toast(response.text)
            except Exception as e:
                st.toast(f"Something went wrong {e}")



    # column 2
    with col2:
        st.markdown("#### Your Current Location")
        st.map(df, use_container_width=True)
else:
    st.error("Failed to retrieve your current location. Please check your browser settings or try again later.")
