import streamlit as st

st.title("Log Analytics Dashboard")

st.sidebar.title("Menu")
choice = st.sidebar.selectbox("Select option", ["Home", "About","contact-us"])

uploaded_file = st.file_uploader("Upload File")

if uploaded_file is not None:
    st.success("File uploaded successfully!")

  
    try:
        content = uploaded_file.read().decode("utf-8")
        lines = content.split("\n")

        st.subheader("Preview of File")
        st.text("\n".join(lines[:10]))  

    except:
        st.warning("Cannot preview this file type (binary or unsupported)")

day = st.selectbox(
    "Select Day",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

st.write("Selected Day:", day)


#Basic Examples using streamlit
#pip install streamlit ->comment for installation of streamlit
#streamlit run pratice.py(file_name) -> comment for running the streamlit application
#for streamlit title
st.title("Log Analytics Dashboard")
#for inputs:
name = st.text_input("Enter your name")
#age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
age = st.slider("Enter your age", min_value=0, max_value=120, step=1)
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old!")
    st.success("Form submitted successfully!")
#display table data

import pandas as pd

data = {"Name" :["SaiKumar", "Venkat"],"Ages": [20, 22], "locations": ["Macherial","Khamamam"]}

df = pd.DataFrame(data)

st.write(df)
#plotly:plotly is a python visualization library that allows you to create interactive and visually appealing charts and graphs. It provides a wide range of chart types, including line charts, bar charts, scatter plots, pie charts, and more. Plotly is built on top of the JavaScript library D3.js and can be used in Python through the plotly.py library. It is commonly used for data visualization in various fields such as data science, analytics, and web development.
#It gives the interactive graphs
#we can able to zoom in and out of the graph
#streamlit->used to create web applications  
#plotly->used to create interactive graphs and charts
#together->builds live dashboards
#install ->pip install plotly

data = {
    "minute": [
        "10:00", "10:01", "10:02", "10:03", "10:04",
        "10:05", "10:06", "10:07", "10:08", "10:09"
    ],
    "error_count": [
        5, 7, 6, 8, 50, 9, 6, 55, 7, 8
    ],  # spikes = anomalies
    "service": [
        "auth", "payment", "inventory", "shipping", "user",
        "orders", "auth", "payment", "inventory", "shipping"
    ]
}
import plotly.express as px
df = pd.DataFrame(data)
st.subheader("Error Trend")
fig_line = px.line(df, x="minute", y="error_count", title="Errors Over Time")
anomalies = df[df["error_count"] > 30]

fig_line.add_scatter(
    x=anomalies["minute"],
    y=anomalies["error_count"],
    mode="markers",
    name="Anomalies"
)

st.plotly_chart(fig_line)


st.subheader("Error Count by Service (Bar Chart)")
fig_bar = px.bar(
    df,
    x="service",
    y="error_count",
    color="service",
    title="Errors by Service"
)
st.plotly_chart(fig_bar)


st.subheader("Service Distribution (Pie Chart)")
fig_pie = px.pie(
    df,
    names="service",
    values="error_count",
    title="Error Distribution by Service"
)
st.plotly_chart(fig_pie)


st.subheader("Error Scatter Analysis")
fig_scatter = px.scatter(
    df,
    x="minute",
    y="error_count",
    color="service",
    size="error_count",
    title="Error Scatter Plot"
)
st.plotly_chart(fig_scatter)


st.subheader("Error Frequency Distribution (Histogram)")
fig_hist = px.histogram(
    df,
    x="error_count",
    nbins=10,
    title="Error Count Distribution"
)
st.plotly_chart(fig_hist)