import uuid
from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class OntoumlElement():
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created: datetime = field(default_factory=datetime.now)
    modified: Optional[datetime] = None

    def __post_init__(self):
        if not self.id:
            raise ValueError("The 'id' field must not be empty.")

