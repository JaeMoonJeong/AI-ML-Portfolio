import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import argparse
import os

def train():
    # 1. 인자 설정 (데이터 경로 및 출력 경로)
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='data/train.csv')
    parser.add_argument('--output', type=str, default='/app/output/model.pkl') # 출력 경로 기본값 수정
    args = parser.parse_args()

    # 2. 데이터 로드
    if not os.path.exists(args.data):
        print(f"Error: Data file not found at {args.data}")
        return

    print(f"Loading data from {args.data}...")
    df = pd.read_csv(args.data)
    
    # 3. 전처리: Extracurricular Activities (Yes/No -> 1/0)
    # 데이터에 해당 컬럼이 있는지 확인 후 변환
    if 'Extracurricular Activities' in df.columns:
        df['Extracurricular Activities'] = df['Extracurricular Activities'].map({'Yes': 1, 'No': 0})
    
    X = df.drop('Performance Index', axis=1)
    y = df['Performance Index']
    
    # 4. 모델 학습
    print("Training the Linear Regression model...")
    model = LinearRegression()
    model.fit(X, y)
    
    # 5. 출력 디렉토리 생성 및 모델 저장
    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    joblib.dump(model, args.output)
    print(f"Successfully saved the model to: {args.output}")
    print(f"Training Score (R^2): {model.score(X, y):.4f}")

if __name__ == "__main__":
    train()