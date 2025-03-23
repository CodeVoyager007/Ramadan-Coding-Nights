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
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: white;
        padding: 10px;
        text-align: center;
        color: #800000;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Update the TIME_ZONES dictionary with more regions and cities
TIME_ZONES = {
    "Asia": [
        "Asia/Karachi",  # Pakistan
        "Asia/Tokyo",    # Japan
        "Asia/Dubai",    # UAE
        "Asia/Kolkata",  # India
        "Asia/Singapore", # Singapore
        "Asia/Shanghai", # China
        "Asia/Seoul",    # South Korea
        "Asia/Bangkok",  # Thailand
        "Asia/Jakarta",  # Indonesia
        "Asia/Manila",   # Philippines
        "Asia/Riyadh",   # Saudi Arabia
        "Asia/Tehran",   # Iran
        "Asia/Baghdad",  # Iraq
        "Asia/Dhaka",    # Bangladesh
        "Asia/Hong_Kong" # Hong Kong
    ],
    "America": [
        "America/New_York",    # USA Eastern
        "America/Los_Angeles", # USA Pacific
        "America/Chicago",     # USA Central
        "America/Toronto",     # Canada
        "America/Vancouver",   # Canada
        "America/Mexico_City", # Mexico
        "America/Sao_Paulo",   # Brazil
        "America/Buenos_Aires",# Argentina
        "America/Santiago",    # Chile
        "America/Lima",        # Peru
        "America/Bogota",      # Colombia
        "America/Caracas",     # Venezuela
        "America/Panama",      # Panama
        "America/Denver",      # USA Mountain
        "America/Phoenix"      # USA Arizona
    ],
    "Europe": [
        "Europe/London",   # UK
        "Europe/Berlin",   # Germany
        "Europe/Paris",    # France
        "Europe/Rome",     # Italy
        "Europe/Madrid",   # Spain
        "Europe/Amsterdam",# Netherlands
        "Europe/Brussels", # Belgium
        "Europe/Vienna",   # Austria
        "Europe/Moscow",   # Russia
        "Europe/Stockholm",# Sweden
        "Europe/Oslo",     # Norway
        "Europe/Copenhagen",# Denmark
        "Europe/Dublin",   # Ireland
        "Europe/Warsaw",   # Poland
        "Europe/Zurich"    # Switzerland
    ],
    "Australia/Pacific": [
        "Australia/Sydney",    # Australia Eastern
        "Australia/Melbourne", # Australia
        "Australia/Perth",     # Australia Western
        "Australia/Brisbane",  # Australia Queensland
        "Australia/Adelaide",  # Australia Central
        "Pacific/Auckland",    # New Zealand
        "Pacific/Fiji",        # Fiji
        "Pacific/Guam",        # Guam
        "Pacific/Honolulu",    # Hawaii
        "Pacific/Port_Moresby" # Papua New Guinea
    ],
    "Africa": [
        "Africa/Cairo",        # Egypt
        "Africa/Johannesburg", # South Africa
        "Africa/Lagos",        # Nigeria
        "Africa/Nairobi",      # Kenya
        "Africa/Casablanca",   # Morocco
        "Africa/Accra",        # Ghana
        "Africa/Addis_Ababa",  # Ethiopia
        "Africa/Dar_es_Salaam",# Tanzania
        "Africa/Khartoum",     # Sudan
        "Africa/Algiers"       # Algeria
    ],
    "Other": [
        "UTC",      # Coordinated Universal Time
        "GMT",      # Greenwich Mean Time
        "Iceland",  # Iceland (GMT all year)
        "Etc/GMT+12", # International Date Line West
        "Etc/GMT-12"  # International Date Line East
    ]
}

# Create app title with emoji
st.title("🌍 Global Time Zone Converter")

# Create tabs for different features
tab1, tab2, tab3 = st.tabs(["Current Time", "Time Converter", "Time Zone Information"])

with tab1:
    st.subheader("Current Time Across the World")
    
    # Group selection by region
    selected_regions = st.multiselect("Select Regions", list(TIME_ZONES.keys()), default=["Asia"])
    
    # Create a list of time zones based on selected regions
    available_zones = []
    for region in selected_regions:
        available_zones.extend(TIME_ZONES[region])
    
    selected_timezone = st.multiselect(
        "Select Time Zones", available_zones, 
        default=available_zones[:2] if available_zones else None
    )

    if selected_timezone:
        # Create a DataFrame for better display
        times_data = []
        for tz in selected_timezone:
            current_time = datetime.now(ZoneInfo(tz))
            times_data.append({
                "Time Zone": tz,
                "Date": current_time.strftime("%Y-%m-%d"),
                "Time": current_time.strftime("%I:%M:%S %p"),
                "UTC Offset": current_time.strftime("%z")
            })
        
        df = pd.DataFrame(times_data)
        st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("Time Zone Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Source time input
        source_date = st.date_input("Select Date", datetime.now())
        source_time = st.time_input("Select Time", datetime.now().time())
        from_tz = st.selectbox("From Time Zone", [tz for region in TIME_ZONES.values() for tz in region])

    with col2:
        # Target time zones
        to_tzs = st.multiselect("To Time Zones", 
                               [tz for region in TIME_ZONES.values() for tz in region],
                               default=["UTC"])

    if st.button("Convert Time ⚡"):
        # Combine date and time
        dt = datetime.combine(source_date, source_time, tzinfo=ZoneInfo(from_tz))
        
        # Convert to all selected time zones
        conversion_data = []
        for target_tz in to_tzs:
            converted = dt.astimezone(ZoneInfo(target_tz))
            conversion_data.append({
                "Time Zone": target_tz,
                "Date": converted.strftime("%Y-%m-%d"),
                "Time": converted.strftime("%I:%M:%S %p"),
                "UTC Offset": converted.strftime("%z")
            })
        
        df_converted = pd.DataFrame(conversion_data)
        st.dataframe(df_converted, use_container_width=True)

with tab3:
    st.subheader("Time Zone Information")
    
    # Display time zone details
    st.write("### Time Zones by Region")
    for region, zones in TIME_ZONES.items():
        with st.expander(f"{region} Time Zones"):
            for zone in zones:
                current_time = datetime.now(ZoneInfo(zone))
                st.write(f"**{zone}** (UTC {current_time.strftime('%z')})")
                st.write(f"Current time: {current_time.strftime('%Y-%m-%d %I:%M:%S %p')}")

# Add useful information
st.sidebar.title("ℹ️ Quick Info")
st.sidebar.write("""
### Tips:
- Use the tabs to navigate between features
- Select multiple time zones for comparison
- Times are automatically updated
- UTC offsets show the difference from UTC
""")

# Add current UTC time in sidebar
st.sidebar.write("### Current UTC Time")
st.sidebar.write(datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d %I:%M:%S %p"))

# Add footer
st.markdown(
    """
    <div class="footer">
        Coded with 💓 by Ayesha Mughal
    </div>
    """,
    unsafe_allow_html=True
)