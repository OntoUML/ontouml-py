from dataclasses import dataclass, field
from typing import Optional

from icecream import ic
from langstring import LangString

from ontouml_py.model.ontoumlelement import OntoumlElement


@dataclass
class NamedElement(OntoumlElement):

    names: set[LangString] = field(default_factory=set)
    alt_names: set[LangString] = field(default_factory=set)
    description: Optional[LangString] = field(default=None)
    editorial_notes: set[LangString] = field(default_factory=set)
    creators: set[str] = field(default_factory=set)
    contributors: set[str] = field(default_factory=set)
