from example_module.example_class import Example
from services.string_service import StringService

def test_should_add_one():
    service = StringService()
    example = Example(service)
    assert example.add_one(3) == 4

