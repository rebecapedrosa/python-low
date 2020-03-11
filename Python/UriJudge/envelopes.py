n = int(input())

for i in range(0,n):
        lista = input().split('')
        a = int(lista[0])
        b = int(lista[1])
        c = int(lista[2])
        d = int(lista[3])
        if(a>b):
            largura1 = a
            altura1 = b
        else:
            largura1 = b
            altura1 = a

        if(c>d):
            largura2 = c
            altura2 = d
        else:
            largura2 = d
            altura2 = c

        if(altura2>altura1 and largura2>largura1):
            print("S")
        else:
            print("N")
