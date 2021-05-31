from services import string_service
from unittest import TestCase

class StringServiceTestCase(TestCase):
    def test_should_append_hello_world(self):
        service = string_service.StringService()
        assert service.append("Hello ", "World") == "Hello World"