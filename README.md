# Análise Estatística de Resultados de Sorteios da Mega-Sena

## Descrição

Este projeto é uma aplicação Python que oferece uma série de funcionalidades para a análise estatística de resultados de sorteios. Ele permite que os usuários extraiam dados de sorteios a partir de uma planilha Excel e realizem várias análises estatísticas, incluindo o cálculo da frequência de números sorteados, a identificação do número mais e menos sorteado, a verificação de palpites em jogos anteriores e a geração de planilhas de frequência de conjuntos de números.

## Funcionalidades

O projeto é composto por diversos módulos e classes que oferecem as seguintes funcionalidades:

1. **Extração de Dados de Sorteios**: O módulo `modulos/extracao_sorteios.py` extrai os dados de sorteios de uma planilha Excel e converte esses dados em objetos da classe `Sorteio`.

2. **Análise Estatística de Números Sorteados**: O arquivo `classes/estatistica.py` define a classe `Estatistica`, que realiza cálculos estatísticos, como a frequência de números sorteados, o número mais sorteado e o número menos sorteado.

3. **Cálculo de Frequência de Conjuntos de Números**: O módulo `funcoes/freq_combinacoes.py` permite calcular a frequência de combinações de números sorteados em concursos anteriores, de acordo com o tamanho do conjunto especificado.

4. **Geração de Gráficos de Frequência**: A função em `funcoes/graficos.py` oferece a capacidade de gerar gráficos que representam a frequência de números sorteados.

5. **Interface de Usuário**: As funções em `funcoes/interface.py` fornece uma interface para menu, aceitando dinâmicamente várias opções.

## Uso

Para utilizar este projeto, siga as instruções abaixo:

1. Certifique-se de que você tem uma planilha Excel contendo os dados dos sorteios em `dados/dados_sorteios.xlsx`.

2. Execute o arquivo `main.py`.

3. Use o menu interativo apresentado para escolher entre as opções disponíveis e realizar análises estatísticas dos resultados dos sorteios.

É possível ajustar os parâmetros, como a data inicial, o tamanho dos conjuntos e outros, de acordo com suas necessidades e preferências.

## Pré-requisitos

Para executar o projeto, você precisará ter o Python 3 instalado e as seguintes bibliotecas:

- `pandas`: Para a leitura da planilha de dados e manipulação de dados.
- `openpyxl`: Para a escrita de planilhas Excel.
- `matplotlib` e`mplcursors`: Exibição gráfica da análise.

Certifique-se de que todas as bibliotecas necessárias estão instaladas no ambiente Python.

## Estrutura da planilha

- Colunas: concurso, data, bola1, bola2, bola3, bola4, bola5 e bola6.
- Site para extrair dados atualizados: https://loteriadacaixa.net.br/mega-sena/todos-os-resultados-da-mega-sena/29275

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para criar novas funcionalidades, melhorar as existentes ou corrigir possíveis problemas. As contribuições são bem-vindas.

## Autores

Este projeto foi desenvolvido por Cleiner Ediel Furlani Garcia.

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
