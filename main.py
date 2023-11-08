from classes.estatistica import Estatistica
from funcoes.freq_combinacoes import criar_planilha, qtd_conj_sorteado
from funcoes.graficos import grafico
from funcoes.interface import menu
from modulos.extracao_sorteios import extrai_dados
from utils.utils_generic import colors

opcoes = ['Alterar Intervalo de Análise', 'Número mais e menos sorteado', 'Frequência dos números',
          'Verificar palpite em jogos que já ocorreram',
          'Gerar planilha de frequência de conjuntos', 'Mostrar gráfico de frequência de números', 'Encerrar']

dados = extrai_dados('dados/dados_sorteios.xlsx')

stt = Estatistica()
stt.sorteios = dados
stt.calcula_freq_numeros()

while True:
    menu(opcoes)
    op = input('Opção: ')
    print('-' * 60)

    if op == '1':  # Alterar Intervalo de Análise
        stt.calcula_freq_numeros(input('Data inicial formato(dd/mm/YYYY): '))

    elif op == '2':  # Número mais e menos sorteado
        stt.calcula_num_mais_sort()
        stt.calcula_num_menos_sort()

        res = stt.num_mais_sorteado
        print(f'Número mais sorteado: {res[0]} --> qtd: {res[1]}')

        res = stt.num_menos_sorteado
        print(f'Número menos sorteado: {res[0]} --> qtd: {res[1]}')

    elif op == '3':  # Frequência dos números
        while True:
            print('Ordenação padrão de 1 a 60, definir nova ordenação...\n'
                  '1 - mais ao menos\n'
                  '2 - menos ao mais\n'
                  '3 - Fechar')
            print('-' * 60)
            op = input('Ordenar a frequência: ')
            print('-' * 60)
            if op == '1':
                res = stt.ordena_freq_numeros(op='mais_sort')
            elif op == '2':
                res = stt.ordena_freq_numeros(op='menos_sort')
            elif op == '3':
                break
            else:
                print('Opção inválida!')
                continue
            print('Número'.ljust(6), 'Quantidade')
            for k, v in res.items():
                print(f'{k}'.ljust(6), v)
            print('-' * 60)

    elif op == '4':  # Verificar palpite em jogos que já ocorreram
        qtd_min_acerto = int(input('Quantidade minima de acerto(2 a 6): '))
        palpite = []

        i = 1
        while True:
            n = int(input(f'Número {i}: '))
            if n not in palpite:
                palpite.append(n)
                i += 1
            else:
                print(f'{n} já existe!')
            if i > 6:
                break

        res = stt.verifica_acertos(palpite, qtd_min_acerto)

        if res:
            print('-' * 100)
            for item in res:
                print(f'{item["inf_concurso"]}\n'
                      f'Palpite: {item["palpite"]}\n'
                      f'Quantidade de acertos: {item["qtd_acertos"]}\n'
                      f'Acertos: {item["acertos"]}')
                print('-' * 100)
        else:
            print('Sua palpite não acertou mais do que 2 números em nenhum jogo passado!')

    elif op == '5':  # Gerar planilha de frequência de conjuntos
        print(colors('Atenção quanto maior o conjunto mais tempo vai demorar o cálculo!', 'strong'))
        print(colors('Recomendo cálculo de conjunto de 2 e 3 números', 'light_yellow'))
        n = int(input('Tamanho do conjunto(1 a 6): '))
        matriz_conj_qtd = qtd_conj_sorteado(n, stt.sorteios)
        criar_planilha(matriz_conj_qtd, f'dados/freq_combinacoes_{n}.xlsx')

    elif op == '6':  # Mostrar gráfico de frequência de números
        print('Exibindo gráfico de frequência de sorteio de cada número')
        grafico(stt.frequencia_num)

    elif op == '7':  # Encerrar
        break

    else:
        print('Opção inválida!')
