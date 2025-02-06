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

def rearrange(change_position):
    int_change_position = int(change_position)
    row_to_move = df.loc[[int_change_position]]  # Select the row as a DataFrame
    remaining_rows = df.drop(int_change_position)  # Remove the selected row
    print("def")
    df = pd.concat([row_to_move, remaining_rows], ignore_index=True)
    st.dataframe(df)    


# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Score': [85, 90, 78, 88]}
df = pd.DataFrame(data)

# Move row index 2 ('Charlie') to the top
row_to_move = df.loc[[2]]  # Select the row as a DataFrame
remaining_rows = df.drop(2)  # Remove the selected row

change_position = st.text_input("what position will it be")
st.button("update the order", on_click = rearrange)

# Concatenate with the moved row at the top
df = pd.concat([row_to_move, remaining_rows], ignore_index=True)
st.dataframe(df)        

