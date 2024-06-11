import streamlit as st
import datetime
from modules import gti, dpd


# Function to get all tracking updates of GTI and DPD and sort them
def get_tracking_data(tracking_code):
    # Dati di esempio
    gti_updates = gti.track(tracking_code)
    if gti_updates == [] : return []
    dpd_updates = dpd.track(tracking_code)
    not_sorted_updates = []
    for update in gti_updates: not_sorted_updates.append(update)
    for update in dpd_updates: not_sorted_updates.append(update)
    sorted_updates = sorted(not_sorted_updates, key=lambda x: x['date'],reverse=True)
    return sorted_updates

# Set page configuration
st.set_page_config(page_title="EUR-Railway Tracking", page_icon="🚆")

# Title of the site
st.title("🚆 EUR-Railway Tracking")

# Introductory message
st.markdown("""
Welcome to the EUR-Railway package tracking system! 
Enter your DPD tracking code to see updates.
""")

# Input for the tracking code
tracking_code = st.text_input("Enter your tracking code:")

# Button to track
if st.button("Track"):
    if tracking_code:
        # Get tracking data
        tracking_data = get_tracking_data(tracking_code)
                
        # Display each tracking update
        st.subheader("🔍 Tracking Updates")
        for update in tracking_data:
            st.markdown(f"**Date:** {datetime.datetime.fromtimestamp(update['date']).strftime('%Y-%m-%d %H:%M')}")
            st.markdown(f"**Location:** {update['location']}")
            st.markdown(f"**Status:** {update['status']}")
            st.markdown(f"**Courier:** {update['courier']}")
            st.markdown("---")
    else:
        st.error("Please enter a valid tracking code.")

st.markdown("---")
st.markdown("<div style='text-align: center;'>Made by galbaninoh with 🩷</div>", unsafe_allow_html=True)