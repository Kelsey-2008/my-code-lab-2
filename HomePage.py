# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# Remember this cite: https://www.inthekitchenwithmatt.com/most-popular-candy-in-america

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Web Development Lab02 📊")
st.header("CS 1301")
st.subheader("Web Development - Section C")
st.subheader("Kelsey Blair")

# INTRODUCTORY TEXT
st.write("""
This websites purpose is to show you the statistics or numbers of the most eaten candines in the US.
You may use the sidebar on the left to navigate to the different pages.

### How to use this app:
- **Survey Page**: Compare how much candy you eat per year from the most eaten candies in the US!
- **Visuals Page**: Look at the most eaten candies in the US and their profits!

Hope you find something interesting or surprising!
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
