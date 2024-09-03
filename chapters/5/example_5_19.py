from typing import Optional
from dataclasses import dataclass, field, fields
from enum import Enum, auto
from datetime import date


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    identifier: str  # identifier is the only required field.
    title: str = (
        "<untitled>"  # title is the first field with a default. This forces all fields below to provide defaults.
    )
    creators: list[str] = field(default_factory=list)
    created_at: Optional[date] = (
        None  # The value of date can be a datetime.date instance, or None.
    )
    type: ResourceType = (
        ResourceType.BOOK
    )  # This Enum will provide type-safe values for the Resource.type field. The type field default is ResourceType.BOOK
    description: str = ""
    language: str = ""
    subjects: list[str] = field(default_factory=list)

    def __repr__(self) -> str:
        cls = self.__class__
        cls_name = cls.__name__
        indent = " " * 4
        res = [f"{cls_name}("]
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f"{indent}{f.name} = {value!r},")
        res.append(")")
        return "\n".join(res)


description = "Improving the design of existing code"
book = Resource(
    "978-0-13-475759-9",
    "Refactoring, 2nd Edition",
    ["Martin Fowler", "Kent Beck"],
    date(2018, 11, 19),
    ResourceType.BOOK,
    description,
    "EN",
    ["computer programming", "OOP"],
)

assert (
    str(book)
    == """Resource(
    identifier = '978-0-13-475759-9',
    title = 'Refactoring, 2nd Edition',
    creators = ['Martin Fowler', 'Kent Beck'],
    created_at = datetime.date(2018, 11, 19),
    type = <ResourceType.BOOK: 1>,
    description = 'Improving the design of existing code',
    language = 'EN',
    subjects = ['computer programming', 'OOP'],
)"""
)
