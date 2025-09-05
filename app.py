import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hello PlotTwist", page_icon="📊")

st.title("✅ Deployment Test — PlotTwist")
st.write("If you see this running on Streamlit Cloud, deployment is working fine!")

# Simple DataFrame
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [100, 120, 90, 150]
}
df = pd.DataFrame(data)

st.subheader("Sample Data")
st.dataframe(df)

st.subheader("Chart")
st.line_chart(df.set_index("Month"))
