from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic (3).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | SOUMEN SARKER"
PAGE_ICON = ":wave:"
NAME = "SOUMEN SARKER"
DESCRIPTION = """
Data Sceince Enthuesiest, ML/DL Practitioner.
"""
EMAIL = "sks0007771@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/soumen-sarker-61302216b/",
    "GitHub": "https://github.com/soumenksarker",
    "Kaggle": "https://www.kaggle.com/soumenksarker",
    "Codeforces": "https://codeforces.com/profile/Soumen_Sarkar",
}
PROJECTS = {
"🏆 Built and deployed an NLP application that reveals named entities, classifies sentiment, and do OCR base Bangla(extractive) and English(abstructive) text summarization using spacy, textblob, genism, T5 and tesseract.": "https://huggingface.co/spaces/Soumen/Text-Summarization-and-NLP-tasks",
"🏆 Built and deployed an Image Captioning streamlit application.":"https://soumenksarker-imgcaptioning-app-izf09f.streamlitapp.com/",
"🏆 Image Captioning using huggingface API and streamlit.":"https://huggingface.co/spaces/Soumen/image_to_text",
"🏆 Emotion detection application":"https://soumenksarker-emotion-recognition-app-770rmy.streamlitapp.com/",
"🏆 Built and deployed a CV application that detects and classify objects, faces, smiles, and eyes, do enhance and filters to add effect.": "https://huggingface.co/spaces/Soumen/transform_image",
"🏆 Develop and deploy a Personal Website with Chatbot Integration": "https://soumen-sarker-personal-website.streamlit.app/",
"🏆 NLP literaure overview, A Sentiment Classification model by comparing naive Bayes, DNN, RNN, and LSTM classification models. Automatic Text Summarization with Transformer Architecture.": "https://github.com/soumenksarker/NLP-Specialization",  
"🏆 Image Classification/Browser based model to classify Rock/Paper/Scissors Browser-based model, node.js, training with and without transfer learning, evaluating, alerting on browser!":"https://github.com/soumenksarker/TF-in-Deployment",
"🏆 Bank Marketing Analysis Live Dashboard": "https://soumenksarker-live-bank-data-dashboard-app-2z8bky.streamlitapp.com/",
"🏆 House Price Prediction from research to production environment":"https://fathomless-falls-91100.herokuapp.com/docs",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Years of expereince in extracting actionable insights from Data
- ✔️ Strong hands on experience and knowledge in Bussiness/Financial/Data Science Projects (User_Athentication, Database Integration, KPI design, Real Time Interactive Dashboard)
- ✔️ Good understanding of Machine Learning/Deep Learning Projects(CV, NLP, Medical Data/Image Analysis, Time Series Processing) Architecture and Creating Pipeline(Data Processing, Model Building, Training, Evaluation),
      Packaging, Restfull API Integration, Web base App Development and Deploy for Predict and Inferencing on PaaS Cloud(streamlit, render, heroku e.t.c)/Ecosystem like Tensorflow Serving.
- ✔️ Excellent team-player and displaying strong sense of initiative on accomplishing tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Tensorflow, Keras), SQL
- 🗄️ Databases: SQLite, MySQL, Postgres, BigQuery SQL
- 📊 Data Visulization: Matplotlib, seaborn, ggplot2, Plotly
- 📚 Modeling: ML-Logistic regression, linear regression, decision trees, Random Forest, XGBoost
               DL-CNN, RNN, LSTM, Autoencoder, Transformer

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
