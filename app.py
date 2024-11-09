import streamlit as st
from datetime import datetime

# Função para processar o conteúdo da sessão colada no textarea
def processar_conteudo_txt(conteudo):
    membros = []
    total_loot = {}
    total_custos = {}
    total_balance = {}
    total_tibia_coins = {}
    session_info = {}
    
    for linha in conteudo.split("\n"):
        linha = linha.strip()
        
        if not linha:
            continue  # Pula linhas vazias

        # Extrai a data da sessão
        if linha.startswith("Session data:"):
            session_info['data'] = linha.split("From ")[1].split(",")[0]
            session_info['hora'] = linha.split(" ")[2]

        # Verifica se a linha representa o nome de um jogador
        if linha and linha[0].isalpha() and ":" not in linha:
            nome = linha.split('(')[0].strip()
            if nome not in membros:
                membros.append(nome)

        # Adiciona loot, supplies, balance e tibia coins aos membros
        if membros:
            if "Loot:" in linha and "Total" not in linha:
                loot = int(linha.split(':')[1].strip().replace(',', ''))
                total_loot[membros[-1]] = loot

            if "Supplies:" in linha:
                supplies = int(linha.split(':')[1].strip().replace(',', ''))
                total_custos[membros[-1]] = supplies

            if "Balance:" in linha:
                balance = int(linha.split(':')[1].strip().replace(',', ''))
                total_balance[membros[-1]] = balance

    return membros, total_loot, total_custos, total_balance, session_info

# Função para calcular a divisão do loot
def calcular_divisao_loot(membros, total_loot, total_custos, total_balance, total_tibia_coins, valor_tibia_coin):
    if len(membros) == 0:
        raise ValueError("A lista de membros está vazia. Verifique o conteúdo do texto.")

    # Calcula o saldo de cada membro
    saldos = {}
    for membro in membros:
        # Se o balance estiver disponível, usa o balance direto, senão calcula o saldo como loot - supplies
        saldos[membro] = total_balance.get(membro, total_loot.get(membro, 0) - total_custos.get(membro, 0))
        # Adiciona o custo dos tibia coins ao saldo
        saldos[membro] -= total_tibia_coins.get(membro, 0) * valor_tibia_coin
    
    # Calcula o lucro total da party e o lucro médio por membro
    saldo_total = sum(saldos.values())
    lucro_medio = saldo_total / len(membros)

    # Ajusta o saldo de cada membro para que todos tenham o lucro médio
    transferencias = {membro: saldo - lucro_medio for membro, saldo in saldos.items()}

    return transferencias, saldo_total, lucro_medio

# Interface do app
st.title("Divisão de Loot de Party Hunt - Tibia")

# Adicionar uma imagem no header
st.image("header.png",use_container_width=True)

st.subheader("Cole o conteúdo da sessão no campo abaixo")

# Campo de texto para colar o conteúdo da sessão
conteudo = st.text_area("Cole o conteúdo da sessão de Party Hunt aqui", height=300)

# Inserir valor em gold dos Tibia Coins
valor_tibia_coin = st.number_input("Valor em gold de cada Tibia Coin", min_value=0)

# Campo para inserir quantos Tibia Coins cada membro gastou
tibia_coins_gastos = {}
if conteudo:
    membros, _, _, _, _ = processar_conteudo_txt(conteudo)
    for membro in membros:
        tibia_coins_gastos[membro] = st.number_input(f"Tibia Coins gastos por {membro}", min_value=0, key=membro)

# Calcular resultado ao clicar em um botão
if st.button("Calcular divisão"):
    if conteudo:
        try:
            # Processa o conteúdo colado e extrai os dados
            membros, total_loot, total_custos, total_balance, session_info = processar_conteudo_txt(conteudo)

            if membros:
                # Calcula as transferências
                resultado, saldo_total, lucro_medio = calcular_divisao_loot(membros, total_loot, total_custos, total_balance, tibia_coins_gastos, valor_tibia_coin)

                # Formata a data da sessão
                data_sessao = datetime.strptime(session_info['data'], '%Y-%m-%d').strftime('%b %d, %Y')
                hora_sessao = session_info['hora']
                dia_semana = datetime.strptime(session_info['data'], '%Y-%m-%d').strftime('%A')

                # Mostra os resultados no formato esperado
                st.subheader("📅 Sessão do time:")
                st.write(f"{data_sessao} - {hora_sessao} ({dia_semana})")
                
                st.subheader("👥 Membros do time:")
                for membro in membros:
                    st.write(f"- {membro}")
                
                st.subheader("🔄 Bank transfers:")
                pagamentos = sorted([(membro, valor) for membro, valor in resultado.items() if valor > 0], key=lambda x: x[1], reverse=True)
                recebimentos = sorted([(membro, -valor) for membro, valor in resultado.items() if valor < 0], key=lambda x: x[1], reverse=True)

                # Verifica se há transferências para serem feitas
                if not pagamentos or not recebimentos:
                    st.write("Nenhuma transferência necessária. Todos os saldos já estão equilibrados.")
                else:
                    # Exibir transferências detalhadas, priorizando o maior saldo positivo
                    while pagamentos and recebimentos:
                        recebedor, valor_receber = recebimentos.pop(0)
                        pagador, valor_pagar = pagamentos.pop(0)

                        transferencia = min(valor_pagar, valor_receber)
                        st.write(f"- {pagador} transfer {int(transferencia)} to {recebedor}")
                        
                        

                        valor_pagar -= transferencia
                        valor_receber -= transferencia

                        if valor_pagar > 0:
                            pagamentos.insert(0, (pagador, valor_pagar))
                        if valor_receber > 0:
                            recebimentos.insert(0, (recebedor, valor_receber))

                st.subheader("💰 Profit total:")
                st.write(f"{int(saldo_total):.}gp ({int(lucro_medio):.} gp cada)")
            else:
                st.error("Nenhum membro foi encontrado. Verifique o formato do conteúdo.")
        except Exception as e:
            st.error(f"Erro ao processar o conteúdo: {e}")
    else:
        st.error("Por favor, cole o conteúdo da sessão para realizar a análise.")

# Footer
st.markdown("---")
st.markdown("Autor: João Augusto")
st.markdown("Meu GitHub: [https://github.com/ArkaNiightt](https://github.com/ArkaNiightt)")
st.markdown("Contato: [https://www.linkedin.com/in/joaoaugustopina/](https://www.linkedin.com/in/joaoaugustopina/)")
