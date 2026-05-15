import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Help Desk System")

st.title("Help Desk Management Expert System")

ticket_id = st.text_input("Ticket ID")

employee = st.text_input("Employee Name")

issue = st.selectbox(
    "Select Issue",
    [
        "Network Problem",
        "Printer Error",
        "Login Failure",
        "Software Crash"
    ]
)

priority = st.selectbox(
    "Priority",
    ["Low", "Medium", "High"]
)

if st.button("Generate Solution"):

    solution = ""

    if issue == "Network Problem":
        solution = "Restart Router and Check Cable"

    elif issue == "Printer Error":
        solution = "Reconnect Printer and Install Drivers"

    elif issue == "Login Failure":
        solution = "Reset Password"

    else:
        solution = "Reinstall Software"

    st.success("Issue Analysis Completed")

    st.write(f"Ticket ID: {ticket_id}")
    st.write(f"Employee: {employee}")
    st.write(f"Issue: {issue}")
    st.write(f"Priority: {priority}")
    st.write(f"Solution: {solution}")

    st.info(f"Generated At: {datetime.now()}")