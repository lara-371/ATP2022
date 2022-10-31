#MENU
import obras
myObras = obras.readDataset("obras.csv")
def menu():
    N = int(input("Escolha uma opção:"))
    if N == 1:
        print(obras.ndataset(myObras))
    elif N == 2:
        obras.Imptabela(myObras)
    elif N == 3:
        print(obras.TitAno(myObras))
    elif N == 4:
        print(obras.TitPorAno(myObras))
    elif N == 5:
        print(obras.listComp(myObras))
    elif N == 6:
        print(obras.distPeriod(myObras))
    elif N == 7:
        print(obras.distAno(myObras))
    elif N == 8:
        print(obras.distComp(myObras))
    elif N == 9:
        obras.graf(obras.distAno(myObras))
    elif N == 10:
        print(obras.TitComp(myObras))
    elif N == 11:
        obras.desenhaTabela(myObras)
    