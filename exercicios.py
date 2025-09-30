from typing import List

#1_Calcular Média de Valores em uma Lista
def calcular_media(valores: list[float]) -> float:
    return sum(valores)/len(valores)

#2_Filtrar Dados Acima de um Limite
def filtrar_valores_acima_de(valores: list[float], limite:float) -> list[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

#3_Contar Valores Únicos em uma Lista
def contar_valores_unicos(valores: list[float]) -> float:
    return len(set(valores))

#4_Converter Celsius para Fahrenheit em uma Lista
def celsius_para_farenheit(temperaturas_em_celsiu: list[float]) -> list[float]:
    temperaturas_em_fahrenheit= []
    for temperatura in temperaturas_em_celsiu:
        temperatura_fahrenheit = (temperatura*1.8) + 32
        temperaturas_em_fahrenheit.append(temperatura_fahrenheit)
    return temperaturas_em_fahrenheit

#5_Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(desvios: list[float]) -> float:
    media=sum(desvios)/len(desvios)
    variancia = sum((x-media)**2 for x in desvios)/len(desvios)
    return variancia ** 0.5

#6_Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: list[int]) -> list[int]:
    completo = set(range(min(sequencia), max(sequencia)+1))
    return list(completo - set(sequencia))