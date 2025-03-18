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

# Columns for input layout
col1, col2 = st.columns(2)

with col1:
    # Whole number input for PL Size
    PL_value = st.number_input('PL Size', value=0, step=1)
    PL_unit = st.selectbox('Unit for PL', ['inch', 'ft'])

    # Whole number input for SO
    SO_value = st.number_input('SO', value=0, step=1)
    SO_unit = st.selectbox('Unit for SO', ['inch', 'ft'])

    # Whole number input for DH
    DH_value = st.number_input('DH', value=0, step=1)
    DH_unit = st.selectbox('Unit for DH', ['inch', 'ft'])

    # Whole number input for Min Stickup
    MinStickup_value = st.number_input('Min Stickup', value=0, step=1)
    MinStickup_unit = st.selectbox('Unit for Min Stickup', ['inch', 'ft'])

    # Whole number input for PSD (Meter input is kept)
    PSD = st.number_input('PSD (m)', value=0, step=1)

    # Whole number input for Poney Rotor (feet)
    PoneyRotor = st.number_input('Poney Rotor (ft)', value=0, step=1)

with col2:
    # Whole number input for BOP Extension Size
    BOP_value = st.number_input('BOP Extension Size', value=0, step=1)
    BOP_unit = st.selectbox('Unit for BOP', ['inch', 'ft'])

    # Whole number input for SW
    SW_value = st.number_input('SW', value=0, step=1)
    SW_unit = st.selectbox('Unit for SW', ['inch', 'ft'])

    # Whole number input for Clamp Size
    Clamp_value = st.number_input('Clamp Size', value=0, step=1)
    Clamp_unit = st.selectbox('Unit for Clamp', ['inch', 'ft'])

    # Whole number input for Adapter Size
    Adapter_value = st.number_input('Adapter Size', value=0, step=1)
    Adapter_unit = st.selectbox('Unit for Adapter', ['inch', 'ft'])

    # Whole number input for Rotor Size (Meter input kept)
    Rotor = st.number_input('Rotor Size (m)', value=0, step=1)

# Add some spacing for better UI on mobile devices
st.write("\n" * 2)

# Button to calculate the results
if st.button('Calculate'):
    # Convert all inputs to inches for calculation
    PL = to_inches(PL_value, PL_unit)
    BOP = to_inches(BOP_value, BOP_unit)
    SO = to_inches(SO_value, SO_unit)
    SW = to_inches(SW_value, SW_unit)
    DH = to_inches(DH_value, DH_unit)
    Clamp = to_inches(Clamp_value, Clamp_unit)
    MinStickup = to_inches(MinStickup_value, MinStickup_unit)
    Adapter = to_inches(Adapter_value, Adapter_unit)

    # Perform calculations
    Cutting_ProRod_Length_inch = (PL + BOP + SO + SW + 12 + 48) - (DH + Clamp + MinStickup + Adapter)
    RC_Value_inch = (DH + Adapter) - (SW + SO)
    Clamp_Position_inch = (RC_Value_inch + (SW + SO)) - DH

    # Convert rotor and poney rotor for the final ProRod Used
    ProRod_Used = (Rotor + (PoneyRotor * 0.3048) + (1.82 * 3) + (0.294 * 3)) - PSD

    # Show the results
    st.markdown(f"""
    ### Results:
    - **Cutting ProRod Length:** `{to_feet(Cutting_ProRod_Length_inch)}`
    - **RC Value:** `{to_feet(RC_Value_inch)}`
    - **Clamp Position:** `{to_feet(Clamp_Position_inch)}`
    - **ProRod Used:** `{round(ProRod_Used, 2)} m`
    """)


