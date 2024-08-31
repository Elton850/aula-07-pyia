lista_Produtos = []

while True:
    menu_principal = str(input("""
    1 - Estoque
    2 - Vendas
    0 - Sair do programa
"""))
    
    match menu_principal:
        case "1":
            while True:
                menu_estoque = str(input("""
                1 - Cadastrar Novo Produto
                2 - Ver Produtos
                3 - Editar Produto
                4 - Excluir Produto
                0 - Voltar
                """))
                match menu_estoque:
                    case "1":
                        while True:
                                while True:
                                    nome_produto = str(input("Digite o nome do produto: "))
                                    if nome_produto != "":
                                        break
                                    else:
                                        print("Digite um nome para o novo produto")

                                while True:
                                    try:
                                        qdt_estoque = int(input("Digite a quantidade em estoque: "))
                                        if qdt_estoque < 0:
                                            print("Digite uma quantidade maior que ou igual a 0")
                                        else:
                                            break
                                    except:
                                        print("Digite apenas números")

                                while True:
                                    try:
                                        preco = str(input("Digite o preço unitário: "))

                                        preco_formatado = float(preco.replace(",","."))

                                        if preco_formatado < 0:
                                            print("Digite um valor mair que ou igual a 0")
                                        else:
                                            break
                                    except:
                                        print("Digite apenas números separador por vírgula (,)")
                                
                                if len(lista_Produtos) == 0:
                                    id_da_vez = 1
                                else:
                                    id_da_vez = max(produto_da_vez['id'] for produto_da_vez in lista_Produtos) + 1
                                        
                                novo_produto = {
                                    "id" : str(id_da_vez),
                                    "nome_produto" : str(nome_produto),
                                    "qdt_estoque" : str(qdt_estoque),
                                    "preco" : str(preco)
                                }
                                lista_Produtos.append(novo_produto)
                                print("Cadastro realizado com sucesso!")
                                break
                    case "2":
                        if len(lista_Produtos) > 0:
                            print("Produtos em Estoque")
                            for produto in lista_Produtos:
                                print(produto)
                        else:
                            print("Não existem produtos cadastrados")
                    case "3":
                        if len(lista_Produtos) > 0:
                            print("Edição de produtos")
                            for produto in lista_Produtos:
                                print(produto)
                            while True:
                                id_escolhido = str(input("Digite o ID do Produto a ser editado: "))
                                for produto in lista_Produtos:
                                    if id_escolhido == produto['id']:
                                        while True:
                                            menu_editar = str(input("""
                                            1 - Editar Nome
                                            2 - Editar Quantidade
                                            3 - Editar Preco
                                            """))
                                            match menu_editar:
                                                case "1":
                                                    novo_nome = str(input("Digite o novo nome do produto: "))
                                                    if novo_nome != "":
                                                        produto['nome_produto'] = novo_nome
                                                        print("Nome alterado")
                                                    else:
                                                        print("Digite um nome para o produto")
                                                case "2":
                                                    while True:
                                                        try:
                                                            nova_qdt = int(input("Digite a nova quantidade: "))
                                                            if nova_qdt > 0:
                                                                produto['qdt_estoque'] = nova_qdt
                                                                print("Quantidade alterada!")
                                                            else:
                                                                print("Digite uma quantidade maior que ou igual a 0")
                                                        except:
                                                            print("Digite um número inteiro positivo")
                                                case _:
                                                    print("Opção Inválida!")
                                    else:
                                        print("O id escolhido não existe, escolha o id de um produto do estoque")
                        else:
                            print("Não existem produtos cadastrados")
                    case "0":
                        break
                    case _:
                        print("Opção Inválida!")
        case "2":
            print("Teste")
        case "0":
            print("Programa Encerrado!")
            break
        case _:
            print("Opção Inválida!")