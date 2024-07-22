from typing import List

def converte_fahrenheit(teperaturas: List[float]) -> List[float]:
    fahrenheit = [(9/5) * temp + 32 for temp in teperaturas]
    return fahrenheit