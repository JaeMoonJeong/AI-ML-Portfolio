# 미션 15 - 연구자 1: 학습 환경 Docker 이미지
# ==========================================
# 
# 빌드 방법:
#   docker build -t mission15-researcher1 .
#
# 실행 방법 (Jupyter Notebook):
#   docker run -p 8888:8888 -v $(pwd)/data:/app/data mission15-researcher1
#
# 실행 방법 (학습 스크립트):
#   docker run -v $(pwd)/data:/app/data -v $(pwd)/output:/app/output mission15-researcher1 python train.py

FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 설치 (matplotlib 의존성)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY train_notebook.ipynb .
COPY train.py .
COPY data/ ./data/

# Jupyter Notebook 설정
EXPOSE 8888

# 기본 명령어: Jupyter Notebook 실행
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]