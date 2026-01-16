from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import Field

from app.schemas.base_schema import BaseSchema


class MatriculaSimplificada(BaseSchema):
    id: Annotated[UUID, Field(description="Identificador da matrícula")]
    codigo_matricula: Annotated[
        str, Field(description="Código da matrícula", examples=["RA12724219602"])
    ]
    nome_curso: Annotated[
        str, Field(description="Nome do curso", examples=["Ciência da Computação"])
    ]
    data_inicio: Annotated[
        datetime, Field(description="Data de início", examples=["04/02/2026"])
    ]


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


class AlunoResponse(BaseSchema):
    id: Annotated[UUID, Field(description="Identificador do aluno")]
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
    matriculas: Annotated[
        list[MatriculaSimplificada],
        Field(description="Lista de matrículas do aluno", default_factory=list),
    ] = []


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
