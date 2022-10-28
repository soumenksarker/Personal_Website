import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3
#import torch
from streamlit_chat import message as st_message
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration
selected = option_menu(menu_title=None,
options= ["Certifications & Projects","Live Chat"], 
icons=['bookmarks fill', "chat-dots"],
menu_icon="cast",
default_index=0,
orientation="horizontal")
if selected=="Certifications & Projects":
    option = option_menu(menu_title=None,
    options= ["Problem Solving", "Data Science Courses & Projects","ML/DL courses & Projects"], 
    icons=['boxes', 'book','bookmarks-fill'],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
    )
    
    if option=="Problem Solving":
        Certificates = {
            "🏆 Problem Solving with Algorithm and Data Structures.": "https://github.com/soumenksarker/DS-and-Algs-with-solved-problems",
            "🏆 Algorithmic Toolbox": "https://github.com/soumenksarker/Algorithmic-Toolbox-by-UCSan-Diego-Coursera",
            }
        st.write('\n')
        st.subheader("Accomplishments")
        st.write("---")
        for cer, link in Certificates.items():
            st.write(f"[{cer}]({link})")

    elif option=="Data Science Courses & Projects":
        Certificates = {
            "🏆 SQL Summer Camp": "https://drive.google.com/file/d/1HLNeCdKLPGMXIk75HTTRSxMnKr1KXTe5/view",
            "🏆 Advanced SQL": "https://www.kaggle.com/learn/certification/soumensarker/advanced-sql",
            "🏆 Python for Data Science": "https://app.dataquest.io/verify_cert/7VVAFYTSJ4MNBZXUH5ZJ/",
            "🏆 Functions Advanced":"https://app.dataquest.io/view_cert/IIUZ2JM70ZJKGZ1PWDQ1/",
            "🏆 Git and Version control":"https://app.dataquest.io/view_cert/HNQOZGVCSKV08XKOKV1F/",
            "🏆 Spark and Map-Reduce":"https://app.dataquest.io/view_cert/F7PXZE98GI9ARBD9SCM8/",
            }
        st.write('\n')
        st.subheader("Accomplishments")
        st.write("---")
        for cer, link in Certificates.items():
            st.write(f"[{cer}]({link})")
    elif option=="ML/DL courses & Projects":
        Certificates = {
            "🏆 Machine Learning": "https://www.coursera.org/account/accomplishments/verify/F5ENWFZKEZPY",
            "🏆 Deep Learning Specialization": "https://www.credly.com/badges/0de15cac-795a-4f08-825c-752cb2672784/public_url",
            "🏆 DeepLearning.AI TensorFlow Developer": "https://coursera.org/share/62fe272f9bed07392226d1137bf09f2b",
            "🏆 Complete Responsive Web Development: 4 courses in 1":"https://www.udemy.com/certificate/UC-f6d1f4c4-c0d4-4e16-a94d-8b1d3888164b/",
            "🏆 Deployment of Machine Learning models": "https://github.com/soumenksarker/deploying-machine-learning-models",
            # "🏆 Built and Deployed an NLP application that reveals named entities, classifies sentiment, and does text summarization using spacy, textblob, genism, streamlit and deploy to heroku.": "https://github.com/soumenksarker/text-summarizer-and-others",
            # "🏆Image Classification/Browser based model to classify Rock/Paper/Scissors Browser-based model, node.js, training with and without transfer learning, evaluating, alerting on browser!":"https://github.com/soumenksarker/TF-in-Deployment",
            # "🏆Built and deployed a CV application that detects faces, smiles, and eyes, do enhance, filters to add effect": "https://face-detection-opencv-strmlt.herokuapp.com/",

            }
            # --- Projects & Accomplishments ---
        st.write('\n')
        st.subheader("Accomplishments")
        st.write("---")
        for cer, link in Certificates.items():
            st.write(f"[{cer}]({link})")

if selected=="Live Chat":
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
                st.success("Welcome, Logged In as {}.. bored! feel free to conversate..".format(username))
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
