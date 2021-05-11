from src.services.stringService import append

def test_append():
    assert append("Hello ", "World") == "Hello World"