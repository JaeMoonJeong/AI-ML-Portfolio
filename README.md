# 🤖 AI & Machine Learning Project Portfolio

Hi, I'm Jae-Moon Jeong, a Mechanical Engineer (Ph.D.). This repository documents my systematic journey to integrate advanced AI/ML capabilities with my domain expertise. It covers 18 comprehensive projects, from data fundamentals to full-stack model deployment.

---

## 🚀 Mission Dashboard

This table provides a high-level overview of all 18 projects, their domains, and the core technologies used.

| Project | Directory | Title & Domain | Core Concepts & Models |
| :--- | :--- | :--- | :--- |
| **01** | [`/01_python_fundamentals/`](./01_python_fundamentals/) | **Python Fundamentals & OOP** | `Python`, `Functions`, `OOP`, `Class Design`, `Error Handling` |
| **02** | [`/02_hotel_booking_eda/`](./02_hotel_booking_eda/) | **Hotel Booking EDA** | `Pandas`, `Data Analysis`, `EDA`, `Visualization`, `Seaborn` |
| **03** | [`/03_bike_demand_prediction/`](./03_bike_demand_prediction/) | **Bike Demand Prediction** | `Regression`, `Feature Engineering`, `ML Models`, `RMSLE` |
| **04** | [`/04_ensemble_methods/`](./04_ensemble_methods/) | **Ensemble Techniques** | `Decision Tree`, `Random Forest`, `XGBoost`, `Classification` |
| **05** | [`/05_document_denoising/`](./05_document_denoising/) | **Document Denoising** | `Autoencoder`, `Denoising`, `Image Restoration`, `PyTorch` |
| **06** | [`/06_pneumonia_classification/`](./06_pneumonia_classification/) | **Pneumonia Classification** | `Classification`, `Transfer Learning`, `Fine-Tuning`, `CNN` |
| **07** | [`/07_pet_face_detection/`](./07_pet_face_detection/) | **Pet Face Detection** | `Object Detection`, `SSD`, `Bounding Box`, `mAP`, `IOU` |
| **08** | [`/08_football_segmentation/`](./08_football_segmentation/) | **Football Video Segmentation** | `Semantic Segmentation`, `U-Net`, `Pixel-level`, `Dice Loss` |
| **09** | [`/09_fashion_cgan/`](./09_fashion_cgan/) | **Fashion Image Generation** | `Generative AI`, `GAN`, `cGAN`, `Image Generation` |
| **10** | [`/10_text_embedding/`](./10_text_embedding/) | **Text Data & Embedding** | `NLP`, `Embedding`, `Word2Vec`, `TF-IDF` |
| **11** | [`/11_pretrained_nlp/`](./11_pretrained_nlp/) | **Pre-trained NLP Models** | `Transformers`, `BERT`, `GPT`, `Fine-Tuning` |
| **12** | [`/12_llm_prompting/`](./12_llm_prompting/) | **LLM & Prompt Engineering** | `LLM`, `Prompt Engineering`, `In-Context Learning` |
| **13** | [`/13_peft/`](./13_peft/) | **PEFT** | `PEFT`, `LoRA`, `Parameter-Efficient Fine-Tuning` |
| **14** | [`/14_rag/`](./14_rag/) | **RAG (Retrieval-Augmented Gen)** | `RAG`, `LangChain`, `VectorDB`, `LLM` |
| **15** | [`/15_docker/`](./15_docker/) | **Docker for MLOps** | `Docker`, `Containerization`, `MLOps`, `Dockerfile` |
| **16** | [`/16_model_optimization/`](./16_model_optimization/) | **Model Optimization** | `Model Optimization`, `Quantization`, `Pruning` |
| **17** | [`/17_web_prototyping/`](./17_web_prototyping/) | **Web Prototyping** | `Streamlit`, `Flask`, `Web App`, `Prototyping` |
| **18** | [`/18_fastapi_serving/`](./18_fastapi_serving/) | **FastAPI Model Serving** | `FastAPI`, `API`, `Model Serving`, `Uvicorn`, `MLOps` |

---

## 📌 Mission Details

Here is a detailed breakdown of each sprint's objective, key skills, and outcomes.

### 01. Python Fundamentals & OOP
* **[➡️ Go to Notebook](./01_python_fundamentals/)**
* **Mission:** Solidify Python programming basics, from functions and error handling to Object-Oriented Programming (OOP).
* **Key Skills:**
    * `Functions`: Writing reusable blocks of code.
    * `Error Handling`: Using `try-except` blocks for robust code.
    * `OOP`: Designing classes (`BankAccount`, `TimeTracker`, `VoteSystem`) with methods and properties.
    * `Class/Static Methods`: Managing class-level data and utility functions (`EmployeeManager`, `ReservationSystem`).
* **Outcome:** Solved 20+ programming challenges, demonstrating a strong grasp of Python's core concepts and OOP design patterns.

### 02. Hotel Booking EDA
* **[➡️ Go to Notebook](./02_hotel_booking_eda/)**
* **Mission:** Analyze the "Hotel Booking Demand" dataset to understand the primary factors driving booking cancellations.
* **Key Skills:**
    * `Pandas`: Data loading, cleaning, filtering, and aggregation.
    * `Data Visualization`: Using `Matplotlib` and `Seaborn` to create insightful plots (histograms, heatmaps, bar charts).
    * `EDA`: Forming hypotheses and exploring relationships between variables (e.g., `lead_time`, `market_segment`) and `is_canceled`.
* **Outcome:** An analytical report identifying key cancellation drivers and proposing data-driven strategies to reduce cancellation rates.

### 03. Bike Demand Prediction
* **[➡️ Go to Notebook](./03_bike_demand_prediction/)**
* **Mission:** Build a machine learning model to accurately predict bike rental demand (`count`) based on time, weather, and seasonal data.
* **Key Skills:**
    * `Feature Engineering`: Extracting useful features from `datetime` objects.
    * `Regression Models`: Implementing and training various regression models.
    * `Model Evaluation`: Using **RMSLE** (Root Mean Squared Logarithmic Error) as the primary evaluation metric.
* **Outcome:** A predictive model optimized for low RMSLE, providing a baseline for bike-sharing system operations.

### 04. Ensemble Techniques
* **[➡️ Go to Notebook](./04_ensemble_methods/)**
* **Mission:** Implement and compare various ensemble models to improve classification performance.
* **Key Skills:**
    * `Ensemble Theory`: Understanding bagging vs. boosting.
    * `Decision Tree`: Base model for ensembles.
    * `Random Forest`: Implementing bagging.
    * `XGBoost`: Implementing gradient boosting.
* **Outcome:** A notebook comparing the accuracy and robustness of different ensemble methods on a given dataset.

### 05. Document Denoising
* **[➡️ Go to Notebook](./05_document_denoising/)**
* **Mission:** Develop a deep learning model to restore and "clean" damaged or noisy document images.
* **Key Skills:**
    * `Autoencoder`: Building a Denoising Autoencoder architecture.
    * `PyTorch`: Defining the model, loss function, and training loop.
    * `Image Preprocessing`: Handling and normalizing image data.
    * `Evaluation`: Measuring model performance with `RMSE` and `PSNR`.
* **Outcome:** A trained Autoencoder capable of removing noise and reconstructing clean, legible text from "dirty" document images.

### 06. Pneumonia Classification
* **[➡️ Go to Notebook](./06_pneumonia_classification/)**
* **Mission:** Classify chest X-Ray images as "Pneumonia" or "Normal" using deep learning.
* **Key Skills:**
    * `Transfer Learning`: Using pre-trained CNNs (e.g., ResNet, VGG).
    * `Fine-Tuning`: Implementing **Frozen**, **Partial**, and **Full Fine-Tuning** strategies.
    * `Image Augmentation`: Expanding the dataset to improve model generalization.
    * `Classification Metrics`: Evaluating the model using `Accuracy`, `Precision`, `Recall`, and `F1-score`.
* **Outcome:** A high-accuracy classifier for pneumonia detection, with a comparative analysis of different fine-tuning techniques.

### 07. Pet Face Detection
* **[➡️ Go to Notebook](./07_pet_face_detection/)**
* **Mission:** Train an Object Detection model to identify and locate cat and dog faces in the "Oxford-IIIT Pet Dataset".
* **Key Skills:**
    * `Object Detection`: Understanding the principles of localization and classification.
    * `SSD Model`: Implementing the Single Shot Detector architecture.
    * `Data Parsing`: Reading XML annotations to get bounding box coordinates.
    * `Evaluation`: Measuring performance using `mAP` (mean Average Precision) and `IOU` (Intersection over Union).
* **Outcome:** A trained SSD model capable of drawing accurate bounding boxes around pet faces in images.

### 08. Football Video Segmentation
* **[➡️ Go to Notebook](./08_football_segmentation/)**
* **Mission:** Perform pixel-level Semantic Segmentation on football footage to identify 11 classes (e.g., Player, Ball, Ground, Referee).
* **Key Skills:**
    * `Semantic Segmentation`: Classifying every pixel in an image.
    * `U-Net`: Implementing the U-Net architecture, which is effective for biomedical and complex scene segmentation.
    * `Loss Functions`: Using `Cross Entropy Loss` and `Dice Loss` for segmentation tasks.
* **Outcome:** A trained U-Net model that can accurately segment and color-code different objects in a football match.

### 09. Fashion Image Generation
* **[➡️ Go to Notebook](./09_fashion_cgan/)**
* **Mission:** Build a **Conditional GAN (cGAN)** to generate specific fashion items (e.g., "T-shirt", "Bag") from the FashionMNIST dataset.
* **Key Skills:**
    * `GANs`: Building Generative Adversarial Networks (Generator vs. Discriminator).
    * `cGAN`: Using conditional labels (the item class) to control the generation process.
    * `Image Generation`: Training a model to produce realistic, novel images.
* **Outcome:** A generative model that can create images of specific clothing items on demand.

### 10. Text Data & Embedding
* **[➡️ Go to Notebook](./10_text_embedding/)**
* **Mission:** Explore foundational NLP techniques for converting text into numerical representations.
* **Key Skills:**
    * `NLP Preprocessing`: Tokenization, stop-word removal.
    * `Bag-of-Words`: `TF-IDF` (Term Frequency-Inverse Document Frequency).
    * `Word Embedding`: Training a `Word2Vec` model to capture semantic meaning.
* **Outcome:** A set of notebooks demonstrating text vectorization techniques for use in downstream ML tasks.

### 11. Pre-trained NLP Models
* **[➡️ Go to Notebook](./11_pretrained_nlp/)**
* **Mission:** Leverage large, pre-trained transformer models for advanced NLP tasks.
* **Key Skills:**
    * `Transformers`: Using the `Hugging Face` library.
    * `BERT`: Fine-tuning BERT for text classification (e.g., sentiment analysis).
    * `GPT`: Understanding the architecture of generative models.
* **Outcome:** A fine-tuned BERT model for a specific text classification task, achieving high accuracy.

### 12. LLM & Prompt Engineering
* **[➡️ Go to Notebook](./12_llm_prompting/)**
* **Mission:** Explore the capabilities of Large Language Models (LLMs) and learn to control their output through effective prompting.
* **Key Skills:**
    * `Prompt Engineering`: Designing clear and effective prompts.
    * `Zero-shot/Few-shot`: Using in-context learning to solve problems.
    * `LLM Applications`: Brainstorming and testing use cases for LLMs.
* **Outcome:** A guide and series of experiments demonstrating how prompt structure impacts LLM performance.

### 13. PEFT (Parameter-Efficient Fine-Tuning)
* **[➡️ Go to Notebook](./13_peft/)**
* **Mission:** Implement parameter-efficient methods to fine-tune large models with limited computational resources.
* **Key Skills:**
    * `PEFT`: Understanding the need for efficient tuning.
    * `LoRA`: Implementing Low-Rank Adaptation to fine-tune a model by training only a small fraction of its parameters.
* **Outcome:** A fine-tuned model using LoRA, demonstrating comparable performance to full fine-tuning at a fraction of the computational cost.

### 14. RAG (Retrieval-Augmented Generation)
* **[➡️ Go to Notebook](./14_rag/)**
* **Mission:** Build a RAG system to provide LLMs with external knowledge, reducing hallucinations and enabling domain-specific answers.
* **Key Skills:**
    * `VectorDB`: Storing and querying text embeddings (e.g., FAISS, ChromaDB).
    * `LangChain`: Orchestrating the RAG pipeline (Retrieve -> Augment -> Generate).
    * `RAG`: Combining information retrieval with text generation.
* **Outcome:** A functional chatbot or Q&A system that can answer questions based on a custom document set.

### 15. Docker for MLOps
* **[➡️ Go to Notebook](./15_docker/)**
* **Mission:** Containerize a machine learning application using Docker to ensure reproducibility and easy deployment.
* **Key Skills:**
    * `Docker`: Writing a `Dockerfile` for a Python application.
    * `Containerization`: Building, running, and managing Docker containers.
    * `MLOps`: Understanding the first step in creating a reproducible ML pipeline.
* **Outcome:** A Docker image containing a trained model and its dependencies, ready for deployment.

### 16. Model Optimization
* **[➡️ Go to Notebook](./16_model_optimization/)**
* **Mission:** Explore techniques to make deep learning models smaller, faster, and more efficient for edge devices or production.
* **Key Skills:**
    * `Quantization`: Reducing model precision (e.g., FP32 -> INT8).
    * `Pruning`: Removing unnecessary weights from a neural network.
    * `Knowledge Distillation`: Training a smaller "student" model to mimic a larger "teacher" model.
* **Outcome:** An optimized model with reduced size and faster inference speed.

### 17. Web Prototyping
* **[➡️ Go to Notebook](./17_web_prototyping/)**
* **Mission:** Build an interactive web application to showcase a machine learning model.
* **Key Skills:**
    * `Streamlit`: Rapidly building data-focused web apps in Python.
    * `Flask`: (Optional) A micro-framework for building custom web APIs.
    * `UI/UX`: Creating a simple user interface for model interaction.
* **Outcome:** A functional web app where users can input data (e.g., upload an image) and see the model's prediction.

### 18. FastAPI Model Serving
* **[➡️ Go to Notebook](./18_fastapi_serving/)**
* **Mission:** Deploy a machine learning model as a high-performance, production-ready API.
* **Key Skills:**
    * `FastAPI`: Building fast, modern APIs with automatic documentation.
    * `Pydantic`: Defining data schemas for request and response validation.
    * `Uvicorn`: Running the API as an ASGI server.
    * `MLOps`: Final step in productionalizing a model.
* **Outcome:** A robust API endpoint that serves model predictions, complete with interactive (Swagger) documentation.
