import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

#//remove all the browser cache
st.cache_resource.clear()

task_tracker = st.Page("Task_tracker.py", title = "Task Tracker")
job_hunt_page = st.Page("Job_hunt.py", title = "Job hunt Add")
page_3 = st.Page("Page_3.py", title = "Job Tracker")
page_4 = st.Page("Page_4.py", title = "Past Job")
page_5 = st.Page("Page_5.py", title = "Placeholder")

def restart():
    print("")

restart_button = st.button("restart", on_click = restart)

pg = st.navigation([task_tracker ,job_hunt_page,page_3, page_4, page_5],restart_button)
pg.run()
