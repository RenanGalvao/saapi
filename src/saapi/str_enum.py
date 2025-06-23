import sys
from enum import Enum

# Verifica se StrEnum está disponível (Python 3.11+)
if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    # Implementação compatível para Python 3.8
    class StrEnum(str, Enum):
        def __str__(self) -> str:
            return self.value
