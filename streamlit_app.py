import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

#//remove all the browser cache
st.cache_resource.clear()

#homePage = st.Page("streamlit_app.py", title = "Homepage")
job_hunt_page = st.Page("Job_hunt.py", title = "Job hunting")
page_3 = st.Page("Page_3.py", title = "Blank empty page")

pg = st.navigation([job_hunt_page,page_3])
pg.run()
