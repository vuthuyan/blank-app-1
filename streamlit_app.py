import streamlit as st

st.title("Credit Card Approval Project ")

st.header(" Age")
age = st.slider("seclect your age", 26, 73, 26)

st.header(" Gender")
gender = st.selectbox(
    "Gender",
    ("F","M"),
)
st.header("Dependent count")
Dependents_count= st.slider("seclect your dependents", 0, 5, 0)

st.header(" Education Level")
Education_Level = st.selectbox(
    "Education",
    ("High School","Graduate","Uneducated","Unknown","College","Post-Graduate","Doctorate"),
)

st.header(" Marital Status")
Marital_Status = st.selectbox(
    "Marital Status",
    ("Married","Single","Divorced","Unknown",),
)

st.header(" Income_Category")
Income_Category = st.selectbox(
    "Income Category",
    ("Less than $40K","$40K - $60K","$60K - $80K","$80K - $120K", "$120K +","Unkown",),
)

st.header(" Months_on_book")
months_on_book = st.slider("seclect months", 13, 54, 13)

st.header(" Total_Relationship_Count")
Total_Relationship_Count = st.selectbox(
    "Total_Relationship_Count",
    ("1","2","3","4", "5","6",),
)

st.header(" Months_Inactive_12_mon")
Months_Inactive_12_mon = st.selectbox(
    "Months_Inactive_12_mon",
    ("0","1","2","3","4", "5","6",),
)

st.header("Contacts_Count_12_mon")
Contacts_Count_12_mon = st.selectbox(
    "Contacts_Count_12_mon",
    ("0","1","2","3","4", "5","6",),
)

# st.header("Credit_Limit")
# Credit_Limit= st.slider("Select credit card limit", 1438.3, 34516.0, 1438.3,0.3)

st.header("Credit_Limit")
Credit_Limit = st.number_input("Enter a number ( max 34516)", min_value=0.0, max_value=34516.0, value=0.0,key="1")

st.header("Total_Revolving_Bal")
Total_Revolving_Bal = st.number_input("Enter revolving balance ", min_value=0.0, value=0.0,key="2")

st.header("Avg_Open_To_Buy")
Avg_Open_To_Buy = st.number_input("Enter a number ", min_value=0.0, value=0.0,key="3")

st.header("Total_Amt_Chng_Q4_Q1")
Total_Amt_Chng_Q4_Q1 = st.number_input("Enter a number ", min_value=0.0, value=0.0, key ="4")

st.header("Total_Trans_Amt")
Total_Trans_Amt = st.number_input("Enter a number ", min_value=0.0, value=0.0,key ="5")

st.header("Total_Trans_Ct")
Total_Trans_Ct = st.number_input("Enter a number ", min_value=0.0, value=0.0,key ="6")

st.header("Total_Ct_Chng_Q4_Q1")
Total_Ct_Chng_Q4_Q1 = st.number_input("Enter a number ", min_value=0.0, value=0.0,key ="7")

st.header("Avg_Utilization_Ratio")
Avg_Utilization_Ratio = st.number_input("Enter a number ", min_value=0.0, value=0.0,key ="8")

import pandas as pd
d = {
    'Customer_Age': age,
    'Dependent_count': Dependents_count,
    'Months_on_book': months_on_book,
    'Total_Relationship_Count': Total_Relationship_Count,
    'Months_Inactive_12_mon': Months_Inactive_12_mon,
    'Contacts_Count_12_mon': Contacts_Count_12_mon,
    'Credit_Limit': Credit_Limit,
    'Total_Revolving_Bal': Total_Revolving_Bal,
    'Avg_Open_To_Buy': Avg_Open_To_Buy,
    'Total_Amt_Chng_Q4_Q1': Total_Amt_Chng_Q4_Q1,
    'Total_Trans_Amt': Total_Trans_Amt,
    'Total_Trans_Ct': Total_Trans_Ct,
    'Total_Ct_Chng_Q4_Q1': Total_Ct_Chng_Q4_Q1,
    'Avg_Utilization_Ratio': Avg_Utilization_Ratio,
    'Gender_F': False,
    'Gender_M': False,
    'Education_Level_College': False,
    'Education_Level_Doctorate': False,
    'Education_Level_Graduate': False,
    'Education_Level_High School': False,
    'Education_Level_Post-Graduate': False,
    'Education_Level_Uneducated': False,
    'Education_Level_Unknown': False,
    'Marital_Status_Divorced': False,
    'Marital_Status_Married': False,
    'Marital_Status_Single': False,
    'Marital_Status_Unknown': False,
    'Income_Category_$120K +': False,
    'Income_Category_$40K - $60K': False,
    'Income_Category_$60K - $80K': False,
    'Income_Category_$80K - $120K': False,
    'Income_Category_Less than $40K':False,
    'Income_Category_Unknown': False,
    'Card_Category_Blue': False,
    'Card_Category_Gold': False,
    'Card_Category_Platinum': False,
    'Card_Category_Silver': False
}
if gender == 'F': 
    d['Gender_F'] = True
else:
    d['Gender_M'] = True
Education_Level = "Education_Level_" + Education_Level
d[Education_Level] =True

Marital_Status ="Marital_Status_" + Marital_Status
d[Marital_Status] = True

Income_Category = "Income_Category_" + Income_Category
d[Income_Category] = True

df = pd.DataFrame(data = d, index =[0])
st.dataframe(df)

import joblib 
new_model = joblib.load("random_forest_model.pkl")
new_model.predict(df)
st.write(new_model.predict(df))

