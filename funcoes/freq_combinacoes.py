from classes.sorteio import Sorteio
import itertools
from modulos.extracao_sorteios import extrai_dados
import pandas as pd
from typing import List


def calc_conjuntos_possiveis(tam) -> List[tuple]:
    """
    Calcula todos os conjuntos de tamanho (informar no parametro tam) possíveis com intervalo de 1 a 60

    :param tam: tamanho do conjunto de combinações de 1 a 60

    :return: conjuntos possíveis
    """
    conjs = list(itertools.combinations(range(1, 61), tam))
    return conjs


# noinspection PyShadowingNames
def qtd_conj_sorteado(tam_conjunto: int, sorteios: List[Sorteio]) -> dict:
    """
    :param tam_conjunto: tamanho do conjunto para cálculo dos conjuntos possíveis
    :param sorteios: sorteios extraídos da planilha de dados

    :return dict: matriz
                - lista de conjuntos na key 'conjunto'
                - lista de quantidades na key 'quantidade'
                - lista com a lista de concursos em que o conjunto está presente na key 'concursos'
    """
    combinacoes = calc_conjuntos_possiveis(tam=tam_conjunto)  # Gera uma lista de tuplas com todas as combinações

    conjuntos_qtd = {'conjunto': [],
                     'quantidade': [],
                     'concursos': []}

    qtd_combinacoes = len(combinacoes)
    for i, comb in enumerate(combinacoes, start=1):
        print(f'Calculando combinação {i} de {qtd_combinacoes}...')

        comb_atual = {'comb': comb,
                      'qtd': 0,
                      'concursos': []}
        for sorteio in sorteios:
            if all(num in sorteio.bolas for num in comb):
                comb_atual['qtd'] += 1
                comb_atual['concursos'].append(sorteio.concurso)

        conjuntos_qtd['conjunto'].append(comb_atual['comb'])
        conjuntos_qtd['quantidade'].append(comb_atual['qtd'])
        conjuntos_qtd['concursos'].append(comb_atual['concursos'])
    print('Calculo concluído.')
    return conjuntos_qtd


def criar_planilha(dados, nome_arquivo: str) -> None:
    df = pd.DataFrame(dados)
    df.to_excel(nome_arquivo, index=False, engine='openpyxl')
    print("Dados escritos na planilha com sucesso!")


if __name__ == '__main__':
    sorteios = extrai_dados('../dados/dados_sorteios.xlsx')
    matriz_conj_qtd = qtd_conj_sorteado(1, sorteios)
    criar_planilha(matriz_conj_qtd, 'freq_combinacoes_1.xlsx')
