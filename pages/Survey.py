
import streamlit as st
import pandas as pd
import plotly.express as px
import csv
import statistics as stat 
import os 

st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)
st.title("Data Collection Survey 📝")
st.write("Please fill out the form below to add your data to the dataset.")


with st.form("survey_form"):
    st.write("From Snickers, Reese Cups, and Hershey Kisses, please order them from you favorite to least favorite.")
    category1 = st.text_input("My first favorite is...")
    category2 = st.text_input("My second favorite is...")
    category3 = st.text_input("My third favorite is...")

    st.write("For each candy, how much would you say you eat per year (numbers only).")
    value1 = st.text_input("For my first favorite I eat...")
    value2 = st.text_input("For my second favorite I eat...")
    value3 = st.text_input("For my third favorite I eat...")

    submitted = st.form_submit_button("Submit Data")
    if submitted:
        try: 
            final_info = open("data.csv", "w")
            final_info.write(f"{category1},{value1}\n")
            final_info.write(f"{category2},{value2}\n")
            final_info.write(f"{category3},{value3}\n")
            final_info.close()
        except:
            st.write("An error has occured, please check that you spelled the candies correctly and that you typed out only numbers for how much you eat.")

        st.success("Your data has been submitted!")




final_info = open("data.csv", "r")
reader = csv.reader(final_info)
myDict = {}
for row in reader:
    try: 
        candy = row[0].strip()
        amount = row[1].strip()
        if len(row) >= 2:
            if candy == "Snickers" or candy == "Reese Cups" or candy == "Hershey Kisses":
                if candy not in myDict:
                    myDict[candy] = int(amount)
                else:
                    myDict[candy] += int(amount)
            else:
                st.warning("An error has occured, please check that you spelled the candies correctly with proper capitalization as show in the questions above and that no other words are used. Additionally, please check if you typed out only numbers for how much you eat. Results may calculate but could be inaccurate...")
                break
    except:
        st.warning("An error has occured, please check that you spelled the candies correctly with proper capitalization as show in the questions above and that no other words are used. Additionally, please check if you typed out only numbers for how much you eat. Results may calculate but could be inaccurate...")
        break
final_info.close()
st.bar_chart(myDict, x_label = "Favorite Candies", y_label = "Amount You've Eaten (In a Year)")



Selection = st.multiselect(
    "Choose and compare the percentages of candy you eat:",
    ["Snickers", "Reese Cups", "Hershey Kisses"], default= "Snickers")
if not Selection:
  st.warning("Please select a candy.")


if 'Selection' not in st.session_state:
    st.session_state['Selection'] = Selection
if 'Count' not in st.session_state:
    st.session_state['Count'] = []



final_info = open("data.csv", "r")
reader = csv.reader(final_info)
myPercent = {"candy_names":[], "candy_amount":[]}
count = 0
for row in reader:
    try:
        candy_name = row[0]
        candy_amount = int(row[1])
        count += candy_amount
        if len(row) >= 2:
            if candy_name in Selection:
                myPercent["candy_names"].append(candy_name)
                myPercent["candy_amount"].append(candy_amount)
    except:
        st.warning("Either no data has been given or there is missing data; results could be inaccurate...")
        break
st.session_state["Count"].append(count) 
fig = px.pie(myPercent, values = "candy_amount", names = "candy_names", title = "Candy Percentages")
st.plotly_chart(fig)
final_info.close()



final_info = open("data.csv", "r")
reader = csv.reader(final_info)
numbers = []
for row in reader:
    try: 
        if row: 
            amount = row[1].strip()
            numbers.append(int(amount))
    except:
        st.warning("Either no data has been given or there is missing data; results could be inaccurate...")
        break
if numbers:
    st.metric(label="Median of Data", value= stat.median(numbers))
    st.metric(label="Mean of Data", value= stat.mean(numbers))
final_info.close()


