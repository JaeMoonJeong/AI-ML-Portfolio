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

## 📊 데이터셋 설명 (Dataset Description)
모델 학습에 사용되는 주요 변수들에 대한 정의입니다. 학업 성취도(`Performance Index`)를 예측하기 위한 5개의 독립 변수로 구성되어 있습니다.

| 변수명 | 설명 |
| :--- | :--- |
| **Hours Studied** | 공부한 총 시간 |
| **Previous Scores** | 이전 시험 점수 |
| **Extracurricular Activities** | 과외 활동 참여 여부 (Yes/No) |
| **Sleep Hours** | 하루 평균 수면 시간 |
| **Sample Question Papers Practiced** | 연습한 모의고사 수 |
| **Performance Index** | **목표 변수 (10~100, 학업 성취도)** |

---

## 🔬 연구자 1: 학습 파이프라인 (Researcher 1 Pipeline)

### 1단계: 환경 설정 및 EDA
연구자 1은 로컬 또는 컨테이너 환경에서 데이터를 탐색하고 모델링 방향을 설정합니다.

```bash
cd researcher1

# Jupyter Notebook을 실행하여 EDA 수행
jupyter notebook train_notebook.ipynb

```


* **EDA 주요 내용:** 데이터 분포 확인, 결측치 검사, 상관관계 분석, 시각화
    - 데이터 분포 확인: 각 변수의 수치적 분포 및 이상치 파악
    - 결측치 검사: 데이터셋 내 누락된 값 확인 및 처리 전략 수립
    - 상관관계 분석: 독립 변수들과 목표 변수(Performance Index) 간의 선형/비선형 관계 분석
    - 시각화: 히스토그램, 산점도 등을 활용한 데이터 특징 가시화
    
### 2단계: 모델 학습

Python 스크립트를 실행하여 모델을 학습시키고 결과물을 생성합니다.

```bash
# 기본 학습 실행
python train.py

# 또는 옵션을 지정하여 실행
python train.py --data data/train.csv --output model.pkl

```

* **모델 출력:** `model.pkl` (학습된 모델 + 전처리 객체)

### 3단계: Docker 이미지 빌드

구성된 환경을 컨테이너 이미지로 패키징하고 테스트합니다.

```bash
# 이미지 빌드
docker build -t mission15-researcher1 .

# 테스트 실행 (Jupyter Notebook)
docker run -p 8888:8888 mission15-researcher1

# 테스트 실행 (학습 스크립트)
docker run mission15-researcher1 python train.py

```

---

## 🚀 연구자 2: 모델 추론 (Researcher 2 Inference)

연구자 2는 배포된 이미지를 활용하여 최종 추론을 수행합니다. 구체적인 실행 방법은 `researcher2/docker-compose.yml` 설정을 따릅니다.

```bash
cd researcher2
docker-compose up

```

```

```