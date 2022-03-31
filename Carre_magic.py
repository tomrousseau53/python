from pycsp3 import *

def genere_carre_magic():
    n = int(input("Donner valeur n: "))

    sum = int(n*(n*n+1)/2)

    x = VarArray(size=[n, n], dom=range(1, n*n+1))

    satisfy(
        AllDifferent(x),
        [Sum(row) == sum for row in x],
        [Sum(col) == sum for col in columns(x)],
        [Sum(x[i, i] for i in range(n)) == sum],
        [Sum(x[i, n-i-1] for i in range(n)) == sum],
    )
    
    #supprimer sols=ALL pour trouver la première solution qui vient le nombre de solutions ne sera plus representatif mais ca ira plus vite
    
    if solve(sols=ALL) is SAT:
        for i in range(n):
            print(values(x[i]))
        print("Number of solutions: ", n_solutions())
        print("Domain of any variable: ", x[0][0].dom)

def genere_carre_bimagic():
    n = int(input("Donner valeur n: "))
    sum = int(n*(n*n+1)/2)
    sumSquared = int(n*(n*n+1)*(2*n*n+1)/6)
    
    clues = [
        [0, 2, 0, 5, 0, 1, 0, 9, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 6],
        [0, 3, 0, 0, 6, 0, 0, 7, 0],
        [0, 0, 1, 0, 0, 0, 6, 0, 0],
        [5, 4, 0, 0, 0, 0, 0, 1, 9],
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [0, 9, 0, 0, 3, 0, 0, 8, 0],
        [2, 0, 0, 8, 0, 4, 0, 0, 7],
        [0, 1, 0, 9, 0, 7, 0, 6, 0]
    ]
    
    x = VarArray(size=[n, n], dom=range(1, n*n+1))
    
    satisfy(
        AllDifferent(x),
        [x[i][j] == clues[i][j] for i in range(9) for j in range(9)
     if clues and clues[i][j] > 0],
        [Sum(row) == sum for row in x],
        [Sum(col) == sum for col in columns(x)],
        [Sum(x[i, i] for i in range(n)) == sum],
        [Sum(x[i, n-i-1] for i in range(n)) == sum],
        [Sum(x[i, j]*x[i, j] for i in range(n) for j in range(n)) == sumSquared],
        [Sum(x[j, i]*x[j, i] for i in range(n) for j in range(n)) == sumSquared],
        [Sum(x[i, i]*x[i, i] for i in range(n)) == sumSquared],
        [Sum(x[i, n-i-1] * x[i, n-i-1] for i in range(n)) == sumSquared],
    
    )
    
    if solve(sols=ALL) is SAT:
        for i in range(n):
            print(values(x[i]))
        print("Number of solutions: ", n_solutions())
        print("Domain of any variable: ", x[0][0].dom)
    else:
        print("No solutions for bimagic")
 
if __name__ == "__main__":
    genere_carre_magic()
    genere_carre_bimagic()