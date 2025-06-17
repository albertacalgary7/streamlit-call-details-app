
# Import python packages
import streamlit as st
# from snowflake.snowpark.context import get_active_session
import snowflake.connector

conn = snowflake.connector.connect(
    user=st.secrets["snowflake"]["rasi"],
    password=st.secrets["snowflake"]["S@njay_ram2007"],
    account=st.secrets["snowflake"]["SYJEZGI-VVB98369"],
    warehouse=st.secrets["snowflake"]["COMPUTE_WH"],
    database=st.secrets["snowflake"]["TEST_DB"],
    schema=st.secrets["snowflake"]["PUBLIC"],
    role=st.secrets["snowflake"]["ACCOUNT_ADMIN"]
)
cursor = conn.cursor()
# Write directly to the app
from datetime import datetime
submission_time = datetime.now()
 
import pandas as pd
cursor.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_TIMESTAMP()")


try:
    df = pd.DataFrame(cursor.fetchall(), columns=[col[0] for col in cursor.description])
    st.success("Connection successful!")
    #st.dataframe(df)
except Exception as e:
    st.error(f"Connection failed: {e}")
st.title("Admission Questionnaire")
with st.form("admission_form"):
    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth")
    reason = st.text_area("Primary Reason for Admission")
    suicidal = st.radio("Have you experienced suicidal thoughts recently?", ["Yes", "No"])
    meds = st.radio("Are you currently taking any medications?", ["Yes", "No"])
    med_list = st.text_input("Please list your medications") if meds == "Yes" else ""
    diagnoses = st.multiselect("History of mental health diagnoses",["Depression", "Anxiety", "Bipolar", "PTSD", "Schizophrenia", "Other"])
    emotional_state = st.slider("Rate your current emotional state", 1, 10)
    support = st.radio("Do you have a support system?", ["Yes", "No"])
    hospitalized = st.radio("Have you been hospitalized for mental health before?", ["Yes", "No"])
    emergency_contact = st.text_input("Emergency Contact Information")
  
    submitted = st.form_submit_button("Submit")


# if submitted:
#         try:
#             # Convert list to comma-separated string
#             diagnoses_str = ", ".join(diagnoses)

#             insert_query = f"""
#                 INSERT INTO TEST_DB.PUBLIC.mental_health_admissions 
#                 (timestamp, name, dob,reason, suicidal, meds, med_list, diagnoses, emotional_state, support, hospitalized, emergency_contact)
#                 VALUES (
#                     '{submission_time}',
#                     '{name}',
#                     '{dob}',
#                     '{reason}',
#                     '{suicidal}',
#                     '{meds}',
#                     '{med_list}',
#                     '{diagnoses_str}',
#                     {emotional_state},
#                     '{support}',
#                     '{hospitalized}',
#                     '{emergency_contact}'
#                 )
#             """

#             session.sql(insert_query).collect()
#             st.success("Your response has been submitted successfully.")
#         except Exception as e:
#             st.error(f"Failed to insert data: {e}")
 