from dataclasses import dataclass

@dataclass
class Symbol:
    id: int | None
    name: str
    description: str
