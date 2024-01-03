import streamlit as st 
import pandas as pd 
from datetime import datetime 

def read_data():  
  data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vREos55t0BcKIWlqD3_YTX4OnN2RX2_qQhYqUJL2cB9aRL3DUM_X2BCknrySUYa3fFG-khR1R2Mbk57/pub?gid=231521276&single=true&output=csv" 
  data = pd.read_csv(data_link) 

  return data  
  

def main():  
  st.title("Discipline = Freedom")   
  data = read_data() 

  start_date = datetime.strptime("2024-01-04", "%Y-%m-%d").date() 
  current_date = datetime.now().date()
  difference_in_days = (current_date - start_date).days  

  st.header(f"⌛️ Days ({difference_in_days})") 



if __name__ == '__main__':
    main()
