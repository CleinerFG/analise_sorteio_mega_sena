from datetime import datetime
from typing import List


class Sorteio:
    """
    Representa um sorteio individual, contendo o número do concurso, data do sorteio e bolas sorteadas.
    """

    def __init__(self, concurso: int, data: datetime, bolas: list):
        self._concurso = concurso
        self._data = data
        self._bolas = bolas

    @property
    def concurso(self) -> int:
        return self._concurso

    @property
    def data(self) -> datetime:
        return self._data

    @property
    def bolas(self) -> List[int]:
        return self._bolas

    def __repr__(self):
        return f'Concurso: {self._concurso} data: {self._data} bolas: {self._bolas}'

    def __str__(self):
        return f'Concurso: {self._concurso} data: {self._data} bolas: {self._bolas}'
