from typing import List

def filtra_dados(lista: List[float], limite: float) -> List[float]:
    filtro: List[float] = []
    for valor in lista:
        if valor < limite:
            filtro.append(valor)
    return filtro