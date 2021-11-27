contas = []
depositos = []
saldo = 0


def main():
    opcao = bool(int(input("Olá, Deseja ver ou criar uma conta opcao (1) ou opcao(0): ")))
    while opcao:
        criarConta()
        verSaldo()
        opcao = bool(int(input("Olá, Deseja ver ou criar uma conta opcao (1) ou opcao(0): ")))

def criarConta():
        global contas, depositos, saldo
        num_conta = int(input("Digite o numero da conta : " ))

        while num_conta in contas:
            print("Conta já existente, Digite novamente.")
            num_conta = int(input("Digite o numero da conta : "))
            
        contas.append(num_conta)
        deposito = float(input("Digite o valor do primeiro deposito"))
        
        while deposito <=0:
            print("Valor do deposito invalido")
            deposito = float(input("Digite o valor do deposito que deseja realizar:"))
        depositos.append(deposito)
        saldo += deposito

def verSaldo():
    global saldo
    opcao = bool(int(input ("Deseja ver o saldo do banco agora sim (1) ou não(0)")))
    if opcao:
        print("O saldo do banco é R$", saldo)
        
main()
    
            
