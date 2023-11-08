import matplotlib.pyplot as plt
import mplcursors


def grafico(freq_num: dict) -> None:
    """
    Gera gráfico de frequência dos números
    :param freq_num:  dicionário de frequência dos números
    :return: None
    """

    keys = list(freq_num.keys())
    values = list(freq_num.values())

    # Definir tamanho e cor das bolinhas
    marker_size = 70  # Tamanho dos marcadores
    marker_color = '#008000'  # Cor dos marcadores (laranja)

    plt.scatter(keys, values, s=marker_size, c=marker_color, alpha=0.7)

    plt.xlabel('keys')
    plt.ylabel('values')
    plt.title('FREQUÊNCIA DE SORTEIO DE CADA NÚMERO')
    plt.grid(True)

    # Definir o intervalo do eixo y para reduzir a escala
    plt.ylim(min(values), max(values))  # Você pode ajustar o valor máximo conforme necessário

    # Função para formatar a caixa de texto do tooltip
    def format_tooltip(sel):
        sel.annotation.set_text(f'Chave: {keys[sel.index]}\nValor: {values[sel.index]}')
        sel.annotation.get_bbox_patch().set(fc="white", ec="black", lw=1, boxstyle="round,pad=0.4")

    # Adicionar tooltips interativos com as chaves e valores
    mplcursors.cursor(hover=True).connect("add", format_tooltip)

    plt.show()
