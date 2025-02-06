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

testloc = df_job.at[1,"Job Title"]###
st.write(df_job.shape[0])###
st.write(testloc)###

max_row = df_job.shape[0]
for cont in range(max_row):
    #def test():
    #    df_job.at[cont,"Checkmark"] = True
    #    st.dataframe(df_job)
    checkfull = bool(df_job.at[cont, "Checkmark"])

    if checkfull():
        st.write("dfd")

    container_test = st.container(border = True)
    container_test.write(bool(df_job.at[cont,"Checkmark"]))
    container_test.title(df_job.at[cont,"Job Title"])
    container_test.write("Company: " + df_job.at[cont,"Company Name"])
    container_test.write("Salary: " + df_job.at[cont, "Salary Range"])
    container_test.link_button("Go To Job", df_job.at[cont,"URL link"])
    check = container_test.checkbox("Application submitted",value = bool(df_job.at[cont,"Checkmark"]), key = cont)
    if check:
        df_job.at[cont,"Checkmark"] = True
        st.dataframe(df_job)
    expander_section = container_test.expander("Job Description")
    expander_section.write(df_job.at[cont, "Job Description"])



container1 = st.container(border = True)
container1.write("testing")
expander2 = container1.expander("test2")
expander2.write("sdfwefwesd")
expander1 = st.expander("click to open")
expander1.write("testtesttesttesttesttesttest")