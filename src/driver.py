from example_module.example_class import Example
from services.string_service import StringService

def main():
    service = StringService()
    example = Example(service)
    print(example.get_count())

if __name__ == '__main__':
    main()