from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
import asyncio
import logging
from app.db.base_class import Base
from app.models.log import Log
from app.core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: List[Any]) -> ModelType:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)  # type: ignore
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        if len(obj_in) > 0:
            loop = asyncio.get_event_loop()
            loop.create_task(self.save_log(db, obj_in))
        return obj_in

    async def save_log(self, db: Session, obj_in: CreateSchemaType, response_source: str = settings.RESPONSE_SOURCE_SEMRUSH) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in[0])
        db_obj = self.model(**obj_in_data)

        if db_obj.__class__.__name__ == "BacklinksOverview":
            search_data = obj_in_data.get("domain")
        elif db_obj.__class__.__name__ == "DomainDomains":
            search_data = obj_in_data.get("domains_query")
        elif db_obj.__class__.__name__ == "DomainOrganic":
            search_data = obj_in_data.get("domain")
        elif db_obj.__class__.__name__ == "PhraseRelated":
            search_data = obj_in_data.get("keyword_search")
        else:
            search_data = obj_in_data.get("keyword")

        if response_source == settings.RESPONSE_SOURCE_ROCKKWH:
            unit_cost = 0
        else:
            unit_cost = db_obj.get_unit_value()

        log = Log(
            search_data=search_data,
            search_type=db_obj.__class__.__name__,
            num_rows=len(obj_in),
            source_response=response_source,
            unit_cost=unit_cost
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
