from utils.utils_generic import colors


# noinspection PyTypeChecker
def menu(opcoes) -> None:
    print('=-=' * 20)
    print('MENU DE OPÇÕES'.center(60))
    print('=-=' * 20)
    for i, op in enumerate(opcoes, start=1):
        f_i = colors(i, 'light_blue')
        f_op = colors(op, 'light_green')
        print(f_i, ' - ', f_op)
    print('-' * 60)
