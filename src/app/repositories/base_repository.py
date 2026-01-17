from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import BaseModel
from app.schemas.base_schema import BaseSchema

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseSchema)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseSchema)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType], db_session: AsyncSession) -> None:
        self.model = model
        self.db_session = db_session

    async def save(self, schema: CreateSchemaType) -> ModelType:
        new_entity = self.model(**schema.model_dump())

        self.db_session.add(new_entity)

        await self.db_session.commit()
        await self.db_session.refresh(new_entity)

        return new_entity

    async def find_by_id(self, entity_id: UUID) -> ModelType | None:
        result = await self.db_session.execute(
            select(self.model).where(self.model.id == entity_id)
        )

        return result.scalar_one_or_none()

    async def find_all(self, offset: int = 0, limit: int = 10) -> list[ModelType]:
        result = await self.db_session.execute(
            select(self.model).offset(offset).limit(limit)
        )

        return list(result.scalars().all())

    async def update(
        self, entity_id: UUID, schema: UpdateSchemaType
    ) -> ModelType | None:
        update_data = schema.model_dump(exclude_unset=True)

        if not update_data:
            result = await self.db_session.execute(
                select(self.model).where(self.model.id == entity_id)
            )

            return result.scalar_one_or_none()

        result = await self.db_session.execute(
            update(self.model)
            .where(self.model.id == entity_id)
            .values(**update_data)
            .returning(self.model)
        )

        await self.db_session.commit()

        return result.scalar_one_or_none()

    async def delete(self, entity_id: UUID) -> bool:
        result = await self.db_session.execute(
            delete(self.model).where(self.model.id == entity_id).returning(self.model.id)
        )

        await self.db_session.commit()

        return result.scalar_one_or_none() is not None
