#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
def comparateur(filepath1,filepath2):
    with open(filepath1, 'r', encoding="utf-8") as file1:
        with open(filepath2,'r',encoding="utf-8") as file2:
            for line1 in enumerate(file1):
                line2=file2.readline()
                if line2!=line1:
                    break
                return line2,line1
# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(comparateur(r"C:\Users\youne\Documents\GitHub\c03-ch8-exercices-Younes51-1\exemple.txt",r"C:\Users\youne\Documents\GitHub\c03-ch8-exercices-Younes51-1/exemple1.txt"))
