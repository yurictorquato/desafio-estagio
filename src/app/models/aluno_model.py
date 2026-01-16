from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel
from app.models.matricula_model import Matricula


class Aluno(BaseModel):
    __tablename__ = "tb_alunos"

    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    telefone: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    data_nascimento: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    matriculas: Mapped[list["Matricula"]] = relationship(
        argument="Matricula", back_populates="aluno", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Aluno(id={self.id!r}, nome={self.nome!r})>"
