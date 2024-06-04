# Text Summarization Transformer Deployment with BentoML
This repository provides a comprehensive guide to building a text summarization application using BentoML, with a specific focus on an mT5-small model fine-tuned for Azerbaijani text summarization. The model was trained on the az-news-summary dataset, covering a wide range of topics from Azerbaijani news articles. This project demonstrates the full lifecycle of model serving, from downloading and preparing the model to deploying and interacting with the service.

## Model Description
Model: mT5-small based Azerbaijani Summarization

Model Architecture: Google's Multilingual T5-small

Task: Summarization

Dataset: Azerbaijani News Summary Dataset


## Why BentoML?
BentoML is a flexible and powerful framework for serving machine learning models in production. It offers several benefits:

* Ease of Deployment: BentoML simplifies the deployment of models with minimal code changes.
* Scalability: BentoML’s Runners enable easy scaling of model inference across multiple instances.
* Integration: Seamlessly integrates with popular machine learning frameworks like PyTorch, TensorFlow, and Hugging Face Transformers.
* Monitoring: Supports monitoring with Prometheus for tracking model performance and request metrics.
* Packaging: BentoML packages models into self-contained archives (Bentos) that include all dependencies, ensuring reproducibility and ease of deployment.

## Setup Instructions
1. Clone the Repository

```python
git clone https://github.com/NijatZeynalov/Text-Summarization-Transformer-Deployment-with-BentoML
cd text_summarization_project
```
2. Install Dependencies
    
```python
pip install -r requirements.txt
```

3. Download the Model

```python
python app/models/download_model.py
```
4. Build the Bento

```python
bentoml build
```
5. Serve the Bento Service

```python
bentoml serve app.services.summarization_service:svc
```
6. Serve the FastAPI Frontend

In a separate terminal, start the FastAPI frontend application:

```python
uvicorn app.main:app --host 0.0.0.0 --port 8002
```
7. Access the Application
   
Open your web browser and navigate to the frontend URL:  http://localhost:8002

Prometheus metrics for the service can be accessed at:  http://localhost:8001/metrics

## Usage
Frontend: Interact with the summarization service through the web interface at http://localhost:8002. Enter text into the form and submit it to receive a summarized version.

API: Send HTTP POST requests to the summarization endpoint at http://0.0.0.0:3000/summarize.

```python
import requests

text = ""Səbail klubu kapitan Ağabala Ramazanovla yollarını ayırıb.
Report paytaxt təmsilçisinin mətbuat xidmətinə istinadən xəbər verir ki, 31 yaşlı yarımmüdafiəçi ilə başa çatan müqavilə müddəti yenilənməyib.
Qeyd edək ki, A.Ramazanov karyerası ərzində 2 dəfə - 2018-2020 və 2022-2024-cü illər mövsümündə dənizçilərin formasını geyinib, ümumilikdə 80 oyuna çıxıb, 20 qol vurub, 8 məhsuldar ötürmə edib."""
response = requests.post(
   "http://0.0.0.0:3000/summarize",
   headers={"accept": "text/plain", "Content-Type": "text/plain"},
   data=text
)

print(response.text)

```
