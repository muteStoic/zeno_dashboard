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

#def update_sheet():
#    conn.update(worksheet = "Sheet2", data = data_edit)

#st.button("Update sheet", on_click = update_sheet)

#data_edit = st.data_editor(df_job_show)

max_row = df_job.shape[0]

def create_container(rows):
    container_test = st.container(border = True)
    #container_test.write(bool(df_job.at[cont,"Checkmark"]))
    container_test.title(df_job.at[cont,"Job Title"])
    container_test.write("Company: " + df_job.at[cont,"Company Name"])
    container_test.write("Salary: " + df_job.at[cont, "Salary Range"])
    container_test.link_button("Go To Job", df_job.at[cont,"URL link"])
    check = container_test.checkbox("Application submitted",value = bool(df_job.at[cont,"Checkmark"]), key = cont)
    if check:
        df_job.at[cont,"Checkmark"] = True
        conn.update(worksheet ="Sheet2", data = df_job)
        
                
    expander_section = container_test.expander("Job Description")
    expander_section.write(df_job.at[cont, "Job Description"])




for cont in range(max_row):
    
    checkfull = bool(df_job.at[cont, "Checkmark"])
    


    if isinstance(checkfull, bool):
        if checkfull:
            print("nil")
        else:
            create_container(cont)
            
        

