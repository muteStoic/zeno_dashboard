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
    col1, col2, col3 = past_job_con.columns([2,2,1], vertical_alignment= "center", gap = "large")

    with col1 : 
        st.title(df_job.at[cont,"Job Title"])
        st.write("Company: " + df_job.at[cont,"Company Name"])

    with col2 :
        st.write("Response from company")
        
        st.button("Move forward" , key = "buttonyes"+str(rows) , use_container_width = True)
        st.button("Rejected", key= "buttonno"+str(rows) , use_container_width = True)
        with st.popover("Accepted to next step"):
            st.write("You have been accepted. Write below their response")
            company_response = st.textinput("What they reply and what is the next step")
            sche_date = st.time_input()
            sche_time = st.date_input()

        
            
        #st.text_input("", key = rows)

    with col3:
        st.checkbox("Not sent", key = rows+2)



for cont in range(max_row):
    
    checkfull = bool(df_job.at[cont, "Checkmark"])
    


    if isinstance(checkfull, bool):
        if checkfull:
            print("nil")
        else:
            create_container(cont)
            
        

