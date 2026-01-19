import streamlit as st
import requests

# 페이지 설정
st.set_page_config(page_title="Movie Insight", layout="wide")
BACKEND_URL = "http://34.47.66.39:8000"

# 사이드바 메뉴 구성
menu = st.sidebar.selectbox("메뉴", ["영화 목록", "영화 등록", "리뷰 관리"])

# 1. 영화 목록 표시
if menu == "영화 목록":
    st.header("🎥 등록된 영화 목록")
    # 실제 구현 시에는 requests.get("http://localhost:8000/movies") 사용
    # 예시를 위한 가이드 레이아웃
    try:
        # 백엔드에서 실제 영화 데이터 가져오기
        response = requests.get(f"{BACKEND_URL}/movies/")
        if response.status_code == 200:
            movies = response.json()
            
            if not movies:
                st.info("현재 등록된 영화가 없습니다. '영화 등록' 메뉴에서 영화를 추가해 보세요!")
            else:
                # 3열 그리드 레이아웃 설정
                cols = st.columns(3)
                for idx, m in enumerate(movies):
                    with cols[idx % 3]: # 데이터를 순차적으로 칸에 배치
                        st.markdown(f"### {m['title']}")
                        # 포스터 이미지가 없거나 오류가 날 경우를 대비한 처리
                        img_url = m['poster_url'] if m['poster_url'] and m['poster_url'].startswith("http") else "https://via.placeholder.com/200x300?text=No+Image"
                        st.image(img_url, use_container_width=True)
                        st.write(f"🎬 **감독**: {m['director']}")
                        st.write(f"🎭 **장르**: {m['genre']}")
                        st.divider()
        else:
            st.error("데이터를 불러오는 중 서버 오류가 발생했습니다.")
    except Exception as e:
        st.error(f"백엔드 연결 실패: {e}")

# 2. 영화 등록 (FastAPI POST 요청 준비)
elif menu == "영화 등록":
    st.header("➕ 새로운 영화 등록")
    with st.form("movie_form"):
        title = st.text_input("영화 제목")
        director = st.text_input("감독")
        genre = st.selectbox("장르", ["액션", "SF", "드라마", "코미디", "스릴러"])
        poster_url = st.text_input("포스터 URL (나무위키 등)")
        submitted = st.form_submit_button("등록하기")
        
        if submitted:
            if not title:
                st.error("영화 제목을 입력해주세요.")
            else:
                # 백엔드 DB가 자동으로 생성하므로 'id'는 빼고 보냅니다.
                movie_data = {
                    "title": title, 
                    "release_date": "2026-01-19", 
                    "director": director, 
                    "genre": genre, 
                    "poster_url": poster_url
                }
                
                try:
                    response = requests.post(f"{BACKEND_URL}/movies/", json=movie_data)
                    
                    if response.status_code == 200:
                        st.success(f"✅ '{title}' 영화가 성공적으로 등록되었습니다!")
                        # 등록 후 즉시 확인을 위해 아래에 정보 표시
                        st.image(poster_url if poster_url else "https://via.placeholder.com/150", width=150)
                    else:
                        # 백엔드 터미널에 찍힌 구체적인 에러 확인용
                        st.error(f"서버 오류 발생 (상태 코드: {response.status_code})")
                        st.write(response.text) 
                except Exception as e:
                    st.error(f"백엔드 서버와 연결할 수 없습니다: {e}")

# 3. 리뷰 관리 (심화 기능 포함)
elif menu == "리뷰 관리":
    st.header("📝 리뷰 등록 및 감성 분석")
    
    # 1. 영화 목록 가져오기
    movies = requests.get(f"{BACKEND_URL}/movies/").json()
    movie_titles = [m['title'] for m in movies]
    
    if not movie_titles:
        st.warning("먼저 영화를 등록해주세요.")
    else:
        selected_movie = st.selectbox("영화 선택", movie_titles)
        review_content = st.text_area("리뷰 내용")
        
        if st.button("리뷰 제출"):
            # 백엔드로 리뷰 전송
            review_data = {
                "movie_id": 1, # 실제로는 선택된 영화의 ID 매핑 필요
                "author": "User", "content": review_content
            }
            res = requests.post(f"{BACKEND_URL}/reviews/", json=review_data)
            result = res.json()
            st.write(f"AI 분석 결과: {result['sentiment']}")