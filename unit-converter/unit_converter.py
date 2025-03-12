import streamlit as st  # Import Streamlit for creating the web-based UI

# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
        "liters_milliliters": 1000,  # 1 liter = 1000 milliliters
        "milliliters_liters": 0.001,  # 1 milliliter = 0.001 liters
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,  # Celsius to Fahrenheit
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,  # Fahrenheit to Celsius
        "miles_kilometers": 1.60934,  # 1 mile = 1.60934 kilometers
        "kilometers_miles": 0.621371,  # 1 kilometer = 0.621371 miles
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
    
    if unit_from == unit_to:
        return value  # Return the value if both units are the same

    if key in conversions:
        conversion = conversions[key]
        # Apply the conversion factor or formula
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return f"Conversion from {unit_from} to {unit_to} not supported."

# Streamlit UI setup
st.title("✨ Universal Unit Converter ✨")  # Set title for the web app

# Custom CSS to enhance the design with new colors
st.markdown("""
    <style>
        .stButton > button {
            background-color: #0066CC;  /* Blue */
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #005BB5;  /* Darker Blue */
        }
        .stSelectbox, .stNumberInput {
            font-size: 18px;
            color: #333333;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 15px;
        }
        .stTitle {
            font-family: 'Arial', sans-serif;
            color: #333333;  /* Dark Gray */
        }
        .stText {
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
        .stMarkdown {
            text-align: center;
            font-size: 18px;
            color: #333333;  /* Dark Gray */
        }
        body {
            background-color: #F5F5F5;  /* Light Gray */
        }
        /* Styling for the result to make it more prominent */
        .result {
            font-size: 30px;
            font-weight: bold;
            color: #0066CC;  /* Blue */
            text-align: center;
            padding: 20px;
            background-color: #E8F0FE;  /* Light Blue */
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Displaying introductory text with new color
st.markdown("""
    Welcome to the **Universal Unit Converter**! 🌍
    Use this app to convert various units like length, mass, temperature, and more.
    Please enter a value and select the units you'd like to convert.
""")

# User input: numerical value to convert
value = st.number_input("Enter value to convert:", min_value=0.0, step=0.1, format="%.2f")

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "Convert from:",
    ["", "meters", "kilometers", "grams", "kilograms", "liters", "milliliters", "celsius", "fahrenheit", "miles"]
)

# Dropdown to select unit to convert to
unit_to = st.selectbox(
    "Convert to:",
    ["", "meters", "kilometers", "grams", "kilograms", "liters", "milliliters", "celsius", "fahrenheit", "miles"]
)

# Button to trigger conversion
if st.button("🔄 Convert"):
    # Check if value, unit_from, and unit_to are filled out correctly
    if value <= 0:
        st.warning("Please enter a valid numerical value.")
    elif unit_from == "" or unit_to == "":
        st.warning("Please select both 'Convert from' and 'Convert to' units.")
    elif unit_from == unit_to:
        st.warning("Please select different units for conversion.")
    else:
        result = convert_units(value, unit_from, unit_to)  # Call the conversion function
        # Display the result in a prominent box, no asterisk
        st.markdown(f'<div class="result">Converted Value: {result}</div>', unsafe_allow_html=True)

# Adding a footer for better UI
st.markdown("""
    <div style="text-align: center; font-size: 14px; color: #777777;">
        Made with ❤️ by Ayesha. Happy Converting! 🌟
    </div>
""", unsafe_allow_html=True)
