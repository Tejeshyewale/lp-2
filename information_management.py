import streamlit as st
import pandas as pd

st.set_page_config(page_title="Information Management", layout="wide")

st.title("Information Management Expert System")

if "employees" not in st.session_state:
    st.session_state.employees = []

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Employee", "Search Employee", "View Employees", "Analytics"]
)

# --------------------------------------------------------
# ADD EMPLOYEE
# --------------------------------------------------------

if menu == "Add Employee":

    st.subheader("Add Employee Details")

    col1, col2 = st.columns(2)

    with col1:
        emp_id = st.text_input("Employee ID")
        name = st.text_input("Employee Name")
        age = st.number_input("Age", 18, 60)

    with col2:
        department = st.selectbox(
            "Department",
            ["HR", "IT", "Sales", "Marketing"]
        )

        salary = st.number_input(
            "Salary",
            min_value=10000
        )

        performance = st.slider(
            "Performance Score",
            0,
            100
        )

    if st.button("Save Employee"):

        st.session_state.employees.append({
            "ID": emp_id,
            "Name": name,
            "Age": age,
            "Department": department,
            "Salary": salary,
            "Performance": performance
        })

        st.success("Employee Added Successfully")

# --------------------------------------------------------
# SEARCH EMPLOYEE
# --------------------------------------------------------

elif menu == "Search Employee":

    st.subheader("Search Employee")

    search_name = st.text_input("Enter Employee Name")

    if st.button("Search"):

        found = False

        for emp in st.session_state.employees:

            if emp["Name"].lower() == search_name.lower():

                st.json(emp)
                found = True

        if not found:
            st.error("Employee Not Found")

# --------------------------------------------------------
# VIEW EMPLOYEES
# --------------------------------------------------------

elif menu == "View Employees":

    st.subheader("Employee Database")

    if st.session_state.employees:

        df = pd.DataFrame(st.session_state.employees)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("No Employees Added")

# --------------------------------------------------------
# ANALYTICS
# --------------------------------------------------------

elif menu == "Analytics":

    st.subheader("Employee Analytics")

    if st.session_state.employees:

        df = pd.DataFrame(st.session_state.employees)

        st.metric(
            "Total Employees",
            len(df)
        )

        st.bar_chart(
            df.groupby("Department")["Salary"].mean()
        )

        st.line_chart(
            df["Performance"]
        )

    else:
        st.warning("No Data Available")