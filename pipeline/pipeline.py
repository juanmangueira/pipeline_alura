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

def processa_dados(dados_1:dict, dados_2:dict):
    dados_empresaA = dados_1
    dados_empresaB = dados_2

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
    
    dados_agrupados = []
    dados_agrupados.extend(dados_empresaA)
    dados_agrupados.extend(new_dados_empresaB)
    return dados_agrupados

def main():
    dados_empresaA, dados_empresaB = coleta_dados()
    dados_agrupados = processa_dados(dados_empresaA, dados_empresaB)
    colunas = list(dados_agrupados[-1].keys())
    print(colunas)
    path = './data_processed/'
    with open(path+'dados_empresas.csv','w') as file:
        writer = csv.DictWriter(file, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(dados_agrupados)

main()