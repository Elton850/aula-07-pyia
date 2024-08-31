idades = []
media = 0

while True:
    opcao = str(input("""
1 - Adicionar idade
0 - Finalizar
"""))
    match opcao:
        case "1":
            while True:
                try:
                    nova_idade = int(input("Digite uma idade: "))
                    if nova_idade >= 0:
                        idades.append(nova_idade)
                        print("Idade cadastrada com sucesso")
                        break
                    else:
                        print("Idade inválida, digite um número positivo")
                except:
                    print("Digite um número inteiro para a idade")
        case "0":
            if len(idades) > 0:
                print(f"Maior idade: {max(idades)}")
                print(f"Menor idade: {min(idades)}")
                if len(idades) >= 2:
                    for idade in idades:
                        media += idade
                    print(f"Media idades: {(media / len(idades)):.1f}")
                else:
                    print("Sem média para calcular (é necessário ao menos duas idades cadastradas.)")
            else:
                print("Sem idades cadastradas")
            break
        case _:
            print("Opção inválida!")