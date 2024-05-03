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
profile_pic = current_dir / "assets" / "4486c40b-8e20-4018-ae10-f147ebca72ad-removebg-preview.jpg"


# --- GENERAL SETTINGS ---
NAME = "SOUMEN SARKER"
DESCRIPTION = """
Kaggle Expert, ML/DL Specialist.
"""
EMAIL = "sks0007771@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/soumen-sarker-61302216b/",
    "GitHub": "https://github.com/soumenksarker",
    "Kaggle": "https://www.kaggle.com/soumenksarker",
    "Codeforces": "https://codeforces.com/contests/with/Soumen_Sarkar",
}
PROJECTS = {
"🏆 Write several services and microservices in Travelai's ETL pipeline by reading from api's, data extraction from json files, transform and load to store into postgres database's new column.
    Tools/Tech: Cron, Python, SQLAlchemy ORM(INSERT, BULK UPDATE, e.t.c), OOP, RegEX, Postgres, S3": "",
"🏆 Write SQL query in Apache Superset's SQL lab to grab analytics from connected database, execute as a cron to get several combinational time series csv chart data, mail into server using superset cron alert, read from mail server, match/analytics with api data and notify in dedicated team's channel.":"",
"🏆 Real-Time web scraping and visualization dashboard.": "https://github.com/soumenksarker/RealtimeScraperOpenSearchPostgresIntegration",
"🏆 Real-time Q&A system to Analysis and Visualize on scraped data(integrated with first project).":"https://huggingface.co/spaces/Soumen/QA_to_AnalysisVisualize_on_your_data_and_database",
"🏆 Real-time Credit Card fraud detection using Vertex AI, AutoML, BigQuery, Pub/Sub, Feature Store and Dataflow on GCP.":"https://github.com/soumenksarker/fraudfinder",
"🏆 Unstructured data analytics with BigQuery ML and Vertex AI pre-trained models. Vision API to extract texts from movie posters, Translation API to translate into English, and NLP API to sentiment analysis of movie reviews.":"https://colab.research.google.com/drive/1dapJBwSqyk0OkJi-6pH1Vl-6KKFwWPyl?usp=sharing",
"🏆 Building a Retail Demand Forecasting Model with Dashboard in BigQueryML and DataStudio.": "https://drive.google.com/file/d/1sYq5lMC3-FPNNUuuIUovh7Xld6QAuBrx/view?usp=sharing",
"🏆 Text summarization, from images/pdfs using t5-base and mt5-multilingual csebuetnlp model for Bangla and English languages.": "https://huggingface.co/spaces/Soumen/Text-Summarization-and-NLP-tasks",
"🏆 Conversate beyond your data(Upload multiple pdfs and paste links) using PaLM2 API, Pincone, Langchain":"https://chatwithyourownexpertsystem.streamlit.app/",
"🏆 Document AI to train a Custom Document Extractor processor. ": "https://codelabs.developers.google.com/codelabs/docai-custom#12",
"🏆 End to End Data Ingestion, Transformation, Feature Engineering and Model training, Evaluation with Dagshub, MLflow, and CICD Deployment using GitHub Action on AWS EC2 instance.":"https://dagshub.com/soumenksarker/End-to-end-Machine-Learning-Project-with-MLflow",
"🏆 NLP basic to advance: A Sentiment Classification model by comparing naive Bayes, DNN, RNN, and LSTM classification models. Ended with an advanced architecture like Transformer with attention mechanism and built an Automatic Text Summarizer.": "https://github.com/soumenksarker/NLP-Specialization",  
"🏆 Image Captioning using huggingface API and streamlit.":"https://huggingface.co/spaces/Soumen/image_to_text",
"🏆 Built and deployed a time series Anomaly Detection Tool(analysis, train, visualize and save the model) using pycaret.":"https://adtool.streamlit.app/",
"🏆 Emotion detection application":"https://soumenksarker-emotion-recognition-app-770rmy.streamlitapp.com/",
"🏆 Built a personal website.":"https://soumen-sarker-personal-website.streamlit.app/DigitalCV",
"🏆 Detects and classifies objects, faces, smiles, and eyes, do enhance and filters to add effect.": "https://huggingface.co/spaces/Soumen/transform_image",
"🏆 Image Classification/Browser-based model to classify Rock/Paper/Scissors Browser-based model, node.js, training with and without transfer learning, evaluating, alerting on browser!":"https://github.com/soumenksarker/TF-in-Deployment",
"🏆 House Price Prediction from research to production environment using Sci-kit-learn API (OOP, Inheritance, Transformer, Pipeline), pydantic, pytest, tox, Fast API and Uvicorn.":"https://fathomless-falls-91100.herokuapp.com/docs"
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

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 4+ years of experience in extracting actionable insights from structured and Unstructured Data.
- ✔️ Good understanding of business/financial projects (User_Athentication, Database Integration, KPI design, Real-Time Interactive Dashboard).
- ✔️ Strong hands-on experience in Machine Learning/Deep Learning Projects NLP(NMT, LLMS),  CV(Objet Detection, Segmentation, Classification, Tracking), Time Series Forecasting and Anomaly Detections(Prices, Transactional Data) Architechture Development.
- ✔️ Excellent team player and displays a strong sense of initiative in accomplishing tasks.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL.
- 🗄️ Databases: OpenSearch, PostgreSQL, BigQuery, Dynamodb.
- 📊 Data Visualization: DataStudio, Superset, OpenSearch Dashboard, matplotlib, seaborn, Plotly
- 📚 ML/DL Models, APIs, Vector DB, and libraries: linear regression, Logistic regression, Decision trees, SVM, Random Forest, XGBoost,
               CNN, RNN, LSTM, Autoencoder, Transformers(T5, BERT, LLMA-2, GPT-3.5), Attention. PaLM2, OpenAI, Gemini. Pinecone, Chromadb, llamaindex, Langchain.

"""
)

c1, c2=st.columns([2,3])
if c1.button("Home"):
    switch_page("Homepage")
if c2.button("Accomplishments"):
    switch_page("Accomplishments")

