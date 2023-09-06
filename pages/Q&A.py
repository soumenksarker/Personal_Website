import sqlite3
#import torch
import streamlit as st
from streamlit_chat import message as st_message
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration
conn = sqlite3.connect('data.db')
c=conn.cursor()
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,password TEXT)')
def add_userdata(username, password):
    c.execute('INSERT INTO usertable(username, password) VALUES (?,?)',(username, password))
    conn.commit()
def login_user(username, password):
    c.execute('SELECT * FROM usertable WHERE username=? AND password=?', (username, password))
    data = c.fetchall()
    return data
def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data
st.subheader("SignUp to get access ...")
choice = option_menu(menu_title=None,
options= ["Login","SignUp"], 
icons=['Houses','book'],
menu_icon="cast",
default_index=0,
orientation="horizontal"
)
st.title("Simple Chatbot for fun!")
if choice == "Login":
    #st.session_state.history=[]
    st.subheader("Login Section")
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')
    if st.checkbox("Login"):
        create_usertable()
        result=login_user(username, password)
        if result:
            st.success("Welcome, Logged In as {} .. feelng bored! Conversate ..".format(username))
            @st.experimental_singleton
            def get_models():
                # it may be necessary for other frameworks to cache the model
                # seems pytorch keeps an internal state of the conversation
                model_name = "facebook/blenderbot-400M-distill"
                tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
                model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
                return tokenizer, model
            if "history" not in st.session_state:
                st.session_state.history = []
            st.title("Hello Chatbot")
            def generate_answer():
                tokenizer, model = get_models()
                user_message = st.session_state.input_text
                inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
                result = model.generate(**inputs)
                message_bot = tokenizer.decode(
                    result[0], skip_special_tokens=True
                )  # .replace("<s>", "").replace("</s>", "")
                st.session_state.history.append({"message": user_message, "is_user": True})
                st.session_state.history.append({"message": message_bot, "is_user": False})
            from copyreg import clear_extension_cache
            for chat in st.session_state.history:
                st_message(**chat) 
                # unpacking
            st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)
        else:
           st.warning("Incorrect Username/Password")
    else:
       st.session_state.history = []

elif choice == "SignUp":
    st.subheader("Register Here!")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    if st.button("SignUp"):
        create_usertable()
        add_userdata(new_user, new_password)
        st.success("You have successfully created a valid Account")
        st.info("Login to continue ...")
