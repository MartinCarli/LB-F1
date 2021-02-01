#Creo una classe automobile
class Automobile():

    #Definisco la mia classe con i suoi attributi
    def __init__(self, casa_auto, modello, numero_posti, numero_portiere, kw, targa):
        self.casa_auto=casa_auto
        self.modello=modello
        self.numero_posti=numero_posti
        self.numero_portiere=numero_portiere
        self.kw=kw
        self.targa=targa

    #stampo le caratteristiche delle automobili presenti nella classe
    def __str__(self):
        return' {} {} {} {} {} {}'.format(self.casa_auto, self.modello, self.numero_posti, self.numero_portiere, self.kw, self.targa)
    
    #stampo 'Broom Broom' tramite la creazione della funzione parla
    def parla(self):
        print('Broom Broom')

    #TESTO ESERCIZIO:confronta, metodo che, dato in ingresso self e un’altra
    #istanza di Automobile, determina se le due automobili hanno le stesse informazioni
    #(eccetto per la targa che `e univoca!).

    #confronto se le auto hanno caratteristiche uguali
    def confronta(self,c, a):#a corrisponde ad automobile2
        #casa_auto
        if (c.casa_auto==a.casa_auto):
            print('= casa')
        else:
            print('!= casa')
        print('.................................................')
        #modello
        if (c.modello==a.modello):
            print('= modello')
        else:
            print('!= modello')
        print('.................................................')
        #numero_posti
        if(c.numero_posti==a.numero_posti):
            print('= numero di posti')
        else:
            print('!= numero di posti')
        print('.................................................')
        #numero_portiere
        if(c.numero_portiere==a.numero_portiere):
            print('= numero portiere')
        else:
            print('!= numero portiere')
        print('.................................................')
        #kw
        if (c.kw==a.kw):
            print('= kw')
        else:
            print('!= kw')
        print('.................................................')


    #considero il bollo per le diverse auto
    def bollo(self, cat):
        if (cat=='Euro0'):
            if (self.kw<100):
                print('Euro0 con kw<100, bollo:',self.kw*3)
            else:
                print('Euro0 con kw>100, bollo:', self.kw*4.50)
        elif (cat=='Euro1'):
            if (self.kw<100):
                print('Euro1 con kw<100, bollo:',self.kw*2.50)
            else:
                print('Euro1 con kw>100, bollo:', self.kw*4.35)
        else:
            print('Euro2, bollo:', self.kw*2)

automobile1=Automobile(casa_auto='Fiat', modello='600', numero_posti=4, numero_portiere=3, kw=56, targa='AB456CD')
automobile2=Automobile(casa_auto='Fiat', modello='Panda', numero_posti=5, numero_portiere=5, kw=69, targa='CD456AB')
automobile3=Automobile(casa_auto='Audi', modello='A1', numero_posti=5, numero_portiere=5, kw=90, targa='FP364UZ')
print('\t')
print('automobile1:')
print(automobile1)
print('automobile2:')
print(automobile2)
print('automobile3:')
print(automobile3)
print('\t')

automobile1.parla()
print('\t')

print('CONFR. AUTOMOBILE1 CON AUTOMOBILE2')
print(confronta(automabile1,automobile2))
print('\t')
print('CONFR. AUTOMOBILE2 CON AUTOMOBILE3')
print(confronta(automobile1,automobile3))
print('\t')

print(automobile1.bollo('Euro0'))










