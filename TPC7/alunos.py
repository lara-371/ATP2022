import csv
import matplotlib.pyplot as plt


#Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória;
def lerAlunos(fname):
    f = open(fname, encoding= 'utf-8')
    f.readline()
    csv_reader = csv.reader(f, delimiter=',')
    alunos = []
    for row in csv_reader:
        alunos.append(tuple(row))
    return alunos

alunos = lerAlunos("alunos.csv")

#Crie uma função que calcula a distribuição dos alunos por curso;
def distCurso(alunos):
    res = {}
    for _,_, curso, *_ in alunos:
        if curso in res.keys():
            res[curso] += 1
        else:
            res[curso] = 1
    return res

#Crie uma função que calcula a média das notas de cada aluno e acrescenta essa nova coluna no dataset em memória;
def medNotas(alunos):
    res = []
    for id_aluno, nome, curso, tpc1, tpc2, tpc3, tpc4 in alunos:
        n = int(tpc1)+ int(tpc2)+ int(tpc3)+ int(tpc4)
        media = (int(n/4))
        tuplo = (id_aluno, nome, curso, tpc1, tpc2, tpc3, tpc4, media)
        res.append(tuplo)
    return res

alunos1 = medNotas(alunos)

#Considere os seguintes escalões de notas: E [1-4], D [5-8], C [9-12], B [13-16], A [17-20], acrescente uma coluna ao dataset com o escalão correspondente a cada aluno;
def escalaoAluno(alunos1):
    res = []
    escalao = ()
    for id_aluno, nome, curso, tpc1, tpc2, tpc3, tpc4, media in alunos1:
        if media>=1 and media<=4:
            escalao = ("E")
        elif media>=5 and media<=6:
            escalao = ("D")
        elif media>=9 and media<=12:
            escalao = ("C")
        elif media>=13 and media<=16:
            escalao = ("B")
        elif media>=17 and media<=20:
            escalao = ("A")
        tuplo = (id_aluno, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao)
        res.append(tuplo)
    return res
        
alunos2 = escalaoAluno(alunos1)

#Crie uma distribuição dos alunos por escalão;
def distEsc(alunos2):
    res = {}
    for _, _, _, _, _, _, _, _, escalao in alunos2:
        if escalao in res:
            res[escalao] +=1
        else:
            res[escalao] = 1
    return res

#Crie uma função que apresenta na forma dum gráfico de linha uma distribuição;
def grafDistCurso(alunos):
    res = {}
    for _, _, curso, *_ in alunos:
        if curso in res.keys():
            res[curso] += 1
        else:
            res[curso] = 1
        
        x = res.keys()
        y = res.values()

    plt.plot(x, y)
    plt.xlabel("Cursos")
    plt.ylabel("Nº de alunos")
    plt.show()

def grafDistEscalao(alunos2):
    res = {}
    for _,_,_,_,_,_,_,_, escalao in alunos2:
        if escalao in res:
            res[escalao] += 1
        else:
            res[escalao] = 1
        
        x = res.keys()
        y = res.values()

    plt.plot(x, y)
    plt.xlabel("Escalão")
    plt.ylabel("Nº de alunos")
    plt.show()


#Crie uma função que imprime na forma de uma tabela uma distribuição
def tabelaCursos(alunos2):
    res = {}
    for _,_, curso, *_ in alunos2:
        if curso in res:
            res[curso] += 1
        else:
            res[curso] = 1
    
    n=0
    l = list(res.keys())
    c = list(res.values())
    print(f"| {'Curso:':20} | {'Nº de alunos no Curso:':14} |")

    while n < len(res):
        print(f"| {str(l[n]):20} | {str(c[n]):26} |")
        n = n + 1

def tabelaEscalao(alunos2):
    res = {}
    for _,_,_,_,_,_,_,_, escalao in alunos2:
        if escalao in res:
            res[escalao] += 1
        else:
            res[escalao] = 1
    
    n=0
    l = list(res.keys())
    c = list(res.values())
    print(f"| {'Escalão:':20} | {'Nº de alunos no Curso:':14} |")

    while n < len(res):
        print(f"| {str(l[n]):20} | {str(c[n]):26} |")
        n = n + 1


    
#MENU
def menu():
    print('''
    (1) Ler Alunos
    (2) Distribuir alunos por curso
    (3) Gráfico de distribuição por curso
    (4) Tabela de distribuição por curso
    (5) Calcular média de cada aluno
    (6) Calcular escalão de cada aluno
    (7) Distribuir alunos por escalão
    (8) Gráfico de distribuição de alunos por escalão
    (9) Tabela de distribuição por escalão
    (0) Sair
    ''')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        print(lerAlunos())
    elif op == 2:
        distCurso(alunos)
    elif op == 3:
        medNotas(alunos)
    elif op == 4:
        grafDistCurso(alunos)
    elif op == 5:
        tabelaCursos(alunos)
    elif op == 6:
        escalaoAluno(alunos1)
    elif op == 7:
        distEsc(alunos1)
    elif op == 8:
        grafDistEscalao(alunos2)
    elif op == 9:
        tabelaEscalao(alunos2)
    elif op == 0:
        print('Sair')
    menu()