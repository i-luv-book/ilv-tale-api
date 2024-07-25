from pydantic import BaseModel
from pydantic import Field
from typing import List

class Keyword(BaseModel):
    traits: List[str] = Field(None,example="누구(형상)에 관한 키워드")
    characters: List[str] = Field(None,example="주인공에 관한 키워드")
    settings: List[str] = Field(None,example="배경에 관한 키워드")
    genre: List[str] = Field(None,example = "장르에 관한 키워드")

class GameFairyTaleRequestDTO(BaseModel):
    keywords: Keyword = Field(None,example="동화 생성 키워드")
    fairytale: str = Field(None,example="이전의 생성된 동화(옵션 포함)")

class Option(BaseModel):
    optionTitle: str = Field(None,example="선택지 제목")
    optionContent : str = Field(None,example="선택지 내용")

class GameFairyTaleResponseDTO(BaseModel):
    title : str = Field(None,example="동화 제목")
    content : str = Field(None,example="동화 내용")
    options : List[Option] = Field(None,example="선택지 3개")
    imgURL: str = Field(None, example="동화 이미지")

class GameEndFairyTaleResponseDTO(BaseModel):
    title : str = Field(None,example="게임형 동화 제목")
    content : str = Field(None,example="게임형 동화 마지막 내용")
    imgURL: str = Field(None, example="동화 이미지")

class FairyTaleRequestDTO(BaseModel):
    keywords: Keyword = Field(None,example="동화 생성 키워드")

class Page(BaseModel):
    content : str = Field(None,example="동화 첫 페이지")
    imgURL : str = Field(None,example ="동화 이미지")

class FairyTaleResponseDTO(BaseModel):
    title : str = Field(None,example="동화 제목")
    pages: List[Page] = Field(None,example="동화 내용들")
    summary : str = Field(None,example="동화 요약문")

