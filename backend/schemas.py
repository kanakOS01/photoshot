from enum import Enum
from pydantic import BaseModel
from typing import List


class TrainType(str, Enum):
    Man = "Man"
    Woman = "Woman"
    Other = "Other"


class EthnicityTypes(str, Enum):
    White = "White"
    Black = "Black"
    AsianAmerican = "Asian American"
    EastAsian = "East Asian"
    SouthEastAsian = "South East Asian"
    MiddleEastern = "Middle Eastern"
    Pacific = "Pacific"
    Hispanic = "Hispanic"


class EyeColorTypes(str, Enum):
    Brown = "Brown"
    Blue = "Blue"
    Hazel = "Hazel"
    Green = "Green"
    Grey = "Grey"


class TrainModel(BaseModel):
    name: str
    type: TrainType
    age: int
    ethnicity: EthnicityTypes
    eyecolor: EyeColorTypes
    bald: bool
    images: List[str]


class GenereateImage(BaseModel):
    prompt: str
    model_id: str


class GeneratePackImage(BaseModel):
    pack_id: str
    model_id: str
