import streamlit as st 
import pandas as pd 
from datetime import datetime 

st.set_page_config(page_title='Discipline', page_icon='📚', layout="wide", initial_sidebar_state="auto") 

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

  st.sidebar.write("**Category 1**") 
  st.sidebar.info("Work - 55 mins", icon='🍅')  
  st.sidebar.info("Research - 55 mins", icon='📄') 
  st.sidebar.info("Startup - 55 mins", icon='🚀') 
  st.sidebar.info("Knowledge - 55 mins", icon='🪴') 
  st.sidebar.markdown("***")

  st.sidebar.write("**Category 2**") 
  st.sidebar.info("Quran time - 30 mins ", icon='🕋')
  st.sidebar.info("Russian - 30 mins", icon='🇷🇺')
  st.sidebar.info("Reading - 30 mins", icon='📘')

  st.sidebar.write("**Category 3**") 
  st.sidebar.info("Workout - 30 mins", icon='💪')
  st.sidebar.info("Free time activities - 30 mins", icon='🏓')
  st.sidebar.info("Piano - 30 mins", icon='🎹')


  st.header(f"⌛️ Days ({difference_in_days})") 

  col1, col2, col3, col4, col5 = st.columns((3, 2, 2, 2, 2)) 
  col1.write("**Date**") 
  col2.write("**Work**") 
  col3.write("**Type**") 
  col4.write("**Reaction**") 
  col5.write("**Status**")



if __name__ == '__main__':
    main()
