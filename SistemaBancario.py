class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito deve ser positivo.')

    def saque(self, valor):
        if valor > 0:
            if valor <= 500 and len(self.saques) < 3:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saques.append(valor)
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print('Limite diário de saque excedido ou valor de saque inválido.')
        else:
            print('Valor de saque deve ser positivo.')

    def extrato(self):
        print('=== Extrato ===')
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')


# Função para interação com o usuário
def main():
    sistema = SistemaBancario()

    while True:
        print('\nEscolha uma operação:')
        print('1 - Depósito')
        print('2 - Saque')
        print('3 - Extrato')
        print('0 - Sair')

        escolha = input('Opção: ')

        if escolha == '1':
            valor = float(input('Digite o valor do depósito: '))
            sistema.deposito(valor)
        elif escolha == '2':
            valor = float(input('Digite o valor do saque: '))
            sistema.saque(valor)
        elif escolha == '3':
            sistema.extrato()
        elif escolha == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == "__main__":
    main()
