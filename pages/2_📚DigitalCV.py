from pathlib import Path
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "365301312_3529339043954415_640094006408748687_n-removebg-preview.jpg"


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
"🏆 Built and deployed an NLP application that does text generation/gpt2 and OCR(image/pdf)/tesseract base text summarization/t5-base and mt5-multilingual csebuetnlp model.": "https://huggingface.co/spaces/Soumen/Text-Summarization-and-NLP-tasks",
"🏆 Conversate with your multiple own documents using llma2, deployed on streamlit cloud.":"https://multipledocumentllama2bot-uava2a7xahgt8wpxzvfggp.streamlit.app/",
"🏆 End to End ML project with MLflow.":"https://dagshub.com/soumenksarker/End-to-end-Machine-Learning-Project-with-MLflow",
"🏆 Image Captioning using huggingface API and streamlit.":"https://huggingface.co/spaces/Soumen/image_to_text",
"🏆 Built and deployed a time series Anomaly Detection Tool using pycaret":"https://adtool.streamlit.app/",
"🏆 Developed and deployed an Image Captioning streamlit application.":"https://soumenksarker-imgcaptioning-app-izf09f.streamlitapp.com/",
"🏆 Emotion detection application":"https://soumenksarker-emotion-recognition-app-770rmy.streamlitapp.com/",
"🏆 Built and deployed a CV application that detects and classify objects, faces, smiles, and eyes, do enhance and filters to add effect.": "https://huggingface.co/spaces/Soumen/transform_image",
"🏆 NLP literaure overview, A Sentiment Classification model by comparing naive Bayes, DNN, RNN, and LSTM classification models. Automatic Text Summarization with Transformer Architecture.": "https://github.com/soumenksarker/NLP-Specialization",  
"🏆 Image Classification/Browser based model to classify Rock/Paper/Scissors Browser-based model, node.js, training with and without transfer learning, evaluating, alerting on browser!":"https://github.com/soumenksarker/TF-in-Deployment",
"🏆 Bank Marketing Analysis Live Dashboard": "https://soumenksarker-live-bank-data-dashboard-app-2z8bky.streamlitapp.com/",
"🏆 House Price Prediction from research to production environment using Sci-kit-learn api(OOP, Inheritence, Transformer, Pipeline), pydantic, pytest, tox, Fast API and Uvicorn.":"https://fathomless-falls-91100.herokuapp.com/docs",

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
- ✔️ Good understanding of Bussiness/Financial/Data Science Projects (User_Athentication, Database Integration, KPI design, Real Time Interactive Dashboard)
- ✔️ Strong hands on experience of Machine Learning/Deep Learning Projects(CV, NLP(chatbot, llma2), Image Processing, Time Series Forecasting(GCN, Graph autoencoder, Attention) Architecture Development and Deployment on cloud
- ✔️ Excellent team-player and displaying strong sense of initiative on accomplishing tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Tensorflow, Keras, MLops, SageMaker ), SQL
- 🗄️ Databases: SQLite, BigQuery SQL, BigQuery ML
- 📊 Data Visulization: Matplotlib, seaborn, ggplot2, Plotly
- 📚 Modeling: ML-Logistic regression, linear regression, decision trees, SVM, Random Forest, XGBoost
               DL-CNN, RNN, LSTM, Autoencoder, Attention, Transformer, LLMA2

"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
if st.button("Home"):
   switch_page("Homepage")
