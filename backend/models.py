from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from sqlalchemy.types import TIMESTAMP

from backend.schemas import TrainType, EthnicityTypes, EyeColorTypes


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    profile_pic: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=text("now()"), onupdate=text("now()"))

    def __repr__(self) -> str:
        return f"User(id={self.id}!r, username={self.username!r})"


class TrainingImages(Base):
    __tablename__ = "training_images"

    id: Mapped[str] = mapped_column(primary_key=True)
    image_url: Mapped[str] = mapped_column(nullable=False)
    model_id: Mapped[str] = mapped_column(ForeignKey("models.id", ondelete='CASCADE', onupdate='CASCADE'))

    owner = relationship("Model", back_populates="training_images")


class OutputImages(Base):
    __tablename__ = "output_images"

    id: Mapped[str] = mapped_column(primary_key=True)
    image_url: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[str] = mapped_column(nullable=False) # to link a user to output img without a foreign key (just query)
    model_id: Mapped[str] = mapped_column(ForeignKey("models.id", ondelete='CASCADE', onupdate='CASCADE'))
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=text("now()"), index=True)

    owner = relationship("Model", back_populates="output_images")


class Model(Base):
    __tablename__ = "models"
   
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[TrainType] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    ethnicity: Mapped[EthnicityTypes] = mapped_column(nullable=False)
    eyecolor: Mapped[EyeColorTypes] = mapped_column(nullable=False)
    bald: Mapped[bool] = mapped_column(nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=text("now()"), onupdate=text("now()"))
    training_images: Mapped[List[TrainingImages]] = relationship("TrainingImages", back_populates="owner")
    output_images: Mapped[List[OutputImages]] = relationship("OutputImages", back_populates="owner")


class PackPrompts(Base):
    __tablename__ = "pack_prompts"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    pack_id: Mapped[str] = mapped_column(ForeignKey("packs.id", ondelete='CASCADE', onupdate='CASCADE'))

    owner = relationship("Packs", back_populates="prompts")


class Packs(Base):
    __tablename__ = "packs"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    prompts: Mapped[List[PackPrompts]] = relationship("PackPrompts", back_populates="owner")
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=text("now()"), onupdate=text("now()"))