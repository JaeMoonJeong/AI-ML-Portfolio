from transformers import pipeline

# 한국어 감성 분석에 특화된 경량 모델 로드
# 모델이 처음 실행될 때 다운로드되므로 약간의 시간이 소요됩니다.
model_name = "jaehyeong/koelectra-base-v3-generalized-sentiment-analysis"

try:
    sentiment_model = pipeline("sentiment-analysis", model=model_name)
except Exception as e:
    print(f"모델 로드 실패: {e}")
    # 모델 로드 실패 시를 대비한 기본 함수
    sentiment_model = None

def analyze_sentiment(text: str):
    if not text:
        return "데이터 없음", 0.0
    
    if sentiment_model:
        result = sentiment_model(text)[0]
        # 모델 결과: LABEL_0(부정), LABEL_1(긍정) 등 (모델마다 다름)
        # 이 모델은 1이 부정, 0이 긍정인 경우가 많으니 결과를 매핑합니다.
        label = result['label']
        score = result['score']
        
        # 단순화된 매핑 (실제 모델 출력 확인 후 조정 필요)
        sentiment = "Positive" if "1" in label or "pos" in label.lower() else "Negative"
        return sentiment, score
    else:
        return "Model Not Loaded", 0.0