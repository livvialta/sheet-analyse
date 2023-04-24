import pandas as pd
import matplotlib.pyplot as plt


class Tarefas:
    def __init__(self) -> None:
        self.df = pd.read_excel("./dados/processo.xlsx")
        
    def unique_orders(self):
        self.df['Date Date'] = pd.to_datetime(self.df['Date Date'])

        super_baratao_dec = self.df[(self.df['Store Name'] == 'Super Baratão') & (self.df['Date Date'].dt.month == 12)]

        num_pedidos = super_baratao_dec['Quantity SKU'].sum() 

        print(num_pedidos)
        
    def rejection_orders(self):
        
        mercado_marisol = self.df[self.df['Store Name'] == 'Mercado Marisol']

        pedidos_por_mes = mercado_marisol.groupby(mercado_marisol['Date Date'].dt.month)['Order Number'].count()
        pedidos_rejeitados_por_mes = mercado_marisol[mercado_marisol['Orden aprobada (Yes / No)'] == 'No'].groupby(mercado_marisol['Date Date'].dt.month)['Order Number'].count()

        percentual_rejeicao_por_mes = (pedidos_rejeitados_por_mes / pedidos_por_mes) * 100

        mes_maior_rejeicao = percentual_rejeicao_por_mes.idxmax()

        print("O mês com maior percentual de rejeição na loja Mercado Marisol foi o mês:", mes_maior_rejeicao)
        
    def users_orders(self):
        
        mercado_preco_baixo_dec = self.df[(self.df['Store Name'] == 'Mercado Preço Baixo') & (self.df['Date Date'].dt.month == 12)]

        num_usuarios = mercado_preco_baixo_dec['User Phone Number'].nunique()

        print("O número de usuários que fizeram pedidos na loja Mercado Preço Baixo no mês de Dezembro foi:", num_usuarios)

    def total_orders_graphic(self):
        
        #2022 e 2023
        pedidos_filtrados = self.df[self.df['Date Date'].dt.year.isin([2022, 2023])]

        total_by_loja = pedidos_filtrados.groupby('Store Name')['Quantity SKU'].sum().reset_index()


        plt.figure(figsize=(10, 6))
        plt.bar(total_by_loja['Store Name'], total_by_loja['Quantity SKU'], color='yellow',width=0.2)
        plt.xlabel('Loja')
        plt.ylabel('Total de Pedidos')
        plt.title('Total de Pedidos por Loja - (2022-2023)')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig('./graphics/total_orders_2022_2023.png')
        plt.show()

    def variable_from_orders(self):

        ano_anterior = self.df[self.df['Date Date'].dt.year == 2022]
        ano_atual = self.df[self.df['Date Date'].dt.year == 2023]


        pedidos_unicos2022 = ano_anterior.groupby('Store Name')['User Phone Number'].nunique()
        pedidos_unicos2023 = ano_atual.groupby('Store Name')['User Phone Number'].nunique()

        percentual = ((pedidos_unicos2023 - pedidos_unicos2022) / pedidos_unicos2022) * 100

        self_variacao_percentual = pd.DataFrame({'Loja': percentual.index, '% de Variação': percentual.values})
        print(self_variacao_percentual)
