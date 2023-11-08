from classes.sorteio import Sorteio
from datetime import datetime
from modulos.extracao_sorteios import extrai_dados
from typing import List


class Estatistica:
    def __init__(self):
        """
        Diversas informações estatísticas sobre os concursos presentes na planilha de dados
        """
        self._sorteios = None
        self._freq_numeros = None
        self._num_mais_sorteado = None
        self._num_menos_sorteado = None

    @property
    def sorteios(self) -> List[Sorteio]:
        return self._sorteios

    @sorteios.setter
    def sorteios(self, value: List[Sorteio]):
        self._sorteios = value

    @property
    def concursos(self) -> List[Sorteio]:
        return self._sorteios

    @property
    def frequencia_num(self) -> dict:
        return self._freq_numeros

    @property
    def num_mais_sorteado(self) -> tuple:
        return self._num_mais_sorteado

    @property
    def num_menos_sorteado(self) -> tuple:
        return self._num_menos_sorteado

    def calcula_freq_numeros(self, data_inicial='01/01/1996') -> None:
        """
            Calcula a frequência em que cada número foi sorteado

            Função altera o atributo freq_numeros,
            adicionando o dicionário com a frequência de cada número
            :param data_inicial: data inicial para fazer o cálculo, por padrão a contagem inicia em 01/01/1996
            :return: None
            """
        # Dicionário para contar a frequência de cada número
        numeros_possiveis = range(1, 61)
        freq_num_sorteios = {n: 0 for n in numeros_possiveis}  # Cria dicionário com chaves de 1 a 60 com o valor 0

        data_inicial_f = datetime.strptime(data_inicial, '%d/%m/%Y').date()
        for sorteio in self._sorteios:
            data_concurso = datetime.strptime(sorteio.data, '%d/%m/%Y').date()
            if data_concurso >= data_inicial_f:
                for n in range(1, 61):
                    if n in sorteio.bolas:
                        freq_num_sorteios[n] += 1

        self._freq_numeros = freq_num_sorteios

    def calcula_num_mais_sort(self) -> None:
        """
        Calcula o número mais sorteado

        Função altera o atributo num_mais_sorteado,
        adicionando uma tupla com o número mais sorteado e a quantidade.

        :return: None
        """
        freq_nums = self._freq_numeros
        num_qtd = max(freq_nums.items(), key=lambda item: item[1])
        self._num_mais_sorteado = num_qtd

    def calcula_num_menos_sort(self) -> None:
        """
        Calcula o número menos sorteado

        Função altera o atributo num_menos_sorteado,
        adicionando uma tupla com o número menos sorteado e a quantidade.

        :return: None
        """
        freq_nums = self._freq_numeros
        num_qtd = min(freq_nums.items(), key=lambda item: item[1])
        self._num_menos_sorteado = num_qtd

    def ordena_freq_numeros(self, op='mais_sort') -> dict or None:
        """
        Ordena o dicionário de estatísticas de frequência de números

        :param op: define as opções de ordenação, por padrão ordena do mais sorteado ao menos sorteado
            -> 'mais_sort' ordena do número mais sorteado ao menos
            -> 'menos_sort' ordena do número menos sorteado ao mais

        :return dict: ordenado de acordo com a opção
        """
        freq_nums = self._freq_numeros
        if op == 'menos_sort':
            reverse = False
        elif op == 'mais_sort':
            reverse = True
        else:
            print('Opção inválida!')
            return None

        freq_ordenada = dict(sorted(freq_nums.items(), key=lambda item: item[1], reverse=reverse))
        return freq_ordenada

    def verifica_acertos(self, palpite: list, min_acerto=2) -> List[dict]:
        """
        Verifica quantidade de acertos em jogos anteriores considerando um palpite

        :param palpite: lista com os números para palpite
        :param min_acerto: quantidade minima de acertos para considerar

        :return list: contendo dicionários com os acertos
        """
        resultado_acertos = []
        for sorteio in self._sorteios:
            intersecao = set(sorteio.bolas) & set(palpite)
            qtd = len(intersecao)
            if qtd >= min_acerto:
                acerto_ordenado = list(intersecao)
                acerto_ordenado.sort()
                palpite_ordenado = palpite
                palpite_ordenado.sort()
                inf = {'inf_concurso': sorteio.__repr__(),
                       'palpite': palpite_ordenado,
                       'qtd_acertos': qtd,
                       'acertos': acerto_ordenado
                       }
                resultado_acertos.append(inf)
        return resultado_acertos


if __name__ == '__main__':
    sorteios = extrai_dados('../dados/dados_sorteios.xlsx')
    stt = Estatistica()
    stt.sorteios = sorteios
    stt.calcula_freq_numeros('01/05/2023')
    stt.calcula_num_mais_sort()
    print(stt.num_mais_sorteado)
