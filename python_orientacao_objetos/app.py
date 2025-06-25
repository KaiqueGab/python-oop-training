import os

restaurantes = [{'nome':'UaiRango', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Ifood', 'categoria':'Churracaria', 'ativo':True},
                {'nome':'Cantina Italiana', 'categoria':'Pizza', 'ativo':True}]

def voltar_menu():
    print('\n' + 30 * '=')
    input('Digite uma tecla para voltar ao Menu Principal: ')
    main()


def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(f'{subtitulo}:\n')


def cadastrar_rest():
    exibir_subtitulo('Cadastros de Novos Restaurantes')
    
    nome_rest = input('Digite o nome do Restaurante que deseja Cadastrar: \n')
    categ_rest = input(f'Digite o nome da Categoria do Restaurante {nome_rest}: ')

    dados_rest = {'nome':nome_rest, 'categoria':categ_rest, 'ativo':False}

    restaurantes.append(dados_rest)
    print(f'\nO restaurante {nome_rest} foi cadastrado com SUCESSO!')

    voltar_menu()


def listar_rest():
    exibir_subtitulo('Listar Restaurantes')

    for restaurante in restaurantes:
        nome_rest = restaurante['nome']
        categ_rest = restaurante['categoria']
        ativo_rest = restaurante['ativo']
        print(f'- {nome_rest} | {categ_rest} | {ativo_rest}')

    voltar_menu()


def ativar_rest():
    exibir_subtitulo('Ativar Restaurantes')

    voltar_menu()
    

def finalizar_app():
    exibir_subtitulo('Finalizando o programa')


def opcao_invalida():
    print('Opção Invalida!!\n')
    voltar_menu()


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