import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
PAGE_TITLE = "Accomplishments| SOUMEN SARKER"
st.set_page_config(page_title=PAGE_TITLE)
c1, c2=st.columns([2,3])
if c1.button("Home"):
    switch_page("Homepage")
if c2.button("CV"):
    switch_page("DigitalCV")
st.subheader("Certifications & Projects")
option = option_menu(menu_title=None,
options= ["Problem Solving", "Data Science Courses & Projects","ML/DL courses & Projects"], 
icons=['boxes', 'book','bookmarks-fill'],
menu_icon="cast",
default_index=0,
orientation="horizontal")

if option=="Problem Solving":
    Certificates = {
        "🏆 Algorithmic Toolbox": "https://github.com/soumenksarker/Algorithmic-Toolbox-by-UCSan-Diego-Coursera",
        "🏆 Solved problem with Algorithm and Data Structures.": "https://github.com/soumenksarker/DS-and-Algs-with-solved-problems",
        "🏆 Algorithms on Graphs.":"https://github.com/soumenksarker/Algorithm-on-graphs"
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


