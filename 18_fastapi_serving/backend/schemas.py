from pydantic import BaseModel
from typing import List, Optional

# 영화 데이터 규격
class MovieBase(BaseModel):
    title: str
    release_date: str
    director: str
    genre: str
    poster_url: Optional[str] = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True

# 리뷰 데이터 규격
class ReviewBase(BaseModel):
    movie_id: int
    author: str
    content: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    sentiment: Optional[str] = None

    class Config:
        from_attributes = True