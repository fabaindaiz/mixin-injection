from src.service2 import Service2

class Service2Instance1(Service2):
    def init(self, cfg: dict):
        print(f"serv2: {cfg}")

    def work(self):
        print("Service2 work")