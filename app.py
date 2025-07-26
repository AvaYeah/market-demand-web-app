import streamlit as st
import pandas as pd

st.title("📈 Market Demand Trend Monitor")

# Example trend data
data = {
    'Date': pd.date_range(start='2025-07-01', periods=10),
    'Search Volume': [150, 180, 200, 220, 250, 300, 320, 340, 400, 420]
}

df = pd.DataFrame(data)
st.line_chart(df.set_index('Date'))

st.write("This is a demo showing a simple market demand trend over 10 days.")

