from dependency.core import provider
from dependency_injector import providers
from example.services.settings import Config
from example.services.factory import Factory

@provider(
    component=Factory,
    provider=providers.Factory
)
class Type1Factory(Factory):
    def __init__(self, cfg: dict):
        self.__cfg = Config(**cfg)
        print(f"Factory init")

    def work(self):
        print("Factory work")