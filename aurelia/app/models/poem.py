from dataclasses import dataclass
from datetime import datetime

@dataclass
class Poem:
    id: int | None
    author_id: int
    dream_id: int
    content: str
    created_at: datetime
