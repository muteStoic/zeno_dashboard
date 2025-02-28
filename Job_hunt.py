import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from io import StringIO
from io import BytesIO
import openai
import base64
from PIL import Image
import os
import ast
from datetime import datetime


st.cache_resource.clear()

assistandid = "asst_Tot8FMaAwWRmOAng4D6z3x66"
# Initialize session state for the thread ID if not already set
if "threadid" not in st.session_state:
    st.session_state.threadid = "your_thread_id_here"


client = openai
#//remove all the browser cache
#st.cache_resource.clear()

#//initialize the connection that is refered in the secrets toml
conn = st.connection("google_service_account", type = GSheetsConnection)

#//create variable that capture the information in the first sheet of the gsheetinto variable df
df_job = conn.read(worksheet = "Sheet2", ttl = None)
st.session_state.fulljobdata = df_job


def get_connection():
    conn = st.connection("google_service_account", type = GSheetsConnection)
    df_job = conn.read(worksheet = "Sheet2", ttl = None)



#//function to insert new data into the spreadsheet that is link to the "update button"
def update_sheet() :
    #update all the data in the Sheet titled "Sheet2" with the new data from "data_edit" variable
    conn.update(worksheet = "Sheet2", data = data_edit)





#//function to add new task into the next available row in the google sheet.
def add_task():

    #// take the data that is stored in the variable that the user has keyed into the text box.
    task_name = st.session_state.taskName2
    role = st.session_state.role2
    

    #//(from gpt) check if there is task_name and role data in the 
    if task_name and role:

        #//create a new line of data using pandas concat that will only have the task name and the role. the columns to be displayed are the task name and role. this is important so that the system knows where the dat will be placed at.
        new_data = pd.DataFrame([[task_name, role]], columns=["Job Title", "Company Name"])
        
        #//use the concat method to append the new data line into the next available row in the google sheet.
        new = pd.concat([df_job,new_data])
        st.dataframe(new)

        #*(used for testing)st.dataframe(new)
        # Append the new data to the Google Sheets
        conn.update(worksheet ="Sheet2", data = new)

        
        st.cache_resource.clear()
        

        # Reload the dataframe to reflect the new row
        st.rerun()

        #create an else statement if there is no data detected it will pop-up an error message that will tell the user to ensure to input all of the information necessary.


def rearrange():
    row_to_move = df_job.loc[[2]]  # Select the row as a DataFrame
    remaining_rows = df_job.drop(2)  # Remove the selected row
    print("def")
    df_job = pd.concat([row_to_move, remaining_rows], ignore_index=True)
    st.dataframe(df_job) 

st.button("test", on_click = rearrange)


st.title('Job hunting with AI')

#//the form section to show the user on what they need to put in so that it can be included into the new line. the form is used so that any changes made here will not rerun the whole program.
with st.form("update data"):
    st.write("form section to put in information")
    taskName2 = st.text_input('Task Name', key = "taskName2")
    role2 = st.text_input('role' , key = "role2")
    st.form_submit_button("add", on_click = add_task)

    #//using the streamlit data editor to displa the information from the sheet that is stored in "df" variable. dont know what is the key and num_rows is about.
    data_edit = st.data_editor(df_job, use_container_width = True, key="my_key", num_rows = "dynamic" )

###


st.title("OpenAI Image and Text Messaging App")

st.dataframe(df_job)
# File uploader for the image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if st.button("Send Message"):
    
    thread = client.beta.threads.create()
    st.session_state.threadid = thread.id


    


    if not uploaded_file:
        st.error("Please upload an image.")
    else:
        # Read the image content and encode it to base64
        image_bytes = uploaded_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        
        
        response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user","content": [{"type": "text","text": "You will help me to read an image to extract important data from it. The data that i required is as follows (Job Title	Job Description	Key Activities	Company Name	URL link   	Company email	PIC email	Company information	Company website	Salary Range   Requirement). Sources is the url link in the image. Put the requirement as is that is shown in the image into the data, the requirement data dont put it as an array, just separate it with a dot.save the extracted data as extracted_data. I just need the code itself and nothing else. if there is no information just put in 'nil'. Do not say anything else other than the requested information.",},{"type": "image_url","image_url": {"url": f"data:image/jpg;base64,{image_base64}"},},],}],)
        st.write(response.choices[0].message.content)

    company_full_information1 = response.choices[0].message.content#change this data to response.choices[0].message.content for full running build
    print(company_full_information1[27:-3])
    company_full_information2 = company_full_information1[27:-3]
    
    company_full_information = ast.literal_eval(company_full_information2)
    st.write(company_full_information)

    
    job_title = company_full_information["Job Title"]
    job_desc = company_full_information["Job Description"]
    key_act = company_full_information["Key Activities"]
    com_name = company_full_information["Company Name"]
    url_job = company_full_information["URL link"]
    com_email = company_full_information["Company email"]
    pic_email = company_full_information["PIC email"]
    com_inf = company_full_information["Company information"]
    com_web = company_full_information["Company website"]
    salary = company_full_information["Salary Range"]
    requirement = company_full_information["Requirement"]
    remark_data = ""
    checkmark_data = False
    time = datetime.now().strftime(" %d-%m-%Y ")

    job_data = pd.DataFrame([[job_title, job_desc, key_act, com_name, url_job, com_email, pic_email, com_inf, com_web, salary,remark_data, checkmark_data, requirement, time
]], columns=["Job Title","Job Description", "Key Activities", "Company Name", "URL link", "Company email", "PIC email", "Company information", "Company website", "Salary Range","Remark", "Checkmark", "Requirement", "Time"
])
#"Job Title","Job Description", "Key Activities", "Company Name", "URL link", "Company email", "PIC email", "Company information", "Company website", "Salary Range"
#job_title, job_desc, key_act, com_name, url_job, com_email, pic_email, com_inf, com_web, salary
#job_data = pd.DataFrame([[job_title,job_desc,key_act,com_name,url_job,com_name, url_job,com_email,pic_email,com_inf,com_web,salary]], columns=["Job Title", "Job Description","Key Activit","Company Name", "URL link", "Company email", "PIC Email","Company information", "Company website", "Salary Range"])
    st.data_editor(job_data)
    full_job = pd.concat([st.session_state.fulljobdata,job_data])
    #st.session_state.fulljobdata = full_job
    st.dataframe(st.session_state.fulljobdata)    
    conn.update(worksheet ="Sheet2", data = full_job)  
    


if st.button("Send Message2"):
    
    thread = client.beta.threads.create()
    st.session_state.threadid = thread.id


    


    if not uploaded_file:
        st.error("Please upload an image.")
    else:
        # Read the image content and encode it to base64
        image_bytes = uploaded_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        
        
        response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user","content": [{"type": "text","text": "You will help me to read an image to extract important data from it. The data that i required is as follows (Job Title	Job Description	Key Activities	Company Name	URL link   	Company email	PIC email	Company information	Company website	Salary Range   Requirement). Sources is the url link in the image. Put the requirement as is that is shown in the image into the data, the requirement data dont put it as an array, just separate it with a dot.save the extracted data as extracted_data. I just need the code itself and nothing else. if there is no information just put in 'nil'. Do not say anything else other than the requested information.",},{"type": "image_url","image_url": {"url": f"data:image/jpg;base64,{image_base64}"},},],}],)
        st.write(response.choices[0].message.content)

    company_full_information1 = response.choices[0].message.content#change this data to response.choices[0].message.content for full running build
    print(company_full_information1[27:-3])
    company_full_information2 = company_full_information1[27:-3]
    
    company_full_information = ast.literal_eval(company_full_information2)
    st.write(company_full_information)

    
    job_title = company_full_information["Job Title"]
    job_desc = company_full_information["Job Description"]
    key_act = company_full_information["Key Activities"]
    com_name = company_full_information["Company Name"]
    url_job = company_full_information["URL link"]
    com_email = company_full_information["Company email"]
    pic_email = company_full_information["PIC email"]
    com_inf = company_full_information["Company information"]
    com_web = company_full_information["Company website"]
    salary = company_full_information["Salary Range"]
    requirement = company_full_information["Requirement"]
    remark_data = ""
    checkmark_data = False
    time = datetime.now().strftime(" %d-%m-%Y ")

    job_data = pd.DataFrame([[job_title, job_desc, key_act, com_name, url_job, com_email, pic_email, com_inf, com_web, salary,remark_data, checkmark_data, requirement, time
]], columns=["Job Title","Job Description", "Key Activities", "Company Name", "URL link", "Company email", "PIC email", "Company information", "Company website", "Salary Range","Remark", "Checkmark", "Requirement", "Time"
])
#"Job Title","Job Description", "Key Activities", "Company Name", "URL link", "Company email", "PIC email", "Company information", "Company website", "Salary Range"
#job_title, job_desc, key_act, com_name, url_job, com_email, pic_email, com_inf, com_web, salary
#job_data = pd.DataFrame([[job_title,job_desc,key_act,com_name,url_job,com_name, url_job,com_email,pic_email,com_inf,com_web,salary]], columns=["Job Title", "Job Description","Key Activit","Company Name", "URL link", "Company email", "PIC Email","Company information", "Company website", "Salary Range"])
    new_con = get_connection()
    
    
    #st.data_editor(new_con)
    full_job = pd.concat([new_con,job_data])
    #st.session_state.fulljobdata = full_job
    st.dataframe(full_job)    
    conn.update(worksheet ="Sheet2", data = full_job)  





#test code of extracted data below
extracted_data = {
    "Job Title": "Project Manager",
    "Job Description": "Biji-biji Initiative is immediately seeking an experienced and driven Project Manager to lead the implementation of MCMC Microsoft AI Teach & AI for MY future.",
    "Key Activities": "Plans, executes, and manages projects with clear objectives, timelines, budgets, and metrics while ensuring risks are mitigated for successful outcomes. Engages with communities, partners, and stakeholders, fostering relationships and cross-functional collaboration to align activities with organizational goals. Oversees resources, budgets, and impact assessments, ensuring transparent financial reporting, quality assurance, and continuous improvement through stakeholder feedback.",
    "Company Name": "Biji-biji Initiative",
    "URL link": "https://linkedin.com/jobs/view/4141400195/",
    "Company email": 'nil',
    "PIC email": 'nil',
    "Company information": 'nil',
    "Company website": 'nil',
    "Salary Range": "Ranges from RM5000 until RM6500"
}
#####
##
