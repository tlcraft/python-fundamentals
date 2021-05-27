from services.string_service import StringService

class Example:
    def __init__(self, stringService: StringService):
        self.stringService = stringService

    def add_one(self, x: int) -> int:
        return x + 1

    def get_count(self) -> str:
        number = self.add_one(1)
        string = self.stringService.append("Count: ", number)
        return string