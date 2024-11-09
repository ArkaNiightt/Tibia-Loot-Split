# Divisão de Loot de Party Hunt - Tibia

Este é um aplicativo desenvolvido em Python utilizando Streamlit para ajudar a dividir o loot e os custos de uma caçada em grupo no jogo Tibia. O objetivo é tornar a distribuição dos lucros mais justa, considerando também os custos adicionais, como o uso de Tibia Coins.

## Funcionalidades
- Processamento de dados da sessão de caçada (loot, custos, saldo de cada membro).
- Cálculo do lucro total e do lucro médio para cada membro da party.
- Distribuição dos custos com base no saldo final, mostrando quem deve transferir para quem.
- Opção para inserir quantos Tibia Coins cada jogador gastou, além do valor atual de cada Tibia Coin.
- Interface gráfica com um campo para colar o conteúdo da sessão e inputs para valores adicionais.
- Exibição dos resultados de forma clara e detalhada.

## Como Utilizar
1. **Faça o download do código** deste repositório.
2. **Instale as dependências necessárias** utilizando o comando:
   ```sh
   pip install streamlit
   ```
3. **Execute a aplicação** utilizando o comando:
   ```sh
   streamlit run app.py
   ```
4. **Preencha os campos necessários**:
   - Cole o conteúdo da sessão de caçada de Tibia no campo de texto.
   - Informe o valor atual de cada Tibia Coin.
   - Informe quantas Tibia Coins cada membro da party gastou.
5. **Clique no botão "Calcular divisão"** para visualizar os resultados detalhados da divisão do loot.

## Campos e Entradas
- **Conteúdo da Sessão**: Cole o conteúdo do log de caçada do Tibia.
- **Valor dos Tibia Coins**: Informe o valor atual em gold de cada Tibia Coin.
- **Tibia Coins Gastos por Membro**: Informe quantos Tibia Coins cada membro gastou durante a caçada.

## Resultados
- **Sessão do Time**: Informações sobre a data e a duração da sessão.
- **Membros do Time**: Lista dos membros que participaram da caçada.
- **Transferências Bancárias**: Mostra quem deve transferir gold para quem, para equilibrar os lucros e custos da party.
- **Profit Total**: Exibe o lucro total do grupo e o valor médio por membro.

## Imagem no Header
Você pode personalizar a aplicação adicionando uma imagem própria no cabeçalho, simplesmente substituindo o arquivo `header_image.png` pelo seu próprio.

## Requisitos
- Python 3.x
- Streamlit

## Rodapé
Esta aplicação foi desenvolvida por João Augusto.
- GitHub: [https://github.com/ArkaNiightt](https://github.com/ArkaNiightt)
- LinkedIn: [https://www.linkedin.com/in/joaoaugustopina/](https://www.linkedin.com/in/joaoaugustopina/)

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request se desejar melhorar o projeto.

