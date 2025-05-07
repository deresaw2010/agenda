# Lista que armazenará os contatos
agenda = []

def exibir_menu():
    print("\nAgenda de Contatos")
    print("1. Adicionar contato")
    print("2. Editar contato")
    print("3. Excluir contato")
    print("4. Listar contatos")
    print("5. Sair")

def adicionar_contato():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    
    contato = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    
    agenda.append(contato)
    print("Contato adicionado com sucesso!")

def listar_contatos():
    if not agenda:
        print("Agenda vazia.")
        return
    
    for i, contato in enumerate(agenda):
        print(f"\nContato {i+1}")
        print(f"Nome: {contato['nome']}")
        print(f"Endereço: {contato['endereco']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")

def editar_contato():
    listar_contatos()
    try:
        indice = int(input("\nDigite o número do contato que deseja editar: ")) - 1
        if 0 <= indice < len(agenda):
            print("Deixe em branco para manter o valor atual.")
            nome = input(f"Novo nome ({agenda[indice]['nome']}): ") or agenda[indice]['nome']
            endereco = input(f"Novo endereço ({agenda[indice]['endereco']}): ") or agenda[indice]['endereco']
            telefone = input(f"Novo telefone ({agenda[indice]['telefone']}): ") or agenda[indice]['telefone']
            email = input(f"Novo e-mail ({agenda[indice]['email']}): ") or agenda[indice]['email']

            agenda[indice].update({
                "nome": nome,
                "endereco": endereco,
                "telefone": telefone,
                "email": email
            })
            print("Contato atualizado com sucesso!")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def excluir_contato():
    listar_contatos()
    try:
        indice = int(input("\nDigite o número do contato que deseja excluir: ")) - 1
        if 0 <= indice < len(agenda):
            agenda.pop(indice)
            print("Contato excluído com sucesso!")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        editar_contato()
    elif opcao == "3":
        excluir_contato()
    elif opcao == "4":
        listar_contatos()
    elif opcao == "5":
        print("Saindo da agenda...")
        break
    else:
        print("Opção inválida. Tente novamente.")
