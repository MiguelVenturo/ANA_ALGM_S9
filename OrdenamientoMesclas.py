print("  "+
      "\n***Nuevo ordenamineto de lista por mesclas***"+
      "\n ")
def mergesort(a):
    n = len(a)
    if n == 1:
        return a
    mid = n // 2
    arrayOne = a[:mid]
    arrayTwo = a[mid:]
    arrayOne = mergesort(arrayOne)
    arrayTwo = mergesort(arrayTwo)
    return merge(arrayOne, arrayTwo)
def merge(a, b):
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    while a:
        c.append(a[0])
        a.pop(0)
    while b:
        c.append(b[0])
        b.pop(0)
    return c

lista = [3, 2, 9, 4, 6, 5, 8, 7, 10, 1]
print("Lista original: "+
"\n 3, 2, 9, 4, 6, 5, 8, 7, 10, 1"+
"\n ")
lista_ordenada = mergesort(lista)
print("La lista ordena es: ")
print(lista_ordenada)
print(" ")