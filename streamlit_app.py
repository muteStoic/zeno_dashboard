import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("google_service_account", type = GSheetsConnection)

df = conn.read(ttl="5m")

def add_task():
    task_name = st.session_state.taskName
    role = st.session_state.role
    
    if task_name and role:
        new_data = pd.DataFrame([[task_name, role]], columns=["Task Name", "Role"])
        st.dataframe(new_data)
        # Append the new data to the Google Sheets
        conn.update(new_data, append=True)

        

        # Reload the dataframe to reflect the new row
        st.experimental_rerun()



st.title('AI Task Tracker')
st.dataframe(df)
st.data_editor(df)
st.write('Task Name')
taskName = st.text_input('Task Name', key ="taskName" )

st.write('role')
role = st.text_input('Role', key ="role")
st.button('add', on_click = add_task)

with st.form("update data"):
    st.write("form section to put in information")
    taskName2 = st.text_input('Task Name', key = "taskName2")
    role2 = st.text_input('role' , key = "role2")
    st.form_submit_button("add", on_click = add_task)

st.write(taskName2)
st.write(role2)
