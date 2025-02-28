import streamlit as st
import openai
import base64
from openai import Client
from streamlit_gsheets import GSheetsConnection
import pandas as pd



#//initialize the connection that is refered in the secrets toml
st.cache_resource.clear()


#//create variable that capture the information in the first sheet of the gsheetinto variable df

def call_con():
    conn = st.connection("google_service_account", type = GSheetsConnection)
    df_job = conn.read(worksheet = "Sheet3", ttl = None)
    df_job_show = conn.read(worksheet = "Sheet3", ttl = None)
    df_pd = pd.DataFrame(df_job_show)
    st.dataframe(df_pd)
    
    return df_pd

def update_con(x):
    conn2 = st.connection("google_service_account", type = GSheetsConnection)
    df_job_show = conn2.read(worksheet = "Sheet3")
    df_pd = pd.DataFrame(df_job_show)
    conn2.update(worksheet = "Sheet3", data = x)
    


data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Score': [85, 90, 78, 88]}
df2 = pd.DataFrame(data2)


# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Score': [85, 90, 78, 88]}
df = pd.DataFrame(data)

def rearrange(x):
    df = pd.DataFrame(data)
    
    st.write("sdf")
    row_to_move = df.loc[[x]]  # Select the row as a DataFrame
    remaining_rows = df.drop(x)  # Remove the selected row
    print("def")
    df = pd.concat([row_to_move, remaining_rows], ignore_index=True)
    st.dataframe(df)  

# Move row index 2 ('Charlie') to the top
#row_to_move = df.loc[[2]]  # Select the row as a DataFrame
#remaining_rows = df.drop(2)  # Remove the selected row

with st.form("update data"):
    change_position = st.text_input("what position will it be", value = 0)
    int_change_position = int(change_position)
    st.write(int_change_position)
    st.form_submit_button("update the order", on_click = rearrange(int_change_position))


newName = st.text_input("name")
if st.button("Run"):
    newdata = {'Name': [newName],'Score':[10]}
    datainsert = pd.DataFrame(newdata)
    st.dataframe(datainsert)
    wee = call_con()
    df = pd.concat([wee,datainsert])
    update_con(df)


    #conn.update(worksheet ="Sheet2", data = full_job)  

    st.dataframe(df)



#st.dataframe(df2)

# Concatenate with the moved row at the top
#df = pd.concat([row_to_move, remaining_rows], ignore_index=True)
#st.dataframe(df)        

