import streamlit as st
import pandas as pd
import numpy as np
import altair as alt 
from PIL import Image
from model_4 import MyModel

model_instance = MyModel()

#페이지 기본설정
st.set_page_config(layout="wide", page_title="Image Claasification (Jae-Moon)")
st.set_page_icon="📈"
st.title("🚀 Image Claasification (Jae-Moon)")
st.markdown("---")



# [사이드바 처리 로직]
with st.sidebar:
    st.header("설정 및 입력")
    # 입력 방식 선택 (라디오 버튼)
    input_method = st.radio("이미지 입력 방식", ["파일 업로드", "카메라 촬영"])
    
    uploaded_file = None
    if input_method == "파일 업로드":
        uploaded_file = st.file_uploader("이미지 파일을 선택하세요", type=['png', 'jpg', 'jpeg'])
    else:
        uploaded_file = st.camera_input("카메라로 사물을 비춰주세요")
    
# [메인 화면 로직]
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # 이미지를 중앙에 적절한 크기로 배치하기 위해 column 활용
    results = None
    img_col, info_col = st.columns([2, 1])
    
    
    with img_col:
        st.image(image, width=500)
    
    with info_col:
        st.info("📊 이미지 정보")
        st.write(f"- 파일명: {uploaded_file.name}")
        st.write(f"- 해상도: {image.size[0]} x {image.size[1]}")
        st.write("---")
        
        # 분류 실행 버튼

        if st.button("✅ 분류하기", use_container_width=True):
        # 버튼 클릭 시 동작할 로직
            st.success(f"'{uploaded_file.name}' 파일의 분류 프로세스를 시작합니다.")
            results=model_instance.predict(image)
            top_result = results[0]
            print(top_result)


    if results:
        
        df = pd.DataFrame(results)
    
        # 가독성을 위해 라벨의 첫 글자를 대문자로 변경
        df['label'] = df['label'].str.title()

        st.divider()
        st.subheader("📊 Top-5 분석 상세 결과")

        # 2. Altair 막대 차트 생성
        # - x축: 신뢰도 (Score)
        # - y축: 라벨 (Label), 값에 따라 정렬
        chart = alt.Chart(df).mark_bar(
            cornerRadiusTopRight=5,
            cornerRadiusBottomRight=5
        ).encode(
            x=alt.X('score:Q', title='신뢰도 (Confidence Score)', axis=alt.Axis(format='%')),
            y=alt.Y('label:N', sort='-x', title='분류 항목'),
            color=alt.Color('score:Q', scale=alt.Scale(scheme='viridis'), legend=None), # 점수에 따른 색상 변화
            tooltip=['label', alt.Tooltip('score:Q', format='.2%')] # 마우스 호버 시 상세 정보
        ).properties(
            height=300
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        )

        # 3. 차트 출력
        st.altair_chart(chart, use_container_width=True)
        
        
        
        # 1. 최상위 결과값 추출
        top_result = results[0]
        label = top_result['label']
        score = top_result['score']

        # 2. Streamlit UI에 깔끔하게 출력
        st.divider() # 구분선 추가
        st.subheader("🎯 최종 판별 결과")

        
        # 지표(Metric) 형태로 시각화
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="판별된 사물", value=label)
        with col2:
            st.metric(label="신뢰도", value=f"{score:.2%}")

        # 강조 메시지
            
        # 2. 프로그레스 바 표시 (0.0에서 1.0 사이의 값을 받습니다)

        st.progress(score)
        st.success(f"이 물체는 {score:.2%}의 확률로 [{label}]입니다.")

else:
    st.info("왼쪽 사이드바에서 분석할 이미지를 업로드해 주세요.")
    
# results에 모델의 예측 리스트가 담겨 있다고 가정합니다.
