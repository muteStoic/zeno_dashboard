import streamlit as st
import openai
import base64
from openai import Client
from streamlit_gsheets import GSheetsConnection


#//initialize the connection that is refered in the secrets toml
st.cache_resource.clear()
conn = st.connection("google_service_account", type = GSheetsConnection)

#//create variable that capture the information in the first sheet of the gsheetinto variable df
df_job = conn.read(worksheet = "Sheet2")
df_job_show = conn.read(worksheet = "Sheet2", usecols = [0,3,12])



data_edit = st.dataframe(df_job_show)

max_row = df_job.shape[0]

def create_container(rows):
    past_job_con = st.container(border = True)
    col1, col2, col3 = past_job_con.columns([3,3,1])

    with col1 : 
        st.write("col1")

    with col2 :
        st.write("col2")

    with col3:
        st.checkbox("Not sent", key = rows)


past_job_con = st.container(border = True)
col1, col2, col3 = past_job_con.columns([3,3,1])

with col1 : 
    st.write("col1")

with col2 :
    st.write("col2")

with col3:
    st.checkbox("Not sent", key = "test")


for cont in range(max_row):
    
    checkfull = bool(df_job.at[cont, "Checkmark"])
    


    if isinstance(checkfull, bool):
        if checkfull:
            print("nil")
        else:
            create_container(cont)
            
        

