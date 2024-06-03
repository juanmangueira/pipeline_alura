import json
import csv

def coleta_dados():
    path = '../data_raw/'
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
    print(dados_empresaA)
    print(dados_empresaB)
main()