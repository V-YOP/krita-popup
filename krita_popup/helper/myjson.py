import json
from dataclasses import dataclass, asdict, is_dataclass, fields
from typing import Any, Type, TypeVar, get_type_hints

T = TypeVar('T')

def dataclass_to_dict(obj: Any) -> Any:
    if is_dataclass(obj):
        return {k: dataclass_to_dict(v) for k, v in asdict(obj).items()}
    elif isinstance(obj, (list, tuple)):
        return [dataclass_to_dict(v) for v in obj]
    elif isinstance(obj, dict):
        return {k: dataclass_to_dict(v) for k, v in obj.items()}
    else:
        return obj

def dict_to_dataclass(cls: Type[T], data: Any) -> T:
    if isinstance(data, dict):
        fieldtypes = get_type_hints(cls)
        return cls(**{k: dict_to_dataclass(fieldtypes[k], v) for k, v in data.items() if k in fieldtypes})
    elif isinstance(data, list):
        # Assume it's a list of dataclass instances
        return [dict_to_dataclass(cls.__args__[0], v) for v in data]  # cls.__args__[0] for generic types like List[Type]
    else:
        return data

def dumps(obj: Any) -> str:
    return json.dumps(dataclass_to_dict(obj), indent=4)

def loads(cls: Type[T], json_str: str) -> T:
    data = json.loads(json_str)
    return dict_to_dataclass(cls, data)

if __name__ == '__main__':
    # 示例dataclass
    @dataclass
    class Address:
        city: str
        zipcode: str

    @dataclass
    class Person:
        name: str
        age: int
        address: Address

    # 示例使用
    person = Person(name="John Doe", age=30, address=Address(city="New York", zipcode="10001"))
    json_str = dumps(person)
    print(json_str)

    person_obj = loads(Person, json_str)
    print(person_obj)
