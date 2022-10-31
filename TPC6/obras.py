import csv
import matplotlib.pyplot as plt


#Carrega o dataset para uma estrutura de dados pensada por ti
def readDataset(fnome):
    f = open(fnome, encoding= 'utf-8')
    f.readline()    #lê uma linha, se eu não fizer nd com ela, o programa descarta-a
    csv_reader = csv.reader(f, delimiter=';')
    obras = []
    for row in csv_reader:
        obras.append(tuple(row))
    return obras

##print de forma mais bonita Pretty Print
def pp(obras):
    print(f'{obras[0][:25]:25} | {obras[4][:30]:30} | {obras[3][:15]:15} | {obras[2][:6]:6}')   # {obras[onde começa]][onde acaba]:anda este numero de espaços}

#Imprime no monitor uma tabela com o título da obra, a sua descrição, o seu compositor e ano de criação;
def Imptabela(obras):
    res = {
        'Título da obra': [],
        'Descrição': [],
        'Compositor': [],
        'Ano de criação': []
    }
    print(f"Título da obra      ::Descrição           ::Compositor          ::Ano")
    for nome, descricao, ano, compositor, *_ in obras:
        res['Título da obra'].append(nome)
        res['Descrição'].append(descricao)
        res['Compositor'].append(compositor)
        res['Ano de criação'].append(ano)
    print(f"{res['Título da obra']:10} :: {res['Descrição']:20} :: {res['Compositor']:10} :: {res['Ano de criação']:5}")
    
    return res
    


#Quantas obras eatão catalogadas no dataset?
def ndataset(obras):
    res = []
    for nome, *_ in obras:
        res.append(nome)
    obr = len(res)
    return obr

#ListaTitAno
def ordTit(t):
    return t[0]

#Ordenado Alfabéticamente
def TitAno(obras):
    res = []
    for nome, _, ano, *_ in obras:
        res.append((nome, ano))
    res.sort(key=ordTit)

#Produz um dicionário em que cada ano tem a ele associado a lista de títulos a ele associado
def TitPorAno(obras):
    res = {}
    for nome, _, ano, *_ in obras:
        if ano in res.keys():
            res[ano].append(nome)
        else:
            res[ano] = [nome]
    return res

#Produz uma lista ordenada dos compositores
def listComp(obras):
    res = []
    for _, _, _, _, compositor, *_ in obras:
        res.append(compositor)
    res.sort()
    return res

#Calcula uma distribuição das obras por período
def distPeriod(obras):
    res = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in res.keys():
            res[periodo] += 1
        else:
            res[periodo] = 1
    return res

#Calcula uma distribuição das obras por ano
def distAno(obras):
    res = {}
    for _, _, ano, *_ in obras:
        if ano in res.keys():
            res[ano] += 1
        else:
            res[ano] = 1
    return res

#Calcula uma distribuição das obras por compositor;
def distComp(obras):
    res = {}
    for _, _, _, _, compositor, *_ in obras:
        if compositor in res.keys():
            res[compositor] += 1
        else:
            res[compositor] = 1
    return res

#Especifica uma função que recebendo uma distribuição desenha o seu gráfico. Aplica-a às distribuições anteriores;
def graf(dist):
    x = []
    y = []
    for key in dist:
        x.append(key)
        y.append(dist[key])
    plt.bar(x, y)

#Calcula uma estrutura de dados que corresponde a uma lista dos compositores em que cada compositor tem a ele associado uma lista dos títulos das obras que compôs;
def TitComp(obras):
    res = {}
    for nome, _, _, _, compositor, *_ in obras:
        if compositor in res.keys():
            res[compositor].append[nome]
        else:
            res[compositor] = [nome]



#Cria uma função de visualização para estrutura de dados calculada na alínea anterior
def desenhaTabel(obras):
    res = {}
    for nome, _,_,_, compositor, *_ in obras:
        if compositor in res.keys():
            res[compositor].append(nome)
        else:
            res[compositor] = [nome]
    for k in res:
        print(f"|{str(k):20}, {str(res[k]):100}|")
