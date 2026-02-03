from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Dream:
    id: int | None
    user_id: int
    title: str
    description: str
    date: date
    mood: str
    vividness: int
