import csv

def extrai_populacao():
    file = open('../data/dados_processados/populacao.csv')

def extrai_csv(file, info1, info2, info3):
    infos = csv.reader(open(file))
    _ = next(infos)
    values = []
    for row in infos:
        if (row[1] != '' and len(row[1]) <= 3):
            value = []
            value.append(row[info1]) # info1
            value.append(row[info2]) # info2
            value.append(row[info3]) # info3
            # print(value)
            values.append(value)

    return values

from typing import Dict, List, Any

def imprimir_dict_como_tabela(header, dados: Dict[str, List[Any]], marcador_nulo: str = "--") -> None:
    """
    Imprime os valores das listas contidas em um dicionário como uma tabela formatada no terminal.

    Args:
        dados (Dict[str, List[Any]]): Dicionário onde cada valor é uma lista de dados.
        marcador_nulo (str): Texto a ser exibido no lugar de valores None.
    """
    if not dados:
        print("Dicionário vazio.")
        return

    # Extrair todas as linhas a partir dos valores
    linhas = []
    chaves = list(dados.keys())

    for chave in chaves:
        linha = []
        for valor in dados[chave]:
            if valor is None:
                linha.append(marcador_nulo)
            else:
                linha.append(str(value_to_str(valor)))
        linhas.append(linha)

    # Inserir índice da linha como primeira coluna
    for i, linha in enumerate(linhas):
        linha.insert(0, str(i))  # ou use `chaves[i]` se quiser usar a chave como label

    # Criar cabeçalho
    tamanho_linha = len(linhas[0])
    cabecalho = ["#"] + [h for h in header]

    # Calcular larguras de coluna
    larguras = [
        max(len(cabecalho[i]), max(len(linha[i]) for linha in linhas))
        for i in range(tamanho_linha)
    ]

    def formatar_linha(c: List[str]) -> str:
        return " | ".join(f"{c[i]:<{larguras[i]}}" for i in range(tamanho_linha))

    # Imprimir
    print(formatar_linha(cabecalho))
    print("-" * (sum(larguras) + 3 * (tamanho_linha - 1)))
    for linha in linhas:
        print(formatar_linha(linha))


def value_to_str(valor: Any) -> str:
    """Formata o valor numérico com casas decimais, se necessário."""
    if isinstance(valor, float):
        return f"{valor:.2f}"
    return str(valor)

import csv
from typing import List

def salvar_em_csv(nome_arquivo: str, dados: List[List[str]], separador: str = ",") -> None:
    """
    Salva uma lista de listas em um arquivo CSV.

    Args:
        nome_arquivo (str): Nome do arquivo de saída, por exemplo, 'saida.csv'.
        dados (List[List[str]]): Lista de listas, onde cada sublista representa uma linha do CSV.
        separador (str): Separador de colunas (padrão é vírgula).
    """
    try:
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
            writer = csv.writer(arquivo_csv, delimiter=separador, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for linha in dados:
                writer.writerow(linha)
        print(f"Arquivo CSV salvo com sucesso: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
