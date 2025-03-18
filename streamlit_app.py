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
    # PL Size: Whole number input and unit in one box
    PL_value = st.number_input('PL Size', value=0, step=1, format="%.0f")
    PL_unit = st.selectbox('Unit for PL', ['inch', 'ft'], index=0)

    # SO: Whole number input and unit in one box
    SO_value = st.number_input('SO', value=0, step=1, format="%.0f")
    SO_unit = st.selectbox('Unit for SO', ['inch', 'ft'], index=0)

    # DH: Whole number input and unit in one box
    DH_value = st.number_input('DH', value=0, step=1, format="%.0f")
    DH_unit = st.selectbox('Unit for DH', ['inch', 'ft'], index=0)

    # Min Stickup: Whole number input and unit in one box
    MinStickup_value = st.number_input('Min Stickup', value=0, step=1, format="%.0f")
    MinStickup_unit = st.selectbox('Unit for Min Stickup', ['inch', 'ft'], index=0)

    # PSD (Meter input is kept)
    PSD = st.number_input('PSD (m)', value=0, step=1, format="%.0f")

    # Poney Rotor (feet)
    PoneyRotor = st.number_input('Poney Rotor (ft)', value=0, step=1, format="%.0f")

with col2:
    # BOP Extension Size: Whole number input and unit in one box
    BOP_value = st.number_input('BOP Extension Size', value=0, step=1, format="%.0f")
    BOP_unit = st.selectbox('Unit for BOP', ['inch', 'ft'], index=0)

    # SW: Whole number input and unit in one box
    SW_value = st.number_input('SW', value=0, step=1, format="%.0f")
    SW_unit = st.selectbox('Unit for SW', ['inch', 'ft'], index=0)

    # Clamp Size: Whole number input and unit in one box
    Clamp_value = st.number_input('Clamp Size', value=0, step=1, format="%.0f")
    Clamp_unit = st.selectbox('Unit for Clamp', ['inch', 'ft'], index=0)

    # Adapter Size: Whole number input and unit in one box
    Adapter_value = st.number_input('Adapter Size', value=0, step=1, format="%.0f")
    Adapter_unit = st.selectbox('Unit for Adapter', ['inch', 'ft'], index=0)

    # Rotor Size (Meter input kept)
    Rotor = st.number_input('Rotor Size (m)', value=0, step=1, format="%.0f")

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


