from pathlib import Path
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from PIL import Image
PAGE_TITLE = "Digital CV | SOUMEN SARKER"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "365301312_3529339043954415_640094006408748687_n-removebg-preview.jpg"


# --- GENERAL SETTINGS ---
NAME = "SOUMEN SARKER"
DESCRIPTION = """
Kaggle kernel Expert, ML/DL Specialist.
"""
EMAIL = "sks0007771@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/soumen-sarker-61302216b/",
    "GitHub": "https://github.com/soumenksarker",
    "Kaggle": "https://www.kaggle.com/soumenksarker",
    "Codeforces": "https://codeforces.com/profile/Soumen_Sarkar",
}
PROJECTS = {
"🏆 Chatbot and OCR(images/pdfs)/tesseract base text summarization using t5-base and mt5-multilingual csebuetnlp model for bangla and english languages.": "https://huggingface.co/spaces/Soumen/Text-Summarization-and-NLP-tasks",
"🏆 Expert system/conversate beyond your data(healthcare, finance, literature e.t.c) using PaLM2 API, Pincone, Langchain":"https://palmapilangchain-iwjbh4hqfuztdyyysmcxqk.streamlit.app/",
"🏆 Image Captioning using huggingface API and streamlit.":"https://huggingface.co/spaces/Soumen/image_to_text",
"🏆 Emotion detection application":"https://soumenksarker-emotion-recognition-app-770rmy.streamlitapp.com/",
"🏆 Detects and classifies objects, faces, smiles, and eyes, do enhance and filters to add effect.": "https://huggingface.co/spaces/Soumen/transform_image",
"🏆 Real-time Credit Card fraud detection using Vertex AI, AutoML, BigQuery, Pub/Sub, Dataflow on GCP.":"https://github.com/soumenksarker/fraudfinder",
"🏆 End to End Data Ingestion, Transformation, Feature Engineering and Model training, Evaluation with Dagshub, MLflow, and CICD Deployment using GitHub Action on AWS EC2 instance.":"https://dagshub.com/soumenksarker/End-to-end-Machine-Learning-Project-with-MLflow",
"🏆 Unstructured data analytics with BigQuery ML and Vertex AI pre-trained models. Vision API to extract texts from movie posters, Translation API to translate into English, and NLP API to sentiment analysis of movie reviews.":"https://colab.research.google.com/drive/1dapJBwSqyk0OkJi-6pH1Vl-6KKFwWPyl?usp=sharing",
"🏆 Built and deployed a time series Anomaly Detection Tool using pycaret.":"https://adtool.streamlit.app/",
"🏆 NLP literature overview, A Sentiment Classification model by comparing naive Bayes, DNN, RNN, and LSTM classification models. Automatic Text Summarization with Transformer Architecture.": "https://github.com/soumenksarker/NLP-Specialization",  
"🏆 Image Classification/Browser-based model to classify Rock/Paper/Scissors Browser-based model, node.js, training with and without transfer learning, evaluating, alerting on browser!":"https://github.com/soumenksarker/TF-in-Deployment",
"🏆 Bank Marketing Analysis Live Dashboard": "https://soumenksarker-live-bank-data-dashboard-app-2z8bky.streamlitapp.com/",
"🏆 House Price Prediction from research to production environment using Sci-kit-learn API (OOP, Inheritance, Transformer, Pipeline), pydantic, pytest, tox, Fast API and Uvicorn.":"https://fathomless-falls-91100.herokuapp.com/docs",

}


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
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Years of experience in extracting actionable insights from structured and Unstructured Data.
- ✔️ Good understanding of business/financial or any Data Science Projects (User_Athentication, Database Integration, KPI design, Real-Time Interactive Dashboard).
- ✔️ Strong hands-on experience in Machine Learning/Deep Learning Projects CV(Objet Detection, Segmentation, Classification, Tracking) NLP(Sentiment Analysis, Translation, Chatbot), Time Series Forecasting, and Anomaly Detections(Stock Prices, Transactional Data) Architecture Development and Deployment on the Cloud.
- ✔️ Excellent team player and displays a strong sense of initiative in accomplishing tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Tensorflow, Keras, Vertext AI), SQL
- 🗄️ Databases: SQLite, BigQuery SQL, BigQuery ML
- 📊 Data Visualization: Matplotlib, seaborn, ggplot2, Plotly
- 📚 Modeling: ML-Logistic regression, linear regression, decision trees, SVM, Random Forest, XGBoost,
               CNN, RNN, LSTM, Autoencoder,  Transformer, Attention, LLMA2

"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
c1, c2=st.columns([2,3])
if c1.button("Home"):
    switch_page("Homepage")
if c2.button("Accomplishments"):
    switch_page("Accomplishments")

