import csv

def extrai_populacao():
    file = open('../data/dados_processados/populacao.csv')

def extrai_csv(file, info1, info2, info3):
    infos = csv.reader(open(file))
    _ = next(infos)
    values = []
    for row in infos:
        if (row[1] != '' and len(row[1]) <= 3):
            value = []
            value.append(row[info1]) # info1
            value.append(row[info2]) # info2
            value.append(row[info3]) # info3
            # print(value)
            values.append(value)

    return values

