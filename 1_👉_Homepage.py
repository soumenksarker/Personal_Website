from inspect import _empty
from queue import Empty
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Website", page_icon=":tada:", layout="wide")
st.title("Home Page")
st.sidebar.success("Please navigate from above ...")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_8npirptd.json")
lottie_coding1=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_contact_form = Image.open("images/yt_contact_form.png")
#img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Soumen :wave:")
    st.title("A Data Science, ML, DL Practitioner From Bangladesh")
    st.write("I am passionate about finding ways to do Data Science/ML/DL projects using Python, SQL and R ."
            """
            I'll do your Data Science, Machine Learning and Deep Learning projects regarding Computer Vision, Natural Language Processing, Bussiness/Financial data 
            and Medical data/image Analysis from Cleaning, Analysis, Modeling, Training, Evaluating, Predicting/Inferencing to Application Design & Development.
           """
        )
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns([2.5,1])
    with left_column:
        st.header("What I will do...")
        st.write("##")
        st.write("""
    >Data Cleaning, Analysis & Visualization with several data sources and data formats(images, text, json e.t.c)
        Database & Integration: SQLite, SQLAlchemy, BigQuery SQL, redis noSQL
     
        Tools & libraries: Python, numpy, pandas, seaborn, Plotly
    >Apply probability and statistical techniques to derive useful insights from your data
        Tools & libraries: scipy, statsmodels, R
    >Creating Pipeline(Processing, Modeling, Training, Evaluation) with state of the art of Machine Learning and Deep Learning techniques.
        Tools & libraries: scikit-learn, Tensorflow, keras, torch, transformers
    > Packagging, Unit testing, API integration, Application Design & Devloopment, Deployment
        Tools & libraries: poetry, tox, pytest, test PyPI, FastApi, HTML, CSS, jQuery, streamlit
      
        Cloud: huggingface, Uvicorn, Heroku, streamlit, Tensorflow Serving, GCP, AWS e.t.c""")
        
    
    with right_column:
        st_lottie(lottie_coding, height=350, key="coding")



    # Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sks0007771@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns([1.7, 2])
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding1, height=300, key="contact") #set a lottie animation here
        

   
