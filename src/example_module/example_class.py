from services import string_service

class Example:
    def __init__(self, stringService: string_service.StringService):
        self.stringService = stringService

    def add_one(self, x: int):
        return x + 1

    def get_count(self):
        number = self.add_one(1)
        string = self.stringService.append("Count: ", number)
        return string