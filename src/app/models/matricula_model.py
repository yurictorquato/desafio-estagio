from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.aluno_model import Aluno
from app.models.base_model import BaseModel


class Matricula(BaseModel):
    __tablename__ = "tb_matriculas"

    codigo_matricula: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    nome_curso: Mapped[str] = mapped_column(String(50), nullable=False)
    data_inicio: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    aluno_id: Mapped[UUID] = mapped_column(ForeignKey("tb_alunos.id"), nullable=False)

    aluno: Mapped["Aluno"] = relationship(argument="Aluno", back_populates="matriculas")

    def __repr__(self) -> str:
        return f"<Matricula(codigo_matricula={self.codigo_matricula!r}, nome_curso={self.nome_curso!r})>"
