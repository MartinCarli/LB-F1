#creo la lista number_list
number_list = [25, 70, 3, 40]

#stampo i valori della mia lista tramite fun. 'stampa'
def stampa(number_list):
        print(number_list)

stampa([25, 70, 3, 40])

#calcolo la sum, media, min, max degli elementi della mia lista tramite fun. 'statistiche'
def statistiche(number_list):
    sum=0
    media=0
    min=number_list[0]
    max=0

    for item in (number_list):
        sum=sum+item
        media=sum/2
        if item<min:
            min=item
        if item>max:
            max=item

    print('minimo:{}'.format(min))        
    print('somma:{}'.format(sum))
    print('media:{}'.format(media))
    print('massimo:{}'.format(max))
    
statistiche([25, 70, 3, 40])    

def somma_vettoriale(lista1, lista2):
    somma=[]
    check= False

    if len(lista1)==len(lista2):
        for i in range(0, len(lista1)):
            if type(lista[i])== int and type(lista2[i])==int:
                check = True 

   if check == True:
       for i in range(0, len(lista1)):
           somma.append(lista1[i]+lista2[i])

    return somma

def prodotto_vettoriale(lista1, lista2):

    prodotto=0
    check = False

    if len(lista1) == len(lista2):
        for i in range(0, len(lista1)):
            if type(lista[i])== int and type(lista2[i])==int:
                check=True

    if check == True:
        for i in range(0, len(lista1)):
            prodotto=prodotto+(lista1[i]*lista2[i])

    return prodotto

l1= [30, 25, 4, 8]
l2=[28, 3, 2, 1,]

print('la somma vettoriale è:', somma_vettoriale(l1,l2))
print('il prodotto vettoriale è:', prodotto_vettoriale(l1,l2))
            


