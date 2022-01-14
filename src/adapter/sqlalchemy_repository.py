from typing import List, Optional, Type
from src.common.abstracts.repository import T, AbstractRepository


class SqlAlchemyRepository(AbstractRepository[T]):

    def __init__(self, session, model: Type[T]):
        self.session = session
        self.model = model

    def add(self, model: T):
        self.session.add(model)
        return model

    def get(self, **kwargs) -> Optional[T]:
        return self.session.query(self.model).filter_by(**kwargs).first()

    def all(self) -> List[T]:
        return self.session.query(self.model).all()
