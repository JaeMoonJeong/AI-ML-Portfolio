import torch
from PIL import Image
import requests
from transformers import ViTImageProcessor, ViTForImageClassification
from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_vit_model():
    print("--- 모델 가중치 로드 중 (최초 1회) ---")
    classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
    return classifier


class MyModel:
    def __init__(self):
        self.classifier = load_vit_model()
        print("Model init")
        
        
    def predict(self, image):
        #AI 예측 로직 시뮬레이션
        # 나중에 이 부분만 FastAPI의 엔도포인트 함수로 변경하면 됩니다.
        results = self.classifier(image)
        return results