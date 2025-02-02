import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("google_service_account", type = GSheetsConnection)

df = conn.read(ttl="5m")

st.title('AI Task Tracker')
st.dataframe(df)
st.data_editor(df)
st.write('Task Name')

st.write('role')