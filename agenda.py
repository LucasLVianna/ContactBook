def adicionar_contato(contatos, nome_contato, numero_contato, email_contato):
    contato = {"contato" : nome_contato, "numero" : numero_contato, "email" : email_contato, 'favorito' : False}
    contatos.append(contato)
    print(f"Contato de {nome_contato} adicionado com sucesso")
    return

def lista_contatos_salvos(contatos):
    print("\nLista dos contatos salvos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "☆" if contato ['favorito'] else " "
        nome_contato = contato["contato"]
        numero_contato = contato["numero"]
        email_contato = contato["email"]
        print(f"""{indice}. {status} {nome_contato}: número - {numero_contato} / email - {email_contato}""")
    return

def editar_contato(contatos, indice_contato, novo_nome, novo_numero, novo_email):
    indice_arrumado = int(indice_contato) - 1
    if indice_arrumado >= 0 and indice_arrumado<len(contatos):
        contatos[indice_arrumado]["contato"] = novo_nome
        contatos[indice_arrumado]["numero"] = novo_numero
        contatos[indice_arrumado]["email"] = novo_email
        print(f"Contato {indice_contato} atualizado para {novo_nome}")
    else:
        print("Índice de contato não existente")
    return 

def favoritar_contato(contatos, indice_contato):
    indice_arrumado = int(indice_contato) - 1
    contatos[indice_arrumado]['favorito'] = True
    print(f"Contato {indice_contato} salvo como favorito")
    return

def desfavoritar_contato(contatos, indice_contato):
    indice_arrumado = int(indice_contato) - 1
    if indice_arrumado >= 0 and indice_arrumado < len(contatos):
        if contatos[indice_arrumado]['favorito']:
            contatos[indice_arrumado]['favorito'] = False
            print(f"Contato {indice_contato} removido de favorito")
        else:
            print("Este contato não é favorito! Tente novamente")
            return False
    else:
        print("Índice inválido!")
    return

def lista_favoritos(contatos):
    contatos_favoritos = []
    for contato in contatos:
        if contato['favorito']:
            contatos_favoritos.append(contato)
    if contatos_favoritos:
        print("\n☆ Lista de contatos favoritos ☆: ")
        for indice, contato in enumerate(contatos_favoritos, start=1):
            nome_contato = contato["contato"]
            numero_contato = contato["numero"]
            email_contato = contato["email"]
            print(f"""{indice}. {nome_contato}: número - {numero_contato} / email - {email_contato}""")
    else:
        print("Nenhum contato favorito!")
    return

def remover_contato(contatos, indice_contato):
    indice_arrumado = int(indice_contato) - 1
    if indice_arrumado >= 0 and indice_arrumado < len(contatos):
        del contatos[indice_arrumado]
        print(f"Contato de índice {indice_contato} foi apagado!")
    else:
        print("Índice de contato inválido!")
    return

contatos = []
while True:
    print("\nMenu da Agenda de Contatos")
    print("1. Adicionar contato")
    print("2. Lista de contatos salvos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Lista de contatos favoritos")
    print("7. Deletar contato")
    print("8. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_contato = input("Nome do contato a ser adicionado: ")
        numero_contato = input("Telefone do contato: ")
        email_contato = input("Email do contato: ")
        adicionar_contato(contatos, nome_contato, numero_contato, email_contato)
    elif escolha == "2":
        lista_contatos_salvos(contatos)
    elif escolha == "3":
        lista_contatos_salvos(contatos)
        indice_contato = input("Índice do contato que deseja atualizar: ")
        novo_nome = input("Novo nome que deseja utilizar: ")
        novo_numero = input("Novo número que deseja utilizar: ")
        novo_email = input("Novo email que deseja utilizar: ")
        editar_contato(contatos, indice_contato, novo_nome, novo_numero, novo_email)
    elif escolha == "4":
        lista_contatos_salvos(contatos)
        indice_contato = input("Digite o índice do contato que quer favoritar: ")
        favoritar_contato(contatos, indice_contato)
    elif escolha == "5":
        lista_contatos_salvos(contatos)
        indice_contato = input("Digite o índice do contato que quer desfavoritar: ")
        desfavoritar_contato(contatos, indice_contato)
    elif escolha == "6":
        lista_favoritos(contatos)
    elif escolha == "7":
        lista_contatos_salvos(contatos)
        indice_contato = input("Digite o índice do contato que deseja remover: ")
        remover_contato(contatos, indice_contato)
    elif escolha == "8":
        break

print("Saindo...")