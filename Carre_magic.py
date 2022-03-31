from pycsp3 import *
from tkinter import *

def genere_carre_magic():
    
    n = int(input("Donner valeur n: "))

    #Formule du TP à vérifier
    sum = int(n*(n*n+1)/2)

    #Définition du tableau
    x = VarArray(size=[n, n], dom=range(1, n*n+1))

    #Vérification des conditions pour le carré magique
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
        
        #Affichage du carré magique
        window = Tk()
        window.title("Carré magique: ")
        for row in range (n):
            for col in range (n):
                Button(window, text=x[row][col].grid(row=row, column =col))
        window.mainloop()
               
    
    
def genere_carre_bimagic():
    n = int(input("Donner valeur n: "))
    
    #Formule du carré magique
    sum = int(n*(n*n+1)/2)
    
    #Formule du carré bimagic à vérifier en plus
    sumSquared = int(n*(n*n+1)*(2*n*n+1)/6)
    
    #Grille de sudoku
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
    
    #Définition du tableau
    x = VarArray(size=[n, n], dom=range(1, n*n+1))
    
    #Vérification du carré bimagic
    satisfy(
         AllDifferent(x),
        [x[i][j] == clues[i][j] for i in range(9) for j in range(9)
     if clues and clues[i][j] > 0], #Condition pour remplir la grille de Sudoku
        
        #Condition carré magique
        [Sum(row) == sum for row in x],
        [Sum(col) == sum for col in columns(x)],
        
        #Diagonale à partir de la case (0,0)
        [Sum(x[i, i] for i in range(n)) == sum],
        #Diagonale à partir de la case (i,i)
        [Sum(x[i, n-i-1] for i in range(n)) == sum],
        
        #Condition à vérifier en plus pour carré bimagic
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
    

#Execution du programme 
if __name__ == "__main__":
    genere_carre_magic()
    genere_carre_bimagic()