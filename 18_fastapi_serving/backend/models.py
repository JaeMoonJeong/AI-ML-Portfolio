from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Movie(Base): # <--- 이 이름이 'Movie'여야 합니다!
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    release_date = Column(String)
    director = Column(String)
    genre = Column(String)
    poster_url = Column(String)

    # 리뷰와의 관계 설정 (선택 사항이지만 있으면 좋습니다)
    reviews = relationship("Review", back_populates="movie")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    author = Column(String)
    content = Column(Text)
    sentiment = Column(String)

    movie = relationship("Movie", back_populates="reviews")