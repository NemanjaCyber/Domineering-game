class Game:
    def __init__(self):
        self.n=0
        self.m=0
        self.Matrix=None
        self.kraj=False

    def main(self):
        self.dimenzije()
        self.pocetnoStanje()
        self.prikazTable()
        prviIgra=self.koIgraPrvi()
        for i in range(int((self.m * self.n) / 2)+1):
            if(self.kraj == False):
                if(i%2 == 0): self.igracX()
                else: self.igracO()

    def koIgraPrvi(self):
        print("Odaberite ko igra prvi, covek ili racunar (R - Racunar, C - Covek): ")
        igrac=input()
        return igrac

    def dimenzije(self):
        print("DOMINEERING IGRA")
        print("Unesite broj vrsta: ")
        self.n=int(input())
        print("Unesite broj kolona: ")
        self.m=int(input())

    def pocetnoStanje(self):
        self.Matrix = [ [ i*j for j in range(self.m) ] for i in range(self.n) ]
        for i in range(self.n):
            for j in range(self.m):
                self.Matrix[i][j]=' '
    
    def prikazTable(self):
        print(" ",chr(65),end="")
        for j in range(self.m-1):
            print ("",chr(j+66),end="")
        print(" ")
        print("  =",end="")
        for j in range(self.m-1):
            print(" =",end="")
        print(" ")
        for i in range(self.n):
            print(i+1,end=" ")
            for j in range(self.m):
                print(self.Matrix[i][j],end=" ")
            print("")
        print("  =",end="")
        for j in range(self.m-1):
            print(" =",end="")
        print(" ")
        print(" ",chr(65),end="")
        for j in range(self.m-1):
            print ("",chr(j+66),end="")
        print(" ")
        print("")
    
    def igracX(self):
        if self.krajIgreX():
            print("Igrac X je na potezu: ")
            self.predloziPotezX()
            print("Unesite vrstu: ")
            vrsta=int(input())
            print("Unesite kolonu: ")
            kolonaStr=input()
            kolona=ord(kolonaStr)-65
            if self.proveriPotezX(vrsta,kolona): 
                self.Matrix[vrsta-1][kolona]='X'
                self.Matrix[vrsta-2][kolona]='X'
                self.prikazTable()

    def proveriPotezX(self,vrsta,kolona):
        if vrsta>self.n or vrsta<=1 or kolona>self.m or kolona<0:
            print("Nevalidan potez igraca X. Odigrajte opet: ")
            self.igracX()
        elif self.Matrix[vrsta-1][kolona]=='X' or self.Matrix[vrsta-2][kolona]=='X' or self.Matrix[vrsta-1][kolona]=='O' or self.Matrix[vrsta-2][kolona]=='O':
            print("Pozicije zauzete. Odigrajte opet sa novim pozicijama: ")
            self.igracX()
        else: return True

    def krajIgreX(self):
        imaPoteza = False
        for j in range(self.m):
            for i in range(self.n-1):
                if(self.Matrix[i][j] == ' ' and self.Matrix[i+1][j] == ' '):
                    imaPoteza = True
        if imaPoteza == False:
            print("Igrac O je pobedio! Kraj igre!")
            self.kraj = True
        return imaPoteza
            
    def igracO(self):
        if self.krajIgreO():
            print("Igrac O je na potezu: ")
            self.predloziPotezO()
            print("Unesite vrstu: ")
            vrsta=int(input())
            print("Unesite kolonu: ")
            kolonaStr=input()
            kolona=ord(kolonaStr)-65
            if self.proveriPotezO(vrsta,kolona):
                self.Matrix[vrsta-1][kolona]='O'
                self.Matrix[vrsta-1][kolona+1]='O'
                self.prikazTable()

    def proveriPotezO(self,vrsta,kolona):
        if vrsta>self.n or vrsta<0 or kolona>self.m-2 or kolona<0:
            print("Nevalidan potez igraca O. Odigrajte opet: ")
            self.igracO()
        elif self.Matrix[vrsta-1][kolona]=='O' or self.Matrix[vrsta-1][kolona+1]=='O' or self.Matrix[vrsta-1][kolona]=='X' or self.Matrix[vrsta-1][kolona+1]=='X':
            print("Pozicije zauzete. Odigrajte opet sa novim pozicijama: ")
            self.igracO()
        else: return True

    def krajIgreO(self):
        imaPoteza = False
        for i in range(self.n):
            for j in range(self.m-1):
                if(self.Matrix[i][j] == ' ' and self.Matrix[i][j+1] == ' '):
                    imaPoteza = True
        if imaPoteza == False:
            print("Igrac X je pobedio! Kraj igre!")
            self.kraj = True
        return imaPoteza
    
    def predloziPotezX(self):
        listaPolja=[]
        for j in range(self.m):
            for i in range(self.n-1):
                if(self.Matrix[i][j]==' 'and self.Matrix[i+1][j]==' '):
                    listaPolja.append([i+2,chr(j+65)])
        print("Moguci potezi koje mozete da odigrate su: ")
        print(listaPolja)

    def predloziPotezO(self):
        listaPolja=[]
        for i in range(self.n):
            for j in range(self.m-1):
                if(self.Matrix[i][j]==' 'and self.Matrix[i][j+1]==' '):
                    listaPolja.append([i+1,chr(j+65)])
        print("Moguci potezi koje mozete da odigrate su: ")
        print(listaPolja)

a=Game()
a.main()