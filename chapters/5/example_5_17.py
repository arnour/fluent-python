from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
    
@dataclass
class HackerClubMember(ClubMember): # HackerClubMember extends ClubMember.
    all_handles: ClassVar[set[str]] = set() # all_handles is a class attribute
    handle: str = '' # handle is an instance field of type str with an empty string as its default value; this makes it optional
    
    # Common use cases for __post_init__ are validation and computing field values based on other fields.
    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)
            
anna = HackerClubMember('Anna Ravenscroft', handle='AnnaRaven')

assert str(anna) == "HackerClubMember(name='Anna Ravenscroft', guests=[], handle='AnnaRaven')"

leo = HackerClubMember('Leo Rochael')

assert str(leo) == "HackerClubMember(name='Leo Rochael', guests=[], handle='Leo')"

try:
    leo2 = HackerClubMember('Leo DaVinci')
except ValueError as err:
    assert str(err) == "handle 'Leo' already exists."