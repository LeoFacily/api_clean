from typing import Generic, List, Optional, TypeVar
import abc

T = TypeVar('T')

class AbstractRepository(abc.ABC, Generic[T]):
  
  @abc.abstractmethod
  def add(self, model: T):
    pass

  @abc.abstractmethod
  def get(self, **kwargs) -> Optional[T]:
    pass

  @abc.abstractmethod
  def all(self) -> List[T]:
    pass