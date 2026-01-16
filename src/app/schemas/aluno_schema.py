from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import Field

from app.schemas.base_schema import BaseSchema


class AlunoRequest(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do aluno", examples=["Yuri Cruz Torquato"], max_length=50
        ),
    ]
    telefone: Annotated[
        str,
        Field(
            description="Telefone de contato do aluno",
            examples=["71982580127"],
            min_length=11,
            max_length=11,
        ),
    ]
    data_nascimento: Annotated[
        datetime,
        Field(description="Data de nascimento do aluno", examples=["11/04/2000"]),
    ]


class AlunoResponse(AlunoRequest):
    id: Annotated[UUID, Field(description="Identificador do aluno")]
    data_inclusao: Annotated[
        datetime,
        Field(
            description="Data de inclusão do aluno no sistema", examples=["16/01/2026"]
        ),
    ]
    data_atualizacao: Annotated[
        datetime,
        Field(
            description="Data da última atualização de um campo do aluno no sistema",
            examples=["10/12/2025"],
        ),
    ]


class AlunoUpdate(BaseSchema):
    telefone: Annotated[
        str | None,
        Field(
            description="Telefone de contato do aluno",
            examples=["71982580127"],
            min_length=11,
            max_length=11,
        ),
    ] = None
