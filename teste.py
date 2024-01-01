import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt


def ajuda():

    print('v1 = view table')
    print('v2= view table in an orderly way' )
    print('v3 = view income table by city ')
    print('v4 = view income table by city , by starting point ')


def análise():
    print('ola tudo bem')
    q1 = input('digite o comando desejável')
    if(q1 == 'v1'):
        tabela = pd.read_excel('dados_rotes_novos.xlsx')
        display(tabela)

    elif(q1 == 'v2'):
        tabela = pd.read_excel('dados_rotes_novos.xlsx')
        df = tabela.sort_values(by='load_value', ascending=False)
        display(df)

    elif(q1 == 'v3'):
        tabela = pd.read_excel('dados_rotes_novos.xlsx')
        #renda_cidade = tabela[['id','destin','load_value']].groupby('id', 'destin').sum()
        destino_grouped = tabela.groupby('destin').agg({'load_value': 'sum', 'id': 'count'}).reset_index()
        df2 = destino_grouped.sort_values(by = 'load_value',ascending= False )
        display(df2)

    elif(q1 == 'v4'):
        tabela = pd.read_excel('dados_rotes_novos.xlsx')
        #renda_cidade = tabela[['id','destin','load_value']].groupby('id', 'destin').sum()
        starting_grouped = tabela.groupby('starting point').agg({'load_value': 'sum', 'id': 'count'}).reset_index()
        df3 = starting_grouped.sort_values(by = 'load_value',ascending= False )
        display(df3)




        






def main():
    ajuda()
    análise()


if __name__ == "__main__":
    main()


#terminardepois
    

