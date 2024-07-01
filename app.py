import os
import time

array_remedios = [{"nome": "Zolpidem", "valor": 67.90, "ativo": False}, {"nome": "Paracetamol",
                                                                         "valor": 5.25, "ativo": True}, {"nome": "Clorazepam", "valor": 1000.00, "ativo": False}]
menu_ativo = True

def menu():
    print("""
    ╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
    ┃╭━━╯╱╱╱╱╱╱╱╱╱╱┃┃
    ┃╰━━┳━━┳━┳╮╭┳━━┫┃╭━━┳━━┳━━╮
    ┃╭━━┫╭╮┃╭┫╰╯┃╭╮┃┃┃╭╮┃╭━┫╭╮┃
    ┃┃╱╱┃╭╮┃┃┃┃┃┃╭╮┃╰┫╰╯┃╰━┫╭╮┃
    ╰╯╱╱╰╯╰┻╯╰┻┻┻╯╰┻━┻━━┻━━┻╯╰╯""")
    print("1. Cadastrar remédio")
    print("2. Listar remédios")
    print("3. Alterar estado do remédio")
    print("4. Sair")


def exibir_opcoes():
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            cadastrar_remedio()
        elif escolha == 2:
            listar_remedios(0) # 0 = listar
        elif escolha == 3:
            alterar_remedio()
        elif escolha == 4:
            sair()
        else:
            print("Opção inválida")
    except:
        print("Opção inválida, tente outra")


def cadastrar_remedio():
    os.system('cls')
    print("-- Cadastrar remédio --")

    nome_remedio = input("Digite o nome do remédio: ")
    valor_remedio = float(input("Digite o valor do remédio: "))
    str_ativo = input("O remédio digitado está ativo? (s para confirmar) ")
    ativo = False
    if str_ativo.lower() == "s": ativo = True
    
    remedio_nome = {"nome": nome_remedio,
                    "valor": valor_remedio, "ativo": ativo}
    array_remedios.append(remedio_nome)
    
    print(f"O remédio {nome_remedio} foi adicionado com sucesso!")
    time.sleep(2)
    voltar_ao_menu_principal()


def listar_remedios(alterar):
    os.system('cls')
    print("-- Listar remédio --")
    contador = 0
    for remedio in array_remedios:
        print(
            f" {contador} Nome: {remedio['nome']} - Valor: {remedio['valor']} - Status: {remedio['ativo']} ")
        contador += 1
    if(alterar == 0):
        voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def alterar_remedio():
    print("-- Alterar remédio --") #implementar Status 
    listar_remedios(1) # 1 = alterar
    nome_remedio = input("Digite o nome do novo remédio: ")
    valor_remedio = float(input("Digite o valor do novo remédio: "))
    str_ativo = input("O remédio digitado está ativo? (s para confirmar) ")
    ativo = False
    if str_ativo.lower() == "s": ativo = True
    
    remedio_nome = {"nome": nome_remedio,
                    "valor": valor_remedio, "ativo": ativo}
    pos_lista = int(input("Digite o numero ao lado do remedio que irá substituir: "))
    array_remedios[pos_lista] = remedio_nome
    print(f"O remédio {nome_remedio} foi adicionado com sucesso!")
    time.sleep(2)
    voltar_ao_menu_principal()

def sair():
    global menu_ativo
    print("Saindo do programa")
    menu_ativo = False


def main():
    os.system('cls')
    menu()
    exibir_opcoes()


if __name__ == '__main__':
    while menu_ativo:
        main()
