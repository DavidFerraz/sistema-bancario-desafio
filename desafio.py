menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        while True:

            try:
                valor_deposito = float(input("Digite o valor do depósito:"))

            except ValueError:
                 print("Operação falhou! O valor informado é inválido, por favor informe um valor numérico.")
                 continue 

            if(valor_deposito > 0):
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                break

            elif(valor_deposito < 0):
                print("Operação falhou! Não é possível depositar um valor negativo, por favor digite novamente!")                               

    elif opcao == "s":
        print("Saque")

        while True:

            try:
                valor_saque = float(input("Digite o valor do saque:"))

            except ValueError:
                print("Operação falhou! O valor informado é inválido, por favor informe um valor numérico.")
                continue
                
            if(valor_saque > saldo):
                print("Operação falhou! Você não tem saldo suficiente.")
                break
            
            elif(valor_saque > limite):
                print(f"Operação falhou! O valor do saque não exceder R$ {limite:.2f}!")             

            elif(numero_saques >= LIMITE_SAQUES):
                print("Operação falhou! Número máximo de saques excedido.")
                break

            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                print(f"Saques diários realizados: {numero_saques}")
                break

    elif opcao == "e":
        descricao = " EXTRATO "
        descricao = print(descricao.center(22, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("======================")
        
            
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")