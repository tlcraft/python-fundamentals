from example_module.example_class import Example
from unittest import TestCase, mock

# Mock where the component is used, not where it's defined
@mock.patch('example_module.example_class.StringService', autospec=True)
class ExampleTestCase(TestCase):
    def test_should_add_one(self, mock_service):
        example = Example(mock_service)
        assert example.add_one(3) == 4

    def test_should_get_count(self, mock_service):
        mock_service.append = mock.Mock(return_value="TestAppend")
        example = Example(mock_service)
        assert example.get_count() == "TestAppend"
        mock_service.append.assert_called_once_with("Count: ", 2)
