#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def comparateur(filepath1,filepath2):
    with open(filepath1, 'r', encoding="utf-8") as file1:
        with open(filepath2,'r',encoding="utf-8") as file2:
            for count,line1 in enumerate(file1):
                line2=file2.readline()
                if line2!=line1:
                    print("la difference est dans la ligne est : ",count+1)
                    print(line1)
                    print(line2)
                    
                    return "" 
                
    print('les fichiers sont les meme')
    
    
def ajouter_espace(filepath1,filepath2):
    with open(filepath1, 'r', encoding="utf-8") as file1:
        with open(filepath2,'w',encoding="utf-8") as file2:
            file2.write(file1.read().replace(' ',"   "))
            

def convertir_notes(filepath1,filepath2):
     with open(filepath1, 'r', encoding="utf-8") as file1:
        with open(filepath2,'w',encoding="utf-8") as file2:
            for line in file1:
                for cle in PERCENTAGE_TO_LETTER:
                    if PERCENTAGE_TO_LETTER[cle][0]<int(line)<PERCENTAGE_TO_LETTER[cle][1]:
                        file2.write(line.strip()+" "+cle+"\n")
        
                
    
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(comparateur("./exemple.txt","./exemple2.txt"))
    ajouter_espace("./exemple.txt","./test.txt")
    convertir_notes("./notes.txt","./lettre.txt")
