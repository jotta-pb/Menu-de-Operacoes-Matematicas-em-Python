print("--- Menu ---\n")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
print("")

#---------- MENU ----------
a = 1
soma = None
mult = None

while a == 1:
    result_potencia = 0
    print("--- MENU DE OPÇÕES ---")
    print("[1] - Somar")
    print("[2] - Multiplicar")
    print("[3] - Maior")
    print("[4] - Novos números")
    print("[5] - Potência")
    print("[6] - Sair do programa")
    print()
    opcao = int(input("O que deseja executar ?\n"))
    
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma dos números é {soma}.\n")
        continue
        
    elif opcao == 2:
        mult = n1 * n2
        print(f"A produto dos números é {mult}.\n")
        continue
            
    elif opcao == 3:
        if n1 == n2:
            print(f"{n1} e {n2} são iguais.\n")
            continue
                
        else:
            if n1 > n2:
                print(f"O maior número é {n1}.\n")
                continue
                
            else:
                print(f"O maior número é {n2}.\n")
                continue
                
    elif opcao == 4:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        soma = None
        mult = None
        continue

    elif opcao == 5:
        expoente = int(input("Digite o valor do expoente: "))
        n1_pot = n1 ** expoente
        n2_pot = n2 ** expoente
        print(f"Os números {n1} e {n2} elevados ao expoente de valor {expoente} possuem o valor de {n1_pot} e {n2_pot}.\n")
        continue
            
        
    elif opcao > 6:
        print("Opção inválida! Escolha somente as opções de 1 à 5!")
        continue

    elif opcao == 6:
        print("Fim do programa.")
        break