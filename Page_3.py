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

testloc = df_job.at[1,"Job Title"]
st.write(df_job.shape[0])
st.write(testloc)

max_row = df_job.shape[0]
for cont in range(max_row):
    
    container_test = st.container(border = True)
    container_test.title(df_job.at[cont,"Job Title"])
    container_test.write(df_job.at[cont,"Company Name"])
    container_test.write(bool(df_job.at[cont,"Checkmark"]))
    container_test.link_button("Go To Job", df_job.at[cont,"URL link"])



container1 = st.container(border = True)
container1.write("testing")
expander2 = container1.expander("test2")
expander2.write("sdfwefwesd")
expander1 = st.expander("click to open")
expander1.write("testtesttesttesttesttesttest")