from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import Field

from app.schemas.base_schema import BaseSchema


class MatriculaRequest(BaseSchema):
    codigo_matricula: Annotated[
        str, Field(description="Código da matrícula", examples=["RA12724219602"])
    ]
    nome_curso: Annotated[
        str, Field(description="Nome do curso", examples=["Ciência da Computação"])
    ]
    data_inicio: Annotated[
        datetime, Field(description="Data de início", examples=["04/02/2026"])
    ]
    aluno_id: Annotated[
        UUID,
        Field(
            description="Identificador do aluno a ser matriculado", examples=["RA12724219602"]
        ),
    ]


class MatriculaResponse(BaseSchema):
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
    aluno_id: Annotated[
        UUID,
        Field(
            description="Identificador do aluno a ser matriculado", examples=["RA12724219602"]
        ),
    ]
    data_inclusao: Annotated[
        datetime,
        Field(
            description="Data de inclusão da matricula no sistema",
            examples=["16/01/2026"],
        ),
    ]
    data_atualizacao: Annotated[
        datetime,
        Field(
            description="Data da última atualização de um campo da matrícula no sistema",
            examples=["10/12/2025"],
        ),
    ]


class MatriculaUpdate(BaseSchema):
    codigo_matricula: Annotated[
        str | None, Field(description="Código da matrícula", examples=["RA12724219602"])
    ] = None
    data_inicio: Annotated[
        datetime | None, Field(description="Data de início", examples=["04/02/2026"])
    ] = None
