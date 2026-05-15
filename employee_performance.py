import streamlit as st

st.set_page_config(page_title="Employee Evaluation")

st.title("Employee Performance Evaluation Expert System")

employee_name = st.text_input("Employee Name")

attendance = st.slider(
    "Attendance Percentage",
    0,
    100
)

task_completion = st.slider(
    "Task Completion",
    0,
    100
)

communication = st.slider(
    "Communication Skills",
    0,
    100
)

teamwork = st.slider(
    "Teamwork",
    0,
    100
)

if st.button("Evaluate Performance"):

    total = (
        attendance +
        task_completion +
        communication +
        teamwork
    ) / 4

    st.metric(
        "Overall Performance Score",
        round(total, 2)
    )

    if total >= 90:

        st.success("Excellent Employee")
        st.balloons()

    elif total >= 70:

        st.info("Good Performance")

    elif total >= 50:

        st.warning("Average Performance")

    else:

        st.error("Needs Improvement")

    st.progress(int(total))