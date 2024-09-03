from dataclasses import dataclass, InitVar
from typing import Optional
@dataclass
class DatabaseType:
    def lookup(self, field):
        return 'a'

@dataclass
class C:
    i: int
    j: Optional[int] = None
    database: InitVar[DatabaseType] = None
    
    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')


c = C(10, database=DatabaseType())

assert str(c) == "C(i=10, j='a')"