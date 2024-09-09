import streamlit as st 
import pandas as pd 
from datetime import datetime 

st.set_page_config(page_title='Turnikman', page_icon='🏋‍♂️', layout="wide", initial_sidebar_state="auto") 

def read_data(): 
  data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vREos55t0BcKIWlqD3_YTX4OnN2RX2_qQhYqUJL2cB9aRL3DUM_X2BCknrySUYa3fFG-khR1R2Mbk57/pub?gid=622885771&single=true&output=csv" 
  data = pd.read_csv(data_link) 

  return data 

def main(): 
  data = read_data() 
  
  start_date = datetime.strptime("2024-09-09", "%Y-%m-%d").date() 
  current_date = datetime.now().date()
  difference_in_days = (current_date - start_date).days  

  st.sidebar.write("Start date: September 9, 2024") 
  st.sidebar.write(f"Days: {difference_in_days}")
  st.sidebar.write(f"Total pullups: {data.total.sum()}")
   
  st.title(f"🏋‍♂️ Turnikman") 
 
  col1, col2, col3, col4, col5 = st.columns((3, 2, 2, 2, 2)) 
  col1.write("**Date**") 
  col2.write("**Max**") 
  col3.write("**Total**") 
  col4.write("**Type**")
  col5.write("**Record**") 

  
  for i in range(data.shape[0]): 
    col1, col2, col3, col4, col5 = st.columns((3, 2, 2, 2, 2)) 
    col1.write(f"📆 {data.iloc[i].sana}") 
    col2.write(data.iloc[i].maximal)
    col3.write(data.iloc[i].total)
    col4.write(data.iloc[i].type)
    col5.write(data.iloc[i].record)
      

if __name__ == '__main__':
    main() 
