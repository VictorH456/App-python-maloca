import os

array_remedio = []
verifica = True

def menu():        
    print("""
╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━━╯╱╱╱╱╱╱╱╱╱╱┃┃
┃╰━━┳━━┳━┳╮╭┳━━┫┃╭━━┳━━┳━━╮
┃╭━━┫╭╮┃╭┫╰╯┃╭╮┃┃┃╭╮┃╭━┫╭╮┃
┃┃╱╱┃╭╮┃┃┃┃┃┃╭╮┃╰┫╰╯┃╰━┫╭╮┃
╰╯╱╱╰╯╰┻╯╰┻┻┻╯╰┻━┻━━┻━━┻╯╰╯
          """)
    print("1. Cadastrar remédio")
    print("2. Listar remédios")
    print("3. Alterar estado do remédio")
    print("4. Sair")

def escolhas():
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        cadastrar_remedio()
    elif escolha == 2:
        listar_remedio()
    elif escolha == 3: 
        alterar_remedio()
    elif escolha == 4: 
        sair()
    else: 
        print("Opção inválida")

def cadastrar_remedio():
    print("Cadastrar remédio")
    nome_remedio = input("Digite o nome remédio: ")
    array_remedio.append(nome_remedio)
    print(f"O remédio {nome_remedio} foi adicionado com sucesso!")

def listar_remedio():
    print("Listar remédios")
    j = 0
    for i in array_remedio:
        print(f"{j}: {i}")
        j += 1

def alterar_remedio():
    print("Alterar estado do remédio")
    listar_remedio()
    indice = int(input("Escolha uma opção para alterar: "))
    nome = input("Digite um novo nome: ")
    array_remedio[indice] = nome

def sair():
    global verifica
    print("Saindo...")
    verifica = False

def main():
    while verifica:
        menu()
        try: 
            escolhas()
        except:
            print(f"Opção inválida, tente outra\n")

if __name__ == '__main__':
    main()