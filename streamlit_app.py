import streamlit as st

# Function to convert units to inches
def to_inches(value, unit):
    return value * 12 if unit == 'ft' else value

# Function to convert inches to feet and inches
def to_feet(value_in_inches):
    feet = value_in_inches // 12
    inches = value_in_inches % 12
    return f"{int(feet)} ft {int(inches)} inch"

# Title and description
st.title("Cutting ProRod Calculator")
st.write("Calculate the correct Cutting ProRod length for oilfield equipment")
st.write("Done by: Eng Habib Al Wahabi")

# Form layout using columns for better alignment
col1, col2 = st.columns([3, 1])  # Adjust the width ratio of the columns

# Input fields in col1 (value input) and col2 (unit dropdown)
with col1:
    PL_value = st.number_input('PL Size', value=0, step=1)
with col2:
    PL_unit = st.selectbox('', ['inch', 'ft'], index=0, label_visibility="collapsed")

with col1:
    SO_value = st.number_input('SO', value=0, step=1)
with col2:
    SO_unit = st.selectbox('', ['inch', 'ft'], index=0, label_visibility="collapsed")

with col1:
    DH_value = st.number_input('DH', value=0, step=1)
with col2:
    DH_unit = st.selectbox('', ['inch', 'ft'], index=0, label_visibility="collapsed")

with col1:
    MinStickup_value = st.number_input('Min Stickup', value=0, step=1)
with col2:
    MinStickup_unit = st.selectbox('', ['inch', 'ft'], index=0, label_visibility="collapsed")

# PSD (meter input) field remains a whole number
PSD = st.number_input('PSD (m)', value=0, step=1)

# Poney Rotor (feet)
PoneyRotor = st.number_input('Poney Rotor (ft)', value=0, step=1)

# Add some spacing for better UI
st.write("\n" * 2)

# Button for calculating the results
if st.button('Calculate'):
    # Convert all inputs to inches for calculation
    PL = to_inches(PL_value, PL_unit)
    BOP = to_inches(0, 'inch')  # Default value
    SO = to_inches(SO_value, SO_unit)
    SW = to_inches(0, 'inch')  # Default value
    DH = to_inches(DH_value, DH_unit)
    Clamp = to_inches(0, 'inch')  # Default value
    MinStickup = to_inches(MinStickup_value, MinStickup_unit)
    Adapter = to_inches(0, 'inch')  # Default value

    # Perform calculations based on your formula
    Cutting_ProRod_Length_inch = (PL + BOP + SO + SW + 12 + 48) - (DH + Clamp + MinStickup + Adapter)
    RC_Value_inch = (DH + Adapter) - (SW + SO)
    Clamp_Position_inch = (RC_Value_inch + (SW + SO)) - DH

    # Convert rotor and poney rotor for the final ProRod Used
    ProRod_Used = (PSD + (PoneyRotor * 0.3048) + (1.82 * 3) + (0.294 * 3))  # Adjusted based on your formula

    # Show the results neatly
    st.markdown(f"""
    ### Results:
    - **Cutting ProRod Length:** `{to_feet(Cutting_ProRod_Length_inch)}`
    - **RC Value:** `{to_feet(RC_Value_inch)}`
    - **Clamp Position:** `{to_feet(Clamp_Position_inch)}`
    - **ProRod Used:** `{round(ProRod_Used, 2)} m`
    """)

# Clear form button
if st.button("Clear Form"):
    st.experimental_rerun()
