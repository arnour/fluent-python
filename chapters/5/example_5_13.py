from dataclasses import dataclass

try:
    @dataclass    
    class ClubMember:
        name: str
        gests: list = []
except ValueError as err:
    assert str(err) == "mutable default <class 'list'> for field gests is not allowed: use default_factory"