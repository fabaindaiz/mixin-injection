from core import provider
from pydantic import BaseModel

class FactoryConfig(BaseModel):
    key1: str
    key2: str

class Type1FactoryConfig(BaseModel):
    factory: FactoryConfig

@provider(
)
class Type1Factory:
    def __init__(self, cfg: dict):
        self.__cfg = self.get_config(cfg)
        print(f"Factory init: {self.__cfg.model_dump()}")
    
    @staticmethod
    def get_config(cfg: dict) -> Type1FactoryConfig:
        return Type1FactoryConfig(**cfg)

    def work(self):
        print("Factory work")