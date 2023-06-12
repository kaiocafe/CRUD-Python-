import csv
import os

csv_filename = 'Data/itens.csv'
import time

# limpar a tela 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Exibe o menu do programa
def show_menu():
    
    clear_screen()

    #   Linha de codificação para a quantidade total de dados
    itens = []
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            itens.append(row)
    row_count = sum(1 for row in itens)

    print("============ Menu =============")
    print("* TOTAL DE ITENS NO ESTOQUE: ",row_count)  
    print("===============================")
    print("[1] VER LISTA DE ITENS")
    print("[2] ADICIONAR ITENS")
    print("[3] EDITAR ITENS")
    print("[4] EXCLUIR ITENS")
    print("[5] ENCONTRAR ITENS")
    print("[0] SAIR \n")
    print("===============================")
    selected_menu = input("SELECIONE O MENU: ")
    
    # Determinar opções de menu
    if(selected_menu == "1"):
        show_itens()
    elif(selected_menu == "2"):
        add_itens()
    elif(selected_menu == "3"):
        edit_itens()
    elif(selected_menu == "4"):
        delete_itens()
    elif(selected_menu == "5"):
        search_itens()
    elif(selected_menu == "0"):
        exit()
    else:
        print("OPÇÃO INVALIDA")
        back_to_menu()

# Função para retornar ao menu
def back_to_menu():
    print("\n")
    input("DIGITE ENTER PARA RETORNAR AO MENU")
    show_menu()


# Função para retornar ao add_itens ou menu
def back_to_add():
    print("\n")
    a = input("DIGITE [1] PARA RETORNAR AO MENU OU [2] PARA CADASTRAR NOVAMENTE ")
    if a == "2":
        add_itens()
    elif a == "1":
        show_menu()
    else:
        clear_screen()
        print("Opção invalida, tente novamente.")
        back_to_add()

# Função para mostrar os itens
def show_itens():
    clear_screen()
    itens = []

# Abra o arquivo CSV com o modo R/Read (leitura)
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            itens.append(row)

    row_count = sum(1 for row in itens)

    print("-" * 55)
    print("\t\tITENS NO ESTOQUE")
    print("-" * 55)

    print("Codigo\tNome\t\tPreço\t\tQuantidade")
    print("-" * 55)

    # Looping para saída dos dados
    for data in itens:
        print(f"{data['Codigo']}\t{data['Nome']}\t\t{data['Preço']}\t\t{data['Quantidade']}")
  
        
    print("-" * 55)
    print("Total de Itens: ",row_count)
    print("-" * 55)
    
    back_to_menu()


def verificar_codigo_existente(codigo, arquivo):
    with open(arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            if linha[0] == codigo:
                return True
    return False

def add_itens():
    clear_screen()
    csv_filename = 'Data/itens.csv'
    with open(csv_filename, mode='a', newline='') as csv_file:
        fieldnames = ['Codigo', 'Nome', 'Preço', 'Quantidade']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("===============================")
        print("======= Cadastrar itens =======")
        print("===============================\n")

        codigo = input("Código: ")
        if verificar_codigo_existente(codigo, csv_filename):
            print("O código digitado já existe.")
            back_to_add()
        else:
            nome = input("Nome: ")
            preco = input("Preço: ")
            quantidade = input("Quantidade: ")

            writer.writerow({'Codigo': codigo, 'Nome': nome, 'Preço': preco, 'Quantidade': quantidade})

    back_to_menu()



def search_itens():
    clear_screen()
    itens = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            itens.append(row)

    Codigo = input("Digite o Codigo do produto: ")

    data_found = []

    # Procurar os itens
    indice = 0
    for data in itens:
        if (data['Codigo'] == Codigo):
            data_found = itens[indice]
            
        indice = indice + 1

    if len(data_found) > 0:
        print("Iten encontrado =>", f"{data_found['Nome']}")
       # print(f"Nome: {data_found['Nome']}")
        print(f"Preço: R$ {data_found['Preço']}")
        print(f"Quantidade: {data_found['Quantidade']}")
    else:
        print("Nenhum iten encontrado")
    back_to_menu()
    


def edit_itens():
    clear_screen()
    itens = []

    with open(csv_filename, mode="r",newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            itens.append(row)
    row_count = sum(1 for row in itens)

    print("-" * 55)
    print("\t\tEditar Itens")
    print("-" * 55)

    print("Codigo\tNome\t\tPreço\t\tQuantidade")
    print("-" * 55)

    for data in itens:
        print(f"{data['Codigo']}\t{data['Nome']}\t\t{data['Preço']}\t\t{data['Quantidade']}")

    print("-" * 55)
    print("Total de itens :",row_count)
    print("-" * 55)
    Codigo = input("Selecione o Codigo do iten: ")
    Nome = input("Novo nome: ")
    Preço = input("Novo preço: ")
    Quantidade = input("Nova quantidade: ")

    # Procure os itens e altere os dados com novos dados
    indice = 0
    for data in itens:    
        if (data['Codigo'] == Codigo):
            itens[indice]['Nome'] = Nome
            itens[indice]['Preço'] = Preço
            itens[indice]['Quantidade'] = Quantidade
        indice = indice + 1
        

    # Gravar novos dados no arquivo CSV (reescrever)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Codigo', 'Nome', 'Preço','Quantidade']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in itens:
            writer.writerow({'Codigo': new_data['Codigo'], 'Nome': new_data['Nome'], 'Preço': new_data['Preço'], 'Quantidade': new_data['Quantidade']}) 

    back_to_menu()



def delete_itens():
    clear_screen()
    itens = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            itens.append(row)

    print("Codigo\tNome\t\tPreço\t\tQuantidade")
    print("-" * 55)

    for data in itens:
        print(f"{data['Codigo']}\t{data['Nome']}\t\t{data['Preço']}\t\t{data['Quantidade']}")

    print("-" * 55)
    Codigo = input("Excluir o iten de codigo: ")

    indice = 0
    for data in itens:
        if (data['Codigo'] == Codigo):
            itens.remove(itens[indice])
        indice = indice + 1

    # Gravar novos dados no arquivo CSV (deletar)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Codigo', 'Nome', 'Preço', 'Quantidade']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in itens:
            writer.writerow({'Codigo': new_data['Codigo'], 'Nome': new_data['Nome'], 'Preço': new_data['Preço'], 'Quantidade': new_data['Quantidade']}) 

    print(f"O Iten foi excluído com secesso!")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()
