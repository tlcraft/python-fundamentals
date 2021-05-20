from src.services.string_service import StringService

def test_should_append_hello_world():
    service = StringService()
    assert service.append("Hello ", "World") == "Hello World"