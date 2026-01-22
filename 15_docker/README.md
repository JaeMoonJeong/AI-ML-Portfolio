# 미션 15: Docker 기반 ML 협업 워크플로우

## 📋 미션 개요
두 명의 연구자가 협업하여 **Docker 기반의 머신러닝(ML) 워크플로우**를 설계하고 구현합니다. 컨테이너 기술을 통해 개발 환경의 파편화를 방지하고, 모델 학습부터 추론까지의 과정을 표준화합니다.

* **연구자 1:** 데이터 전처리, EDA, 모델링 및 Docker 이미지 빌드/배포를 담당합니다.
* **연구자 2:** Docker 환경에서 학습된 모델을 로드하고 최종 추론(Inference)을 수행합니다.

---

## 📂 프로젝트 구조

```text
mission15/
├── researcher1/                # 연구자 1 작업 폴더
│   ├── train_notebook.ipynb    # EDA 및 모델링 분석 노트북
│   ├── train.py                # 모델 학습 파이프라인 스크립트
│   ├── Dockerfile              # 가상 환경 구성을 위한 Docker 정의 파일
│   ├── requirements.txt        # 프로젝트에 필요한 Python 패키지 목록
│   └── data/
│       └── train.csv           # 모델 학습용 데이터
├── researcher2/                # 연구자 2 작업 폴더
│   ├── inference.ipynb         # 추론 테스트 및 결과 확인 노트북
│   ├── inference.py            # 실제 추론 수행 스크립트
│   ├── docker-compose.yml      # 서비스 오케스트레이션 및 환경 설정
│   └── data/
│       └── test.csv            # 검증을 위한 테스트 데이터
└── README.md                   # 프로젝트 매뉴얼

```

## 🛠 실행 가이드
1. 연구자 1: 모델 학습 및 이미지 빌드
researcher1 디렉토리에서 필요한 라이브러리를 정의하고 Docker 이미지를 생성합니다.

Bash
cd researcher1
# Docker 이미지 빌드
docker build -t ml-collaboration-env:latest .
2. 연구자 2: Docker Compose를 활용한 추론
연구자 2는 정의된 docker-compose.yml을 통해 일관된 환경에서 추론 스크립트를 실행합니다.

Bash
cd researcher2
# 컨테이너 실행 및 추론 수행
docker-compose up
📝 주요 구성 요소 설명
Dockerfile: python:3.9-slim 등의 베이스 이미지를 기반으로 학습 환경을 패키징합니다.

docker-compose.yml: 볼륨 마운트를 통해 학습된 모델 파일이나 데이터를 컨테이너 간에 공유할 수 있도록 설정합니다.

Requirements: pandas, scikit-learn, torch 등 협업에 필요한 공통 라이브러리를 명시합니다.


---

### 💡 실행력을 높이기 위한 제언
현재 구조에서 **연구자 1이 학습한 모델 파일**을 연구자 2가 어떻게 전달받을지가 핵심입니다.

1.  **Action Plan**: `researcher1`에서 생성된 모델 결과물(예: `model.pth`)이 자동으로 `researcher2`의 특정 경로로 복사되거나, 공통 볼륨을 바라보게끔 `docker-compose.yml`을 작성하는 것이 좋습니다.
2.  **질문**: 모델 파일의 확장자는 무엇으로 결정하셨나요? (예: `.pkl`, `.h5`, `.onnx` 등) 확장자에 따라 `requirements.txt`에 추가할 라이브러리가 달라질 수 있습니다.

혹시 `researcher1` 폴더에 들어갈 구체적인 **Dockerfile** 예시 코드가 필요하신가요?