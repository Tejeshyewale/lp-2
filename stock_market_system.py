import streamlit as st
import random

st.set_page_config(page_title="Stock Market System")

st.title("Stock Market Trading Expert System")

stock = st.selectbox(
    "Select Stock",
    ["TCS", "Infosys", "Reliance", "HDFC"]
)

market = st.selectbox(
    "Market Trend",
    ["Bullish", "Bearish", "Stable"]
)

risk = st.slider(
    "Risk Percentage",
    0,
    100
)

investment = st.number_input(
    "Investment Amount",
    min_value=1000
)

if st.button("Predict Trading Decision"):

    predicted_profit = random.randint(1000, 10000)

    if market == "Bullish" and risk < 50:

        decision = "BUY"

    elif market == "Bearish":

        decision = "SELL"

    else:

        decision = "HOLD"

    st.success(f"Trading Decision: {decision}")

    st.metric(
        "Expected Profit",
        f"₹{predicted_profit}"
    )

    st.line_chart(
        [10, 20, 30, 25, 40, 60]
    )