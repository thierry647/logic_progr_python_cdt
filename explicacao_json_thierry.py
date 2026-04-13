'''
arquivos *.txt;

arquivos *.json;

arquivos *.csv;

explicaçao de como exibir e ler codigos para monstrar o arquivo json


'''

import os
import json

def configurar_sistema():
    if not os.path.exists('uploads_projetos'):
        os.makedirs('uploads_projetos')


def listar_projetos():
    arquivos = [f for f in os.listdir('uploads_projetos') if f.endswith('.json')]
    print('\n' + '-'*40)
    print(' PROJETOS LISTADOS')
    print('\n' + '-'*40)

    if not arquivos:
        print('Nenhum projeto encontrado.')
        return []
    for i, arquivos in enumerate(arquivos, 1):
        nome_exibicao = arquivos.replace('projetos_', '').replace('.json', '').replace('_', ' ')
        print(f"{i}. {nome_exibicao.title()}")
    return arquivos 

def gerenciar_projetos():
    arquivos = listar_projetos()
    if not arquivos: return 

    try:
        escolha = int(input('\n Escolha o numero do projeto para gerenciar(ou 0 para voltar): '))
        if escolha == 0: return

        nome_arquivo = arquivos[escolha - 1]
        caminho = f"uploads_projetos/{nome_arquivo}"

        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)

            print(f'\n ---- Nova Atualização ---- ')
            print(f'Aluno: {dados["aluno"]}')
            print(f'Projeto: {dados["projeto"]}')







            