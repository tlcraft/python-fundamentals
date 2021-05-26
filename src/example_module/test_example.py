from example_module import example_class
from services import string_service

def test_should_add_one():
    service = string_service.StringService()
    example = example_class.Example(service)
    assert example.add_one(3) == 4

