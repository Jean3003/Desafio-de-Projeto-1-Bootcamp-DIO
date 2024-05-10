menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('\nDepósito')
        deposito = float(input('Digite um valor => '))

        if deposito > 0:
            saldo += deposito
            extrato += f'\nDepósito: R$ {deposito:.2f}'
            print(f'Depósito no valor de {deposito} realizado com sucesso!')
        else:
            print('\nValor digitado inválido!')

    elif opcao == 's':
        print('Saque')
        if saldo != 0:
            valor_saque = float(input('Digite o valor que deseja sacar => '))
            acima_saldo = valor_saque > saldo
            acima_limite = valor_saque > limite
            acima_saques = numero_saques >= LIMITE_SAQUES
            
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
            else:
                print('Operação inválida! O valor informado é inválido!')
        else:
            print('Você não possui valor na conta!')

    elif opcao == 'e':
        print('Extrato')
        print('\n=============== EXTRATO ================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo}')
        print('='*40)
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor salacione novamente a operação desejada.')
