import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("google_service_account", type = GSheetsConnection)

df = conn.read(ttl="5m")

def test():
    st.write('success')



st.title('AI Task Tracker')
st.dataframe(df)
st.data_editor(df)
st.write('Task Name')
taskName = st.text_input('Task Name')

st.write('role')
Role = st.text_input('Role')
st.button('add', on_click = test)