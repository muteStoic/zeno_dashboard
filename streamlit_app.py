import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("google_service_account", type = GSheetsConnection)

df = conn.read()

st.title('AI Task Tracker')
st.dataframe(df)