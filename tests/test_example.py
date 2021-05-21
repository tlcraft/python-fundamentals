from src.example import Example
from src.services.string_service import StringService

def test_should_add_one():
    service = StringService()
    example = Example(service)
    assert example.add_one(3) == 4
