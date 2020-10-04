# Pontícia Universidade Católica de Minas Gerais
# Instituto de Ciências Exatas e Informática
# Praça da Liberdade
# Engenharia de Software - 6º Período - Noite
# Aluno: Kelton Melo de Oliveira Fonseca
# 
# O programa a seguir faz uma requisição à API do gitHub utilizando GraphQL para conultar os 100 repositórios com maior numero de estrelas nas linguagens Python e  100 da linguagem Java, 
# separando o JSON recebido em módulos cada vez menores a fim de acessar os dados. Tais dados são armazenados em dois arquivos .csv separados por linguagem

import requests
import csv


url = 'https://api.github.com/graphql'
qry = '"language:python"'
api_token = "c9269fbff3e26e513120156dba1d327e0f614b94"
headers = {'Authorization': 'token %s' % api_token}
json = { 'query' : '{ search(query: "language:python", type: REPOSITORY, first: 100) { edges {  node { ... on Repository {  nameWithOwner   createdAt     stargazerCount      primaryLanguage { name } watchers {  totalCount  } forks {  totalCount   } releases { totalCount   } } } } repositoryCount}}' }
response = requests.post(url=url, json=json, headers=headers)
print("Iniciando busca de repositórios Pyhton no GitHub")

with open('Dados_Python.csv', mode='w', newline='') as file:
    while(response.status_code != 200):
        print("Erro na requisição, tentando novamente")
        response = requests.post(url=url, json=json, headers=headers)
    item = 0
    writer = csv.writer(file)
    writer.writerow(["NameWithOwner", "Data Criação", "Total de estrelas", "Linguagem", "Nº de Watchers", "Nº de Forks", "Nº de Releases"])
    data = response.json()
    dadosQry = data['data']
    dadosPesq = dadosQry['search']
    edge = dadosPesq['edges']
    print("Escrevendo informações")
    while (item<100):
        position = edge[item]
        node = position['node']
        qtdReleases = node['releases']
        linguagem = node['primaryLanguage']
        qtdForks = node['forks']
        qtdWatchers = node['watchers']
        if(linguagem == None):
            writer.writerow([node['nameWithOwner'],node['createdAt'], node['stargazerCount'] , 'Não especificado', qtdForks['totalCount'], qtdWatchers['totalCount'],qtdReleases['totalCount']])
        else:
            writer.writerow([node['nameWithOwner'],node['createdAt'], node['stargazerCount'] , linguagem['name'], qtdForks['totalCount'], qtdWatchers['totalCount'], qtdReleases['totalCount']])
        item = item + 1 

# Cria arquivo Java
qry = '"language:python"'
json = { 'query' : '{ search(query: "language:java", type: REPOSITORY, first: 100) { edges {  node { ... on Repository {  nameWithOwner   createdAt     stargazerCount      primaryLanguage { name } watchers {  totalCount  } forks {  totalCount   } releases { totalCount   } } } } repositoryCount}}' }
response = requests.post(url=url, json=json, headers=headers)
print("Iniciando busca de repositórios Java no GitHub")
with open('Dados_Java.csv', mode='w', newline='') as file:
    while(response.status_code != 200):
        print("Erro na requisição, tentando novamente")
        response = requests.post(url=url, json=json, headers=headers)
    item = 0
    writer = csv.writer(file)
    writer.writerow(["NameWithOwner", "Data Criação", "Total de estrelas", "Linguagem", "Nº de Watchers", "Nº de Forks", "Nº de Releases"])
    data = response.json()
    dadosQry = data['data']
    dadosPesq = dadosQry['search']
    edge = dadosPesq['edges']
    print("Escrevendo informações")
    while (item<100):
        position = edge[item]
        node = position['node']
        qtdReleases = node['releases']
        linguagem = node['primaryLanguage']
        qtdForks = node['forks']
        qtdWatchers = node['watchers']
        if(linguagem == None):
            writer.writerow([node['nameWithOwner'],node['createdAt'], node['stargazerCount'] , 'Não especificado', qtdForks['totalCount'], qtdWatchers['totalCount'],qtdReleases['totalCount']])
        else:
            writer.writerow([node['nameWithOwner'],node['createdAt'], node['stargazerCount'] , linguagem['name'], qtdForks['totalCount'], qtdWatchers['totalCount'], qtdReleases['totalCount']])
        item = item + 1 
        
print("Arquivos escrito com sucesso")