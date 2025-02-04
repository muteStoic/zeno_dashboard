import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from io import StringIO
import openai
import base64
from PIL import Image
import os


assistandid = "asst_Tot8FMaAwWRmOAng4D6z3x66"

client = openai
#//remove all the browser cache
#st.cache_resource.clear()

#//initialize the connection that is refered in the secrets toml
conn = st.connection("google_service_account", type = GSheetsConnection)

#//create variable that capture the information in the first sheet of the gsheetinto variable df
df_job = conn.read(worksheet = "Sheet2")


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



st.title('Job hunting with AI')

#//the form section to show the user on what they need to put in so that it can be included into the new line. the form is used so that any changes made here will not rerun the whole program.
with st.form("update data"):
    st.write("form section to put in information")
    taskName2 = st.text_input('Task Name', key = "taskName2")
    role2 = st.text_input('role' , key = "role2")
    st.form_submit_button("add", on_click = add_task)

    #//using the streamlit data editor to displa the information from the sheet that is stored in "df" variable. dont know what is the key and num_rows is about.
    data_edit = st.data_editor(df_job, use_container_width = True, key="my_key", num_rows = "dynamic" )


    
#*(used for testing)st.write(st.session_state["my_key"])

#//streamlit button to run the function of updating the google sheet with the new data table
st.button('update the sheet', on_click = update_sheet)



#st.write(taskName2)
#st.write(role2)

################################################################################
#def run_open_AI():


def encode_image(image_path):
    


    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")



def chat_with_openai_text_and_image():
    st.write(uploaded_file1)
    image_path = uploaded_file1._file_urls.upload_url
    st.session_state.fileurl = "job1jpg.jpg"
    st.write(st.session_state.fileurl)

    # Getting the Base64 string
    base64_image = encode_image(st.session_state.fileurl)
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user","content": [{"type": "text","text": "What is in this image?",},{"type": "image_url","image_url": {"url": f"data:image/jpg;base64,{base64_image}"},},],}],)
    st.write(response)

    
   
    
    """
    text_prompt = "what can you tell about this image"
    image_path = uploaded_file1
    thread = client.beta.threads.create()
    st.session_state.threadid = thread.id
    st.write(st.session_state.threadid)

    message = client.beta.threads.messages.create(
    thread_id=st.session_state.threadid,
    role="user",
    content= "",
    filename = image_path
    )

    run = client.beta.threads.runs.create_and_poll(
    thread_id=st.session_state.threadid,
    assistant_id=assistandid  
    )

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(thread_id=st.session_state.threadid)
        print(messages)

        last_message = messages.data[0]
        response = last_message.content[0].text.value
        print(response)
        st.session_state.ai_generate = response
        #ai_generate.append(response)
        st.write(st.session_state.ai_generate)

    return

    """

    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text_prompt}
        ],
        #files=[{"name": "image.png", "data": image_bytes}]
        files = image_path
    )

    st.write(response['choices'][0]['message']['content'])

    return 


    
    #while run.status != "completed":
        #time.sleep(1)
        #print(run.status)

    """

    


st.button("normal button", on_click = chat_with_openai_text_and_image)


def add_image():
    new_data = pd.DataFrame([[uploaded_file1, uploaded_file1]], columns=["Job Title", "Company Name"])
    st.write(new_data)
    








uploaded_file1 = st.file_uploader("Choose a file")

st.button("upload image to sheet", on_click = add_image)



@st.cache_data(ttl=3600)
def load_image(uploaded_file):
    if uploaded_file is not None:
        st.write(uploaded_file)
        try:
            image = Image.open(uploaded_file)
            return image
        except Exception as e:
            st.error(f"Error loading image: {e}")
            return None
    return None


#uploaded_file1 = st.file_uploader("Choose a file")
#if uploaded_file1 is not None:
    # To read file as bytes:
#    bytes_data = uploaded_file1.getvalue()
    #st.write(bytes_data)

    #dataframe = pd.DataFrame(uploaded_file1)
    #st.write(dataframe)

    #upload_url: "/_stcore/upload_file/29b2669b-cbba-4448-a030-709a273e4da2/463503d4-bb78-4035-98a7-ab369f0be6f5"


uploaded_file = st.file_uploader("1111Upload your image (JPEG, PNG, etc.)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Call the cached function
    image = load_image(uploaded_file)

    if image is not None:
        st.write("Image successfully loaded!")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Display the time when the image was processed (current session)
        #st.write(f"Image processed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.info("Please upload an image to proceed.")
