import csv

def extrai_populacao():
    file = open('../data/dados_processados/populacao.csv')

def extrai_csv(file):
    infos = csv.reader(open(file))
    _ = next(infos)
    values = []
    for row in infos:
        if (row[1] != '' and len(row[1]) <= 3):
            value = []
            value.append(row[2]) # ano
            value.append(row[1]) # sigla
            value.append(row[3]) # info especifica
            # print(value)
            values.append(value)

    return values

extrai_csv('./data/dados_processados/country-and-continent-codes-list-csv.csv')
