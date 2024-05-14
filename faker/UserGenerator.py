from .FakerGeneratorInterface import FakerGeneratorInterface
from ETLPipeline import PostgresDatabaseConnection
from faker import Faker
import random

class UserGenerator(FakerGeneratorInterface):
    def __init__(self, connection: PostgresDatabaseConnection):
        self.conn = connection

    def numberUpdatedRecord(self) -> int:
        rate = random.uniform(0.15, 0.20)
        cur_manager = self.conn.connect()
        with cur_manager as cur:
            cur.execute(f"SELECT COUNT(*) FROM {self.cur.database}.users;")
            row_count = int(cur.fetchone()[0]) * 1.0
            return round(rate * row_count)
        
    def numberInsertedRecord(self) -> int:
        rate = random.uniform(0.25, 0.30)
        cur_manager = self.conn.connect()
        with cur_manager as cur:
            cur.execute(f"SELECT COUNT(*) FROM {self.cur.database}.users;")
            row_count = int(cur.fetchone()[0]) * 1.0
            return round(rate * row_count)
        
    def update(self) -> int:
        