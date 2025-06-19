import os

restaurantes = []

def cadastrar_rest():
    os.system('cls')
    print('Cadastros de Novos Restaurantes:\n')
    
    nome_rest = input('Digite o nome do Restaurante que deseja Cadastrar: ')
    restaurantes.append(nome_rest)
    print(f'\nO restaurante {nome_rest} foi cadastrado com SUCESSO!\n')

    print(30 * '=')
    input('Digite uma tecla para voltar ao Menu Principal: ')
    main()

def listar_rest():
    os.system('cls')
    print('Listar Restaurantes:\n')

    print(30 * '=')
    input('Digite uma tecla para voltar ao Menu Principal: ')
    main()

def ativar_rest():
    os.system('cls')
    print('Ativar Restaurantes:\n')

    print(30 * '=')
    input('Digite uma tecla para voltar ao Menu Principal: ')
    main()
    
def finalizar_app():
    os.system('cls')
    #os.system('clear') # Caso esteja no MAC
    print('Finalizando o programa\n')

def opcao_invalida():
    print('Opção Invalida!!\n')
    input('Digite uma tecla para voltar ao Menu Principal')
    main()

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
    try:
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
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')    
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()