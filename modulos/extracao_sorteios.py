from classes.sorteio import Sorteio
import pandas as pd


# noinspection PyShadowingNames
def extrai_dados(plan_xlsx) -> list:
    """
    Faz a leitura da planilha e organiza os dados
    Colunas na planilha -> concurso, data, bola {i} (i de 1 até 6)

    :param plan_xlsx: planilha com os dados sobre os sorteios
    :return: lista de objetos Sorteio
    """
    sheet = pd.read_excel(plan_xlsx)
    df = sheet.to_dict(orient='records')

    sorteios = []
    for item in df:
        bolas = []
        for i in range(1, 7):
            bolas.append(item[f'bola{i}'])

        s = Sorteio(item['concurso'], item['data'], bolas)
        sorteios.append(s)
    return sorteios


if __name__ == "__main__":
    sorteios = extrai_dados('../dados_sorteios.xlsx')
    for s in sorteios:
        print(s)
