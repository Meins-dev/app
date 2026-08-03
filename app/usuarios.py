from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    nome_exibicao: str
    idade: Optional[int] = None
    telefone: Optional[str] = None
    foto: Optional[str] = None  # filename of the photo, e.g., "user.jpg"

class ErroAutenticacao(Exception):
    pass