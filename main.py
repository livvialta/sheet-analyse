import pandas as pd 
import matplotlib as plt
from features.tarefas import Tarefas 
from os import system as cmd, name as osname
tarefas = Tarefas()

def clearScreen():
    cmd('cls' if osname == 'nt' else 'clear')
    
while True:
    clearScreen()
    print('Menu:')
    print('')
    print('1- Quantos pedidos - únicos - a loja Super Baratão teve no mês de Dezembro?')
    print('2- Qual foi o mês com maior percentual de rejeição da loja Mercado Marisol?')
    print('3- Quantos usuários fizeram pedidos na loja Mercado Preço Baixo no mês de Dezembro?')
    print('4- Construa um gráfico (e compartilhe comigo!) com o total de pedidos de 2022 e 2023. O gráfico deve exibir o total de tarefas de cada loja individualmente.')
    print('5- Identifique o % de variação de pedidos - únicos - por loja no período ano contra ano.')
    print('6- Sair')
    print('-----------------------------------------------------------------------------------')
    try:
        opcao = int(input('Escolha uma das opções abaixo (Digite o número): '))
        
        if opcao == 1:
            tarefas.unique_orders()
            print('')
            sleep = input('Pressione Enter para prosseguir...')
            clearScreen()
            
        elif opcao == 2:
            tarefas.rejection_orders()
            sleep = input('Pressione Enter para prosseguir...')
            clearScreen()
            
        elif opcao ==3:
            tarefas.users_orders()
            sleep = input('Pressione Enter para prosseguir...')
            clearScreen()
            
        elif opcao ==4:
            tarefas.total_orders_graphic()
            sleep = input('Pressione Enter para prosseguir...')
            clearScreen()
            
        elif opcao == 5:
            tarefas.variable_from_orders()
            sleep = input('Pressione Enter para prosseguir...')
            clearScreen()
            
        elif opcao ==6: 
            break
        
        else:
            print('ERRO! Escolha uma das opções válidas.')
    except ValueError:
        print('ERRO! Escolha uma das opções válidas.')
        sleep = input('Pressione Enter para prosseguir...')
        clearScreen()