import streamlit as st

st.set_page_config(page_title="Airline Scheduling")

st.title("Airline Scheduling and Cargo Expert System")

flight_no = st.text_input("Flight Number")

destination = st.text_input("Destination")

cargo_weight = st.number_input(
    "Cargo Weight (KG)",
    min_value=1
)

priority = st.selectbox(
    "Priority Level",
    ["Normal", "High", "Emergency"]
)

weather = st.selectbox(
    "Weather Condition",
    ["Clear", "Rainy", "Storm"]
)

if st.button("Schedule Flight"):

    aircraft = ""

    if cargo_weight <= 100:

        aircraft = "Small Aircraft"

    elif cargo_weight <= 500:

        aircraft = "Medium Aircraft"

    else:

        aircraft = "Heavy Cargo Aircraft"

    st.success("Flight Scheduled Successfully")

    st.write(f"Flight Number: {flight_no}")
    st.write(f"Destination: {destination}")
    st.write(f"Aircraft Type: {aircraft}")
    st.write(f"Priority: {priority}")

    if weather == "Storm":

        st.error("Flight Delay Due To Bad Weather")

    else:

        st.info("Flight Ready For Departure")