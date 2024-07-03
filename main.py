menu = '''


    Selecione a opção desejada:

    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Sair

    

'''

saldo = 0.00
limite_por_saque = 500.00
extrato = f'''

'''
quantidade_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("-> Depósito\n")
        deposito = float(input("Digite o valor desejado para depósito: "))

        if deposito <= 0.00:
            print("Valor inválido, por favor, tente novamente")
        elif deposito > 0.00:
            print(f"Valor a ser depositado: {deposito:.2f}")
            saldo += deposito
            extrato += f"Depósito de: R${deposito:.2f}\n\n"
            print(f"Depósito de {deposito:.2f} reais concluído com sucesso!")


    elif opcao == "2":
        print("-> Saque\n")

        if quantidade_saques > limite_saques:
            print("Limite de saques diários atingido.")
        
        saque = float(input("Digite o valor desejado para saque: "))

        if saque > 500.00:
            print("Saques são limitados a R$500, por favor, tente novamente.")
        elif saque <= 0.00:
            print("Valor inválido, por favor, tente novamente")
        elif saque > saldo:
            print("Saldo insuficiente, por favor, tente novamente")
        elif saque <= saldo:
            print(f"Realizando saque de R${saque:.2f}, por favor, aguarde...")
            saldo -= saque
            extrato += f"Saque de: R${saque:.2f}\n\n"
            quantidade_saques += 1
            print(f"Saque de R${saque:.2f} realizado com sucesso!")


    elif opcao == "3":
        print(f"-> Extrato: {extrato}\nSaldo: R${saldo:.2f}")
    
    elif opcao == "0":
        print("Sessão encerrada.")
        break

    else:
        print("Opção inválida, digite sua opção novamente:")