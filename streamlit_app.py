import streamlit as st

# Function to convert units to inches
def to_inches(value, unit):
    # If unit is 'ft', convert to inches by multiplying by 12
    return value * 12 if unit == 'ft' else value

# Function to convert inches to feet and inches
def to_feet(value_in_inches):
    feet = value_in_inches // 12
    inches = value_in_inches % 12
    return f"{int(feet)} ft {int(inches)} inch"

st.title("Cutting ProRod Calculator")
st.write("Calculate the correct Cutting ProRod length for oilfield equipment")
st.write("Done by: Eng Habib Al Wahabi")

# Layout using columns to align value inputs and units
col1, col2 = st.columns([4, 1])

with col1:
    # PL Size: Whole number input
    PL_value = st.number_input('PL Size', value=0, step=1)  # No format string here
with col2:
    PL_unit = st.selectbox('', ['inch', 'ft'], index=0, key='PL_unit', label_visibility="collapsed")

with col1:
    SO_value = st.number_input('SO', value=0, step=1)
with col2:
    SO_unit = st.selectbox('', ['inch', 'ft'], index=0, key='SO_unit', label_visibility="collapsed")

with col1:
    DH_value = st.number_input('DH', value=0, step=1)
with col2:
    DH_unit = st.selectbox('', ['inch', 'ft'], index=0, key='DH_unit', label_visibility="collapsed")

with col1:
    MinStickup_value = st.number_input('Min Stickup', value=0, step=1)
with col2:
    MinStickup_unit = st.selectbox('', ['inch', 'ft'], index=0, key='MinStickup_unit', label_visibility="collapsed")

# PSD (Meter input is kept)
PSD = st.number_input('PSD (m)', value=0, step=1)

# Poney Rotor (feet)
PoneyRotor = st.number_input('Poney Rotor (ft)', value=0, step=1)

# Use a single button for calculating
st.button("Calculate")

# Show the results section
st.subheader("Results:")
st.text("Cutting ProRod Length: 21 ft")  # Example result, replace with calculation logic

# Optionally add a "Clear Form" button for resetting the form
if st.button("Clear Form"):
    st.experimental_rerun()

# This layout should be visually similar to the one you've shown with clean separation of each input field and the result display


