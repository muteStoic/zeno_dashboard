import streamlit as st
import openai
import base64
from openai import Client
from streamlit_gsheets import GSheetsConnection

#//initialize the connection that is refered in the secrets toml
conn = st.connection("google_service_account", type = GSheetsConnection)

#//create variable that capture the information in the first sheet of the gsheetinto variable df
df_job = conn.read(worksheet = "Sheet2")

st.dataframe(df_job)