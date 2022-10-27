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
Data Sceince enthuesiest, ML/DL practitioner.
"""
EMAIL = "sks0007771@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/soumen-sarker-61302216b/",
    "GitHub": "https://github.com/soumenksarker",
    "Kaggle": "https://www.kaggle.com/soumenksarker",
    "Dataquest": "https://app.dataquest.io/profile/soumensarker.ice.iu.bd",
}
PROJECTS = {
"🏆 Bank Marketing Analysis Live Dashboard": "https://soumenksarker-live-bank-data-dashboard-app-2z8bky.streamlitapp.com/",
"🏆 House Price Prediction from research to production environment":"https://fathomless-falls-91100.herokuapp.com/docs",
"🏆 NLP literaure overview, A Sentiment Classification model by comparing naive Bayes, DNN, RNN, and LSTM classification models. Automatic Text Summarization with Transformer Architecture.": "https://github.com/soumenksarker/NLP-Specialization",
"🏆 Built and Deployed an NLP application that reveals named entities, classifies sentiment, and does text summarization using spacy, textblob, genisma and T5": "https://soumenksarker-nlp-app-z47yvp.streamlitapp.com/",
"🏆 Image Classification/Browser based model to classify Rock/Paper/Scissors Browser-based model, node.js, training with and without transfer learning, evaluating, alerting on browser!":"https://github.com/soumenksarker/TF-in-Deployment",
"🏆 Built and deployed a CV application that detects faces, smiles, and eyes, do enhance, filters to add effect": "https://soumenksarker-face-detection-streamlit-app-bdy2rx.streamlitapp.com/",
"🏆 Develop and Deploy a Personal Site with Chatbot Integration": "https://soumenksarker-personal-website-1--homepage-aqokf8.streamlitapp.com/",

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
- ✔️ Years of expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Data Science app developement(user_athentication, database integration, real time Dashboard)
- ✔️ Good understanding of Machine Learning/Deep Learning Projects(CV, NLP, Time Series) architecture and creating pipeline(data processing, model building, traning, evaluation)
      packaging, restfull api integration using fast api, flask. Streamlit for front end and deploy for predict and inferencing on paas cloud(streamlit, heroku e.t.c)/ecosystem(tensorflow serving)
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Tensorflow, Keras), SQL
- 📊 Data Visulization: Matplotlib, seaborn, ggplot2, Plotly
- 📚 Modeling: ML-Logistic regression, linear regression, decision trees, Random Forest, XGBoost
               DL-CNN, RNN, LSTM, Autoencoder, Transformer
- 🗄️ Databases: SQLite, MySQL, Postgres, BigQuery SQL
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
