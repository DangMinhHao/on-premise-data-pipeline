from abc import ABC, abstractmethod
from ETLPipeline import PostgresDatabaseConnection

class FakerGeneratorInterface(ABC):
    @abstractmethod
    def numberUpdatedRecord(self, connection: PostgresDatabaseConnection) -> int:
        pass

    @abstractmethod
    def numberInsertedRecord(self, connection: PostgresDatabaseConnection) -> int:
        pass

    @abstractmethod
    def update(self, connection: PostgresDatabaseConnection) -> int:
        pass

    @abstractmethod
    def insert(self, connection: PostgresDatabaseConnection) -> int:
        pass
