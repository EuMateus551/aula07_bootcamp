import csv
import typing 


def ler_arquivo_csv(nome_do_arquivo):
    with open(nome_do_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor= csv.DictReader(arquivo)
        return list[leitor]
    
def processar_dados(dados):
    categorias = {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

def calcular_vendas_por_categorias(dados):
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria

def main():
    nome_arquivo = "vendas.csv"
    dados_brutos = ler_arquivo_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_por_categorias(dados_processados)
    for categoria, total in vendas_categoria.items():
        print(f"{categoria}: ${total}")

if __name__ == "__main__":
    main()