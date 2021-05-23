from src.services import string_service

def test_should_append_hello_world():
    service = string_service.StringService()
    assert service.append("Hello ", "World") == "Hello World"