from typing import List

#2_Filtrar Dados Acima de um Limite
def filtrar_valores_acima_de(valores: list[float], limite:float) -> list[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado