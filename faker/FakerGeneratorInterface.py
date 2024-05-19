from abc import ABC, abstractmethod
from ETLPipeline import PostgresDatabaseConnection

class FakerGeneratorInterface(ABC):
    @abstractmethod
    def numberUpdatedRecord(self) -> int:
        pass

    @abstractmethod
    def numberInsertedRecord(self) -> int:
        pass

    @abstractmethod
    def update(self, updated_row_count: int) -> int:
        pass

    @abstractmethod
    def insert(self, inserted_row_count: int) -> int:
        pass
