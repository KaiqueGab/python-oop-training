import os

os.system('cls')

def cadastrar_rest():
    print('Cadastrando Restaurantes:')

def listar_rest():
    print('Listar restaurantes')

def ativar_rest():
    print('Ativar restaurantes')

def finalizar_app():
    os.system('cls')
    #os.system('clear') # Caso esteja no MAC
    print('Encerrando o programa\n')

def exibir_nome_programa():
    print("""
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n
        """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha alguma opção: '))

    match opcao_escolhida:
        case 1:
            cadastrar_rest()
        case 2:
            listar_rest()
        case 3:
            ativar_rest()
        case 4:
            finalizar_app()
        case _:
            print ('Opção invalida!')

def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()