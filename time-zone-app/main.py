# Import required libraries
import streamlit as st
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Time Zone Converter",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    .stButton>button {
        width: 100%;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f0f2f6;
        padding: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# List of available time zones with regions
TIME_ZONES = {
    "Popular": ["UTC", "GMT"],
    "Asia": ["Asia/Karachi", "Asia/Dubai", "Asia/Tokyo", "Asia/Singapore", "Asia/Kolkata", "Asia/Shanghai"],
    "America": ["America/New_York", "America/Los_Angeles", "America/Chicago", "America/Toronto"],
    "Europe": ["Europe/London", "Europe/Paris", "Europe/Berlin", "Europe/Rome"],
    "Australia": ["Australia/Sydney", "Australia/Melbourne", "Australia/Perth"],
    "Africa": ["Africa/Cairo", "Africa/Lagos", "Africa/Johannesburg"]
}

# Flatten time zones for some operations
ALL_TIME_ZONES = [tz for region in TIME_ZONES.values() for tz in region]

# Create app title with emoji
st.title("🌍 Global Time Zone Converter")

# Create tabs for different features
tab1, tab2, tab3 = st.tabs(["Current Time", "Time Converter", "Time Zone Information"])

with tab1:
    # World Clock Feature
    st.subheader("🕒 World Clock")
    
    # Region-based timezone selection
    selected_region = st.selectbox("Select Region", list(TIME_ZONES.keys()))
    selected_timezone = st.multiselect(
        "Select Time Zones", 
        TIME_ZONES[selected_region],
        default=TIME_ZONES[selected_region][:2]
    )

    # Display current time in columns
    if selected_timezone:
        cols = st.columns(len(selected_timezone))
        for i, tz in enumerate(selected_timezone):
            with cols[i]:
                current_time = datetime.now(ZoneInfo(tz))
                st.metric(
                    tz,
                    current_time.strftime("%I:%M:%S %p"),
                    current_time.strftime("%Y-%m-%d")
                )

with tab2:
    # Time Conversion Feature
    st.subheader("⚡ Time Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Source time and timezone
        source_date = st.date_input("Select Date", datetime.now())
        source_time = st.time_input("Select Time", datetime.now().time())
        from_tz = st.selectbox("From Timezone", ALL_TIME_ZONES, index=0)

    with col2:
        # Target timezone(s)
        to_tz = st.multiselect("To Timezone(s)", ALL_TIME_ZONES, default=[ALL_TIME_ZONES[1]])
        
    if st.button("🔄 Convert Time", key="convert"):
        # Combine date and time
        dt = datetime.combine(source_date, source_time, tzinfo=ZoneInfo(from_tz))
        
        # Create conversion results
        results = []
        for target_tz in to_tz:
            converted = dt.astimezone(ZoneInfo(target_tz))
            results.append({
                "Timezone": target_tz,
                "Date": converted.strftime("%Y-%m-%d"),
                "Time": converted.strftime("%I:%M:%S %p"),
                "Day": converted.strftime("%A")
            })
            
        # Display results in a nice table
        if results:
            st.success("Time Conversion Results:")
            df = pd.DataFrame(results)
            st.table(df)

with tab3:
    # Time Zone Information
    st.subheader("ℹ️ Time Zone Information")
    
    # Display time zone differences
    selected_tz = st.selectbox("Select a Time Zone", ALL_TIME_ZONES)
    if selected_tz:
        current_time = datetime.now(ZoneInfo(selected_tz))
        utc_offset = current_time.strftime('%z')
        utc_hours = float(utc_offset[:-2]) + float(utc_offset[-2:]) / 60
        
        st.info(f"""
        **Time Zone**: {selected_tz}
        **Current Time**: {current_time.strftime('%Y-%m-%d %I:%M:%S %p')}
        **UTC Offset**: {utc_hours:+.2f} hours
        **Day of Week**: {current_time.strftime('%A')}
        """)
        
        # Show common working hours overlap
        st.subheader("Working Hours Overlap")
        business_hours = {
            "New York": "9 AM - 5 PM EDT",
            "London": "9 AM - 5 PM BST",
            "Tokyo": "9 AM - 5 PM JST",
            "Sydney": "9 AM - 5 PM AEST"
        }
        st.table(pd.DataFrame([business_hours]).T.rename(columns={0: "Business Hours"}))

# Add footer
st.markdown(
    """
    <div class="footer">
        Made with 💓 by <a href="https://github.com/CodeVoyager007" target="_blank">Ayesha Mughal</a>
    </div>
    """,
    unsafe_allow_html=True
)