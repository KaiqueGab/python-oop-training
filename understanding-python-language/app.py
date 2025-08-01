import os

restaurantes = [{'nome':'UaiRango', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Ifood', 'categoria':'Churracaria', 'ativo':True},
                {'nome':'Cantina Italiana', 'categoria':'Pizza', 'ativo':False}]

def voltar_menu():
    print()
    input('Digite uma tecla para voltar ao Menu Principal: ')
    main()


def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * (len(subtitulo))
    print(linha)
    print(subtitulo) 
    print(linha)
    print()


def cadastrar_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante.

    Inputs:
    - nome_restaurante: nome do restaurante a ser cadastrado
    - categ_restaurante: categoria do restaurante

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    exibir_subtitulo('Cadastros de Novos Restaurantes: ')
    
    nome_restaurante = input('Digite o nome do Restaurante que deseja Cadastrar: ')
    categ_restaurante = input(f'Digite o nome da Categoria do Restaurante {nome_restaurante}: ')

    dados_restaurante = {'nome':nome_restaurante, 
                         'categoria':categ_restaurante, 
                         'ativo':False
                         }

    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante "{nome_restaurante}" foi cadastrado com SUCESSO!')

    voltar_menu()


def listar_restaurante():
    '''
    Essa função é responsável por listar os restaurantes cadastrados.

    Outputs:
    - Exibe uma tabela com: nome, categoria e status (ativo/desativado) dos restaurantes.
    '''
    exibir_subtitulo('Listar Restaurantes: ')

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categ_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categ_restaurante.ljust(20)} | {ativo_restaurante}')

    voltar_menu()


def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado de um restaurante
    
    Inputs:
    - nome_restaurante: nome do restaurante a ser alterado
    - restaurante_encontrado: indica se o restaurante foi localizado

    Outputs:
    - mensagem: Exibe se o restaurante foi ativado ou desativado
    
    '''
    exibir_subtitulo('Alterando o estado Restaurante: ')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #Vai inverter o valor da chave [ativo]
            mensagem = f'O restaurante {nome_restaurante} foi ATIVADO com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi DESATIVADO com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_menu()
    

def finalizar_app():
    exibir_subtitulo('Finalizando o programa: ')


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
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha alguma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                alternar_estado_restaurante()
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