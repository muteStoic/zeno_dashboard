import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

#load secrets
service_account_information = st.secrets["google_service_account"]

#authenticate
credentials = Credentials.from_service_info(service_account_information)
gc = gspread.authorize(credentials)

#connect to the google sheet
sheet_url = "https://docs.google.com/spreadsheets/d/1sB1IGUYyNANw_WOH4kjqHDL60Exg1ocSX4arN-fE3FY/edit"
sheet = gc.open_by_url(sheet_url).sheet1

#fetch data
data = sheet.get_all_records()

st.dataframe(data)





st.title('AI Task Tracker')
