import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

#//remove all the browser cache
st.cache_resource.clear()


job_hunt_page = st.Page("Job_hunt.py", title = "Job hunting")
page_3 = st.Page("Page_3.py", title = "Blank empty page")

pg = st.navigation([job_hunt_page,page_3])
pg.run()


#//initialize the connection that is refered in the secrets toml
conn = st.connection("google_service_account", type = GSheetsConnection)

#//create variable that capture the information in the first sheet of the gsheetinto variable df
df = conn.read(ttl="1m")


#//function to insert new data into the spreadsheet that is link to the "update button"
def update_sheet() :
    #update all the data in the Sheet titled "Sheet1" with the new data from "data_edit" variable
    conn.update(worksheet = "Sheet1", data = data_edit)





#//function to add new task into the next available row in the google sheet.
def add_task():

    #// take the data that is stored in the variable that the user has keyed into the text box.
    task_name = st.session_state.taskName2
    role = st.session_state.role2
    

    #//(from gpt) check if there is task_name and role data in the 
    if task_name and role:

        #//create a new line of data using pandas concat that will only have the task name and the role. the columns to be displayed are the task name and role. this is important so that the system knows where the dat will be placed at.
        new_data = pd.DataFrame([[task_name, role]], columns=["Task Name", "role"])
        
        #//use the concat method to append the new data line into the next available row in the google sheet.
        new = pd.concat([df,new_data])

        #*(used for testing)st.dataframe(new)
        # Append the new data to the Google Sheets
        conn.update(worksheet ="Sheet1", data = new)

        
        st.cache_resource.clear()
        # Reload the dataframe to reflect the new row
        st.rerun()

        #create an else statement if there is no data detected it will pop-up an error message that will tell the user to ensure to input all of the information necessary.



st.title('AI Task Tracker!!')

#//the form section to show the user on what they need to put in so that it can be included into the new line. the form is used so that any changes made here will not rerun the whole program.
with st.form("update data"):
    st.write("form section to put in information")
    taskName2 = st.text_input('Task Name', key = "taskName2")
    role2 = st.text_input('role' , key = "role2")
    st.form_submit_button("add", on_click = add_task)

    
#//using the streamlit data editor to displa the information from the sheet that is stored in "df" variable. dont know what is the key and num_rows is about.
data_edit = st.data_editor(df, key="my_key", num_rows = "dynamic" )
#*(used for testing)st.write(st.session_state["my_key"])

#//streamlit button to run the function of updating the google sheet with the new data table
st.button('update the sheet', on_click = update_sheet)



#st.write(taskName2)
#st.write(role2)
