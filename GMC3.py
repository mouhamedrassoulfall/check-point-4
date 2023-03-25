#exercice1
def maximum(x,y,z):
    return max(x,y,z)

print(maximum(20, 35, 19))




#exercice2
def calcul(a, b):
    addition = a + b
    soustraction = a - b

    return addition, soustraction


print(calcul(40, 10))


#exercice3
def addition(liste):
    r = 1
    for x in liste:
        r += x
    return r
def listMultiply(liste):
    r = 1
    for x in liste:
        r *= x

    return r


def extraire(liste):
    pair=[]
    impaire=[]
    for i in liste:
        if i % 2==0:
            pair.append(i)

        else:
            impaire.append(i)


    print(addition(pair))
    print(listMultiply(impaire))
liste =[0,1,2,3,4,5,6,7,8,9,10]
print(extraire(liste))


#exercice4
dict = {"Gfg": ["ab", "cd", "ef"],"kdh": ["gh", "ij"], "is": ["kl"]}

x = {key: list(map(str.capitalize, dict[key])) for key in dict}


print( str(x))



#exercice5
def maxdct():
    max(d, key=len)




#exercice6
def trier(sequence):
  b = sequence.split('-')
  b.sort()
  c = '-'.join(b)
  return c

a = input('entrer un sequence de couleur separer par tiret ')
print(trier(a))
