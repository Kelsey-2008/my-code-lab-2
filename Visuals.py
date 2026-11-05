# This creates the page for displaying data visualizations.

import streamlit as st
import pandas as pd
import json
import csv
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
st.subheader("Maximum profits from 2020-2025")
source = open("data.json")
loaded = json.load(source)
source.close()
points = pd.DataFrame(loaded)

s_prof = 0
r_prof = 0
h_prof = 0
mydict = {}
for block in loaded:
    if block["Name"] == "Snickers" and block["Profit"] > s_prof:
        s_prof = block["Profit"]
    if block["Name"] == "Reese Cups" and block["Profit"] > r_prof:
        r_prof = block["Profit"]
    if block["Name"] == "Hershey Kisses" and block["Profit"] > h_prof:
        h_prof = block["Profit"]
mydict["Snickers"] = s_prof
mydict["Reese Cups"] = r_prof
mydict["Hershey Kisses"] = h_prof


st.bar_chart(mydict, x_label = "Candies", y_label = "Max Profit (in millions)")

#----------------------------------------

Selection = st.multiselect(
    "Choose Your Candy Profits from 2020-2025:",
    ["Snickers", "Reese Cups", "Hershey Kisses"])
if Selection == []:
    st.warning("Please select at least one candy else the default is to show all candy profits from 2020-2025.")

if 'my_select' not in st.session_state:
    st.session_state['my_select'] = Selection

import altair as alt

source = open("data.json")
loaded = json.load(source)
source.close()

show = []
if "Snickers" in Selection:
    for lines in loaded:
        if lines["Name"] == "Snickers":
            s_dict = {}
            s_dict["Profit"] = lines["Profit"]
            s_dict["Year"] = lines["Year"]
            s_dict["Candy"] = lines["Candy"]
            show.append(s_dict)
if "Reese Cups" in Selection:
    for lines in loaded:
        if lines["Name"] == "Reese Cups":
            r_dict = {}
            r_dict["Profit"] = lines["Profit"]
            r_dict["Year"] = lines["Year"]
            r_dict["Candy"] = lines["Candy"]
            show.append(r_dict)
if "Hershey Kisses" in Selection:
    for lines in loaded:
        if lines["Name"] == "Hershey Kisses":
            h_dict = {}
            h_dict["Profit"] = lines["Profit"]
            h_dict["Year"] = lines["Year"]
            h_dict["Candy"] = lines["Candy"]
            show.append(h_dict)
if show == []:
    st.write()
else:
    points= pd.DataFrame(show)

chart = alt.Chart(points).mark_circle().encode(
    x= alt.X("Year:Q", scale=alt.Scale(domain=[19, 26], nice=False), axis=alt.Axis(format='d', tickMinStep=1)),
    y=alt.Y("Profit:Q", title="Profit (in millions)"),
    color=alt.Color("Candy:N", title="Candy"),
    tooltip=["Year", "Profit", "Candy"]
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])


with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)


# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
