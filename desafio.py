def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair

    => """

    return input(menu)

def deposito(saldo, valor, extrato, /):
    if(valor > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        

    elif(valor < 0):
         print("Operação falhou! Não é possível depositar um valor negativo, por favor digite novamente!")

    return saldo, extrato

def saque(*, saldo, valor, limite, extrato, numero_saques, LIMITE_SAQUES):
           
    if(valor > saldo):
        print("Operação falhou! Você não tem saldo suficiente.")
            
    elif(valor > limite):
       print(f"Operação falhou! O valor do saque não exceder R$ {limite:.2f}!")             

    elif(numero_saques >= LIMITE_SAQUES):
        print("Operação falhou! Número máximo de saques excedido.")

    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        print(f"Saques diários realizados: {numero_saques}")
        
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    descricao = " EXTRATO "
    descricao = print(descricao.center(22, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: {saldo:.2f}")
    print("======================")

def criar_usuario(clientes):
    while True:
        try:
            cpf = int(input("Digite seu CPF (Apenas números): "))
            break
        except ValueError:
            print("Operação falhou! O valor informado é inválido, por favor informe seu CPF novamente.")
            continue

    cliente = verificar_usuario(cpf, clientes)

    if cliente:
        print("Já existe usuário com este CPF!")
        return
    
    nome = input("Nome Completo: ")
    data_nascimento = input("Data de Nascimento(dd/mm/aaaa): ")
    endereco = input("Endereço(lograoduro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome" : nome,
                    "data_nascimento": data_nascimento,
                    "cpf": cpf,
                    "endereco": endereco})
    
    print("=== Cadastro do cliente realizado com sucesso! ===")
    return clientes

def verificar_usuario(cpf, clientes):
    usuarios_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(clientes, numero_conta, contas, AGENCIA):
    while True:
        try:
            cpf = int(input("Digite seu CPF (Apenas números): "))
            break
        except ValueError:
            print("Operação falhou! O valor informado é inválido, por favor informe seu CPF novamente.")
            continue

    cliente = verificar_usuario(cpf, clientes)

    if not cliente:
        print("Não existe usuário com este CPF!")
        return
    
    contas.append({"agencia":AGENCIA,
                   "conta":numero_conta,
                   "usuario":cliente})
    
    print("=== Cadastro da conta realizado com sucesso! ===")

def listar_conta(contas):
    descricao = " CONTAS "
    descricao = print(descricao.center(22, "="))

    for conta in contas:
        print(f"Agência: ", conta["agencia"])
        print("C/C: ", conta["conta"])
        print("Titular: ", conta["usuario"]["nome"])

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "d":
            print("Depósito")

            while True:

                try:
                    valor = float(input("Digite o valor do depósito: "))
                    break

                except ValueError:
                     print("Operação falhou! O valor informado é inválido, por favor informe um valor numérico.")
                     continue 
            saldo, extrato =  deposito(saldo, valor, extrato)                      

        elif opcao == "s":
            print("Saque")

            while True:
                try:
                    valor = float(input("Digite o valor do saque: "))
                    break

                except ValueError:
                    print("Operação falhou! O valor informado é inválido, por favor informe um valor numérico.")
                    continue

            saldo, extrato = saque(saldo=saldo,
            valor=valor, 
            limite=limite,
            extrato=extrato,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            extrato = exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            print("Cadastro novo usuário")
            criar_usuario(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            print("Cadastro nova conta")
            criar_conta(clientes, numero_conta, contas, AGENCIA)

        elif opcao == "lc":
            listar_conta(contas)    

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()