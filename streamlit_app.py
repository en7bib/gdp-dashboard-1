import streamlit as st

# Function to convert units to inches
def to_inches(value, unit):
    return value * 12 if unit == 'ft' else value

# Function to convert inches to feet
def to_feet(value_in_inches):
    feet = value_in_inches // 12
    inches = value_in_inches % 12
    return f"{int(feet)} ft {int(inches)} inch"

st.title("Cutting ProRod Calculator")

# Columns for input layout
col1, col2 = st.columns(2)

with col1:
    PL = st.number_input('PL Size (inches or feet)', value=0.0)
    PL_unit = st.selectbox('Unit for PL', ['inch', 'ft'])

    SO = st.number_input('SO (inches or feet)', value=0.0)
    SO_unit = st.selectbox('Unit for SO', ['inch', 'ft'])

    DH = st.number_input('DH (inches or feet)', value=0.0)
    DH_unit = st.selectbox('Unit for DH', ['inch', 'ft'])

    MinStickup = st.number_input('Min Stickup (inches or feet)', value=0.0)
    MinStickup_unit = st.selectbox('Unit for Min Stickup', ['inch', 'ft'])

    PSD = st.number_input('PSD (m)', value=0.0)

    PoneyRotor = st.number_input('Poney Rotor (ft)', value=0.0)

with col2:
    BOP = st.number_input('BOP Extension Size (inches or feet)', value=0.0)
    BOP_unit = st.selectbox('Unit for BOP', ['inch', 'ft'])

    SW = st.number_input('SW (inches or feet)', value=0.0)
    SW_unit = st.selectbox('Unit for SW', ['inch', 'ft'])

    Clamp = st.number_input('Clamp Size (inches or feet)', value=0.0)
    Clamp_unit = st.selectbox('Unit for Clamp', ['inch', 'ft'])

    Adapter = st.number_input('Adapter Size (inches or feet)', value=0.0)
    Adapter_unit = st.selectbox('Unit for Adapter', ['inch', 'ft'])

    Rotor = st.number_input('Rotor Size (m)', value=0.0)

# Add some spacing for better UI on mobile devices
st.write("\n" * 2)

# Button to calculate the results
if st.button('Calculate'):
    # Convert all inputs to inches for calculation
    PL = to_inches(PL, PL_unit)
    BOP = to_inches(BOP, BOP_unit)
    SO = to_inches(SO, SO_unit)
    SW = to_inches(SW, SW_unit)
    DH = to_inches(DH, DH_unit)
    Clamp = to_inches(Clamp, Clamp_unit)
    MinStickup = to_inches(MinStickup, MinStickup_unit)
    Adapter = to_inches(Adapter, Adapter_unit)

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

