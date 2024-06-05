import json
import csv

def coleta_dados():
    path = './data_raw/'
    with open(path + 'dados_empresaA.json', 'r') as file:
        dados_empresaA = json.load(file)
    
    dados_empresaB = []
    with open(path + 'dados_empresaB.csv', 'r') as file:
        spamreader = csv.DictReader(file,delimiter=',')
        for row in spamreader:
            dados_empresaB.append(row)
    
    return dados_empresaA, dados_empresaB

def main():
    dados_empresaA, dados_empresaB = coleta_dados()
    colunas_empresaA = list(dados_empresaA[0].keys())
    colunas_empresaB = list(dados_empresaB[0].keys())
    print(colunas_empresaA)
    print(colunas_empresaB)

    key_mapping = {'Nome do Item':'Nome do Produto', 
                   'Classificação do Produto':'Categoria do Produto', 
                   'Valor em Reais (R$)':'Preço do Produto (R$)', 
                   'Quantidade em Estoque':'Quantidade em Estoque', 
                   'Nome da Loja':'Filial', 
                   'Data da Venda':'Data da Venda'}
    
    new_dados_empresaB = []
    
    for dict_old in dados_empresaB:
        dict_temp = {}
        for key_old, value in dict_old.items():
            dict_temp[key_mapping[key_old]] = value
        new_dados_empresaB.append(dict_temp)
    
    dados_empresas = []
    dados_empresas.extend(dados_empresaA)
    dados_empresas.extend(new_dados_empresaB)

main()