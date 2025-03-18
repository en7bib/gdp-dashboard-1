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
col1, col2 = st.columns([3, 1])  # Adjusting column size ratio for the layout

with col1:
    # Whole number input for PL Size
    PL_value = st.number_input('PL Size', value=0, step=1)  # No format string here

with col2:
    # Unit for PL
    PL_unit = st.selectbox('', ['inch', 'ft'], index=0, key='PL_unit', label_visibility="collapsed")
    st.markdown("<style>div[role='listbox'] { font-size: 12px; }</style>", unsafe_allow_html=True)  # Custom CSS to make the unit smaller

with col1:
    # SO: Whole number input
    SO_value = st.number_input('SO', value=0, step=1)  # No format string here

with col2:
    # Unit for SO
    SO_unit = st.selectbox('', ['inch', 'ft'], index=0, key='SO_unit', label_visibility="collapsed")
    st.markdown("<style>div[role='listbox'] { font-size: 12px; }</style>", unsafe_allow_html=True)

with col1:
    # DH: Whole number input
    DH_value = st.number_input('DH', value=0, step=1)  # No format string here

with col2:
    # Unit for DH
    DH_unit = st.selectbox('', ['inch', 'ft'], index=0, key='DH_unit', label_visibility="collapsed")
    st.markdown("<style>div[role='listbox'] { font-size: 12px; }</style>", unsafe_allow_html=True)

with col1:
    # Min Stickup: Whole number input
    MinStickup_value = st.number_input('Min Stickup', value=0, step=1)  # No format string here

with col2:
    # Unit for Min Stickup
    MinStickup_unit = st.selectbox('', ['inch', 'ft'], index=0, key='MinStickup_unit', label_visibility="collapsed")
    st.markdown("<style>div[role='listbox'] { font-size: 12px; }</style>", unsafe_allow_html=True)

# PSD (Meter input is kept)
PSD = st.number_input('PSD (m)', value=0, step=1)

# Poney Rotor (feet)
PoneyRotor = st.number_input('Poney Rotor (ft)', value=0, step=1)

# Add some spacing for better UI on mobile devices
st.write("\n" * 2)

# Button to calculate the results
if st.button('Calculate'):
    # Convert all inputs to inches for calculation
    PL = to_inches(PL_value, PL_unit)
    BOP = to_inches(0, 'inch')  # Default values can be assigned for others (if needed)
    SO = to_inches(SO_value, SO_unit)
    SW = to_inches(0, 'inch')
    DH = to_inches(DH_value, DH_unit)
    Clamp = to_inches(0, 'inch')
    MinStickup = to_inches(MinStickup_value, MinStickup_unit)
    Adapter = to_inches(0, 'inch')

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



