#  nella seconda parte del programma c e qualche piccolo errore
# perche non riesce ad aprire il la seconda lista




#                 INIZIO            #

listanumeri= [11,2,3,4,5]

#1
##########   funzione che stampa     #######################
print("\n ADESSO STAMPO LA PRIMA LISTA")
print('\n ~~~~~o~~~~~o~~~~~o~~~~~o~~~~~\n')
def stampa(numeri):
  print(numeri)


stampa(listanumeri)

############################################################


#2
############## statistaiche ############################
print("\n ADESSO CALCOLO QUALCHE INFORMAZIONI DELLA 1 LISTA")
print('\n ~~~~~o~~~~~o~~~~~o~~~~~o~~~~~\n')

def statistiche(numberlist):
    som=0
    min=numberlist[0]
    max=numberlist[0]
    media=0
    for item in (numberlist):
      som = item + som
      if(min>item):
        min= item
      if(max<item):
        max=item
    n=len(numberlist)
    media= som/n
  
    print('\nSomma= {}'.format(som))
    print('\nMedia= {}'.format(media))
    print('\nMin= {}'.format(min))
    print('\nMax= {}'.format(max))

statistiche(listanumeri)
####################################################

#3
#################### sommavettoriale ######################
print("\n ADESSO CALCOLO LA SOMMA VETTORIALE")
print('\n ~~~~~o~~~~~o~~~~~o~~~~~o~~~~~\n')

lista1= [1,2,3,4,5]
lista2= [5,4,3,2,1]

def sommavettoriale(lista1,lista2):

  verifica1=1

  for item in (lista1):
    if not isinstance(item,int):
      verifica1= verifica1 * 0
  if verifica1 == 1:
    print('\nLa lista contiene numeri intei')
  if verifica1 == 0:
    print('\nC e qualche numero che non e intero')

  verifica2=1

  for item in (lista2):
    if not isinstance(item,int):
      verifica2= verifica2 * 0
  if verifica2== 1:
    print('\nLa  seconda lista contiene numeri intei')


  if verifica2 == 0:
    print('\nC e qualche numero nella seconda lista che non e intero')

  n=len(lista1)
  c=len(lista2)

  if(c == n):
    printf('\nLe liste hanno la stessa lunghezza')

  sommal= []

  if(c==n and verifica1 == 1 and verifcia2 == 1):
    for i in range(0,c):
      sommal.append(lista1[i]+lista2[i])
    print('\nLa somma vettoriale e: {}'.format(sommal))
  if(c != n):
    print('\nLe liste non hanno la stessa lunghezza')

  if(c!= n or verifica1 != 1 or verifcia2 != 1):
    print('\nLa lista della somma vettoriale e` vuota: {}'.format(sommal))

sommavettoriale(lista1,lista2)
#4
########################## PRODOTTO VETTORIALE ##########
print("\n ADESSO CALCOLO IL PROFOTTO VETTORIALE")
print('\n ~~~~~o~~~~~o~~~~~o~~~~~o~~~~~\n')


def prodottovettoriale(lista1,lista2):
  verifica1=1
  for item in (lista1):
    if not isinstance(item,int):
      verifica1 = verifica1 * 0
  if verifica1 == 1:
    print('\nLa lista contiene numeri intei')
  if verifica1 == 0:
    print('\nC e qualche numero che non e intero')

  verifica2=1

  for item in (lista2):
    if not isinstance(item,int):
      verifica2= verifica2 * 0
  if verifica2 == 1:
    print('\nLa  seconda lista contiene numeri intei')


  if verifica2 == 0:
    print('\nC e qualche numero nella seconda lista che non e intero')

  n=len(lista1)
  c=len(lista2)

  if(c is n):
    printf('\nLe liste hanno la stessa lunghezza')

  prodotto= []

  if(c == n and verifica1 == 1 and verifcia2 == 1):
    for i in range(0,c):
      proddoto.append(lista1[i]+lista2[i])
    print('\nLa prodotto vettoriale e: {}'.format(prodotto))
  if(c is not n):
    print('\nLe liste (prodotto) non hanno la stessa lunghezza')

  if(c != n or verifica1 != 1 or verifcia2 != 1):
    print('\nATTENZIONE: non sono riuscito a calcolare il prodotto vettoriale')

prodottovettoriale(lista1,lista2)
##################### finito tutte le funzioni ##########
