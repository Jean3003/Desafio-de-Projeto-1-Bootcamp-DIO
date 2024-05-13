def menu():
    menu = """

    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc] \tNova Conta
    [nu] \tNovo Usuário
    [lc] \tListar Contas
    [q] \tSair

    => """
    return input(menu)


def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f'\nDepósito: R$ {valor_deposito:.2f}'
        print(f'Depósito no valor de {valor_deposito} realizado com sucesso!')
    else:
        print('\nValor digitado inválido!')
    return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    acima_saldo = valor_saque > saldo
    acima_limite = valor_saque > limite
    acima_saques = numero_saques >= limite_saques

    if acima_saldo:
        print('Operação inválida! Você digitou um valor de saque acima de seu saldo.')
    elif acima_limite:
        print('Operação inválida! Você não pode sacar acima de R$ 500')
    elif acima_saques:
        print('Operação inválida! O limite de saques é de 3 por dia.')
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f'\nSaque: R$ {valor_saque}'
        numero_saques += 1
        print('\nSaque realizado com sucesso!')
    else:
        print('Operação inválida! O valor informado é inválido!')
    return saldo, extrato, numero_saques
 

def exibir_extrato(saldo, /, *, extrato):
    print('\n=============== EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo}')
    print('='*40)


def criar_usuario(usuarios):
    cpf = input('Informe somente os números do CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nJá existe usuário cadastrado com esse CPF!')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/UF): ')
    usuarios.append({'nome': nome, 'data de nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado com sucesso!')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_contas(agencia, contas, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('\nConta criada com sucesso!')
        contas.append({'agencia': agencia, 'numero da conta': numero_conta, 'usuario': usuario})
    else:
        print('\nUsuário não encontrado!')


def listar_contas(contas):
    for conta in contas:
        linhas = f'''
            Agência: {conta['agencia']}
            C/C: {conta['numero da conta']}
            Titular: {conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(linhas)


def main():
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            print('\nDepósito')
            valor_deposito = float(input('Digite um valor => '))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
           
        elif opcao == 's':
            print('Saque')
            if saldo != 0:
                valor_saque = float(input('Digite o valor que deseja sacar => '))
                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor_saque=valor_saque,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )
            else:
                print('Você não possui valor na conta!')        

        elif opcao == 'e':
            print('Extrato')
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'q':
            break
        
        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_contas(AGENCIA, contas, numero_conta, usuarios)  
        
        elif opcao == 'lc':
            listar_contas(contas)

        else:
            print('Operação inválida, por favor salecione novamente a operação desejada.')


main()
