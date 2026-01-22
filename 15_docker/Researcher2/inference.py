import pandas as pd
import joblib
import os
import argparse

def run_inference():
    # 1. 인자 설정 (모델, 테스트 데이터, 결과 저장 경로)
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='model.pkl')
    parser.add_argument('--data', type=str, default='data/test.csv')
    parser.add_argument('--output', type=str, default='outputs/result.csv')
    args = parser.parse_args()

    # 2. 모델 로드 (연구자 1이 만든 pkl 파일)
    if not os.path.exists(args.model):
        print(f"Error: Model file '{args.model}' not found! 연구자 1에게 받은 pkl 파일을 확인하세요.")
        return

    print(f"Loading model from {args.model}...")
    model = joblib.load(args.model)

    # 3. 테스트 데이터 로드
    if not os.path.exists(args.data):
        print(f"Error: Test data file '{args.data}' not found!")
        return

    df_test = pd.read_csv(args.data)
    
    # 4. 전처리 (연구자 1과 동일한 로직 적용)
    # 실제 협업에서는 이 전처리 과정도 pkl에 포함시키는 것이 베스트입니다.
    if 'Extracurricular Activities' in df_test.columns:
        df_test['Extracurricular Activities'] = df_test['Extracurricular Activities'].map({'Yes': 1, 'No': 0})

    # 학습 때 사용한 특성(Feature)만 추출 (Performance Index 제외)
    X_test = df_test.copy()
    if 'Performance Index' in X_test.columns:
        X_test = X_test.drop('Performance Index', axis=1)

    # 5. 추론(Inference) 수행
    print("Performing inference...")
    predictions = model.predict(X_test)
    
    # 결과 데이터프레임 생성
    df_test['Predicted_Performance_Index'] = predictions

    # 6. 결과 저장
    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        
    df_test.to_csv(args.output, index=False)
    print(f"Inference complete! Results saved to: {args.output}")
    
    # 결과 샘플 출력
    print("\n--- Inference Samples ---")
    print(df_test[['Predicted_Performance_Index']].head())

if __name__ == "__main__":
    run_inference()