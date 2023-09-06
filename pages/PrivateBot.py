from streamlit_extras.switch_page_button import switch_page
import streamlit as st
if st.button("chat"):
  switch_page("chatbot")
