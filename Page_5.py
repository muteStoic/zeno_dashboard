import streamlit as st
import openai
import base64
from openai import Client
from streamlit_gsheets import GSheetsConnection
import pandas as pd



#//initialize the connection that is refered in the secrets toml
st.cache_resource.clear()
conn = st.connection("google_service_account", type = GSheetsConnection)

#//create variable that capture the information in the first sheet of the gsheetinto variable df
df_job = conn.read(worksheet = "Sheet2")
df_job_show = conn.read(worksheet = "Sheet2", usecols = [0,3,12])

  


# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Score': [85, 90, 78, 88]}
df = pd.DataFrame(data)

def rearrange():
    
    st.write("sdf")
    row_to_move = df.loc[[3]]  # Select the row as a DataFrame
    remaining_rows = df.drop(3)  # Remove the selected row
    print("def")
    df = pd.concat([row_to_move, remaining_rows], ignore_index=True)
    st.dataframe(df)  

# Move row index 2 ('Charlie') to the top
row_to_move = df.loc[[2]]  # Select the row as a DataFrame
remaining_rows = df.drop(2)  # Remove the selected row

change_position = st.text_input("what position will it be", value = 3)
st.button("update the order", on_click = rearrange)
int_change_position = int(change_position)
st.write(int_change_position)

# Concatenate with the moved row at the top
df = pd.concat([row_to_move, remaining_rows], ignore_index=True)
st.dataframe(df)        

