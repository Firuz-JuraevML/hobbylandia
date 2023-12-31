import streamlit as st 
import pandas as pd 
from datetime import datetime 

st.set_page_config(page_title='Book Marathon', page_icon='📚', layout="wide", initial_sidebar_state="auto") 

def read_data(): 
  data_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vREos55t0BcKIWlqD3_YTX4OnN2RX2_qQhYqUJL2cB9aRL3DUM_X2BCknrySUYa3fFG-khR1R2Mbk57/pub?gid=0&single=true&output=csv" 
  data = pd.read_csv(data_link) 

  return data 

def main(): 
  books_df = read_data() 
  
  start_date = datetime.strptime("2023-11-05", "%Y-%m-%d").date() 
  current_date = datetime.now().date()
  difference_in_days = (current_date - start_date).days  

  st.sidebar.write("Start date: November 5, 2023") 
  st.sidebar.write(f"Days: {difference_in_days}")
  st.sidebar.write(f"Completed books: {books_df[books_df.status == 'Done'].shape[0]}")
   
  st.title(f"📚 Books ({books_df.shape[0]})") 
 
  col1, col2, col3, col4, col5 = st.columns((3, 2, 2, 1, 2)) 
  col1.write("**Book name**") 
  col2.write("**Author**") 
  col3.write("**Type**") 
  col4.write("**Reaction**") 
  col5.write("**Status**") 
  
  for i in range(books_df.shape[0]): 
    col1, col2, col3, col4, col5 = st.columns((3, 2, 2, 1, 2)) 
    col1.write(f"📕 {books_df.iloc[i].book_name}") 
    col2.write(books_df.iloc[i].author)
    col3.write(books_df.iloc[i].type)
    col4.write(books_df.iloc[i].reaction)
    col5.write(books_df.iloc[i].status)
      

if __name__ == '__main__':
    main() 
