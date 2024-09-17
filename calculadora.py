# calculadora code
def calculadora():
    # o codigo de calculadora irá aqui
    print("Calculadora do Shell!")
    print("Opções:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    while True:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo agora: "))
            resultado = num1 + num2
            print(f"O resultado é: {resultado}")

        elif opcao == 2:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo agora: "))
            resultado = num1 - num2
            print(f"O resultado é: {resultado}")

        elif opcao == 3:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            resultado = num1 * num2
            print(f"O resultado é: {resultado}")

        elif opcao == 4:
            num1 = float(input("Digite o numero ai parça: "))
            num2 = float(input("Digite o segundo agora: "))
            if num2 == 0:
                print("Erro: não é possível dividir por zero!")
            else:
                resultado = num1 / num2
                print(f"O resultado é: {resultado}")

        elif opcao == 5:  # Adicionado opção de sair
            print("Saindo da calculadora...")
            break  # Interrompe o loop


        else:
            print("Erro: opção inválida!")


if __name__ == "__main__":
    calculadora()