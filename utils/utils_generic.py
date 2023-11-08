def colors(texto: str, cor: str) -> str:
    """
    Formatação de string com cores

    Example:
        Imprimir um texto em letra vermelha e fundo preto:
            texto = 'Esse é um texto teste'
            print(f'{colors(texto, "red")}')

    Descrição das cores:
        - white: Letra branca, fundo preto
        - black: Letra preta, fundo branco
        - red: Letra vermelha, fundo preto
        - blue: Letra azul, fundo preto
        - yellow: Letra amarelo, fundo preto
        - green: Letra verde, fundo preto
        - strong: Letra preta, fundo vermelho
        - light_green: Letra verde
        - Light_blue: Letra azul

    :param texto: Texto a ser formatado
    :param cor: Cor para formatação

    :returns:
        str: Texto formatado com a cor especificada

    :raises ValueError: Se 'cor' não for uma opção válida
    """

    colors_dict = {
        'white': '\033[97;40m',
        'black': '\033[1;30;47m',
        'red': '\033[1;31;40m',
        'blue': '\033[1;34;40m',
        'yellow': '\033[1;33;40m',
        'green': '\033[1;32;40m',
        'strong': '\033[1;30;41m',
        'light_green': '\033[32m',
        'light_yellow': '\033[33m',
        'light_blue': '\033[34m',
        'end': '\033[m'
    }

    if cor not in colors_dict:
        raise ValueError(f"A cor '{cor}' não é uma opção válida. Escolha entre: {', '.join(colors_dict.keys())}")

    return f'{colors_dict[cor]} {texto} {colors_dict["end"]}'
