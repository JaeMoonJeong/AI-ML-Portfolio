from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from sqlalchemy.orm import Session

from backend.database import engine, get_db
from backend import models

# [순서 1] DB 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Insight API")

# [순서 2] 감성 분석 모델 임포트
try:
    from backend.ml_model import analyze_sentiment
except ImportError:
    from ml_model import analyze_sentiment

# [순서 3] Pydantic 모델 정의
class MovieSchema(BaseModel):
    id: Optional[int] = None
    title: str
    release_date: str
    director: str
    genre: str
    poster_url: str

    class Config:
        from_attributes = True

class ReviewSchema(BaseModel):
    movie_id: int
    author: str
    content: str
    sentiment: Optional[str] = None

# [순서 4] API 엔드포인트 정의

@app.get("/")
def read_root():
    return {"message": "Server is Running!"}

# 1. 영화 등록 (리스트가 아닌 DB에 저장하도록 수정!)
@app.post("/movies/", response_model=MovieSchema)
def create_movie(movie: MovieSchema, db: Session = Depends(get_db)):
    db_movie = models.Movie(
        title=movie.title,
        release_date=movie.release_date,
        director=movie.director,
        genre=movie.genre,
        poster_url=movie.poster_url
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# 2. 전체 영화 조회 (DB에서 가져오기)
@app.get("/movies/", response_model=List[MovieSchema])
def get_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()

# 3. 리뷰 등록 및 AI 감성 분석 (리뷰도 DB에 저장!)
@app.post("/reviews/")
def create_review(review: ReviewSchema, db: Session = Depends(get_db)):
    sentiment, score = analyze_sentiment(review.content)
    sentiment_result = f"{sentiment} ({score:.2%})"
    
    db_review = models.Review(
        movie_id=review.movie_id,
        author=review.author,
        content=review.content,
        sentiment=sentiment_result
    )
    db.add(db_review)
    db.commit()
    return {"status": "success", "sentiment": sentiment_result}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)