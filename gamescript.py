#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""gamescript.py, écrit par Julian Gilquin, le 27/12/2020.
Dernière mise à jour le 20/03/2021.
Ce programme permet de faire deviner à l'utilisateur le numéro, le nom ou la préfecture d'un département francais au hasard.
"""

import json
import random
import time
import os

#récupère les données depuis le fichier json
with open("DEPFRDATA.json", encoding='utf8') as f :
    data = json.load(f)

#variables pour le score du joueur
nbGoods = 0
nbRecord = 0

#fonction pour nettoyer l'ecran
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#fonction pour ajouter un point a nbGoods 
def addOnePoint() :
    global nbGoods
    nbGoods += 1
    #print("Nombres de réponses correctes à la suite :", nbGoods)

#fonction pour ajuster les points quand on perd
def stopCounts() :
    global nbGoods
    global nbRecord
    if nbGoods > nbRecord:
        nbRecord = nbGoods
    nbGoods = 0
    if nbRecord > 0:
        print("Record de bonnes réponses à la suite sur cette partie :", nbRecord)

#fonction pour deviner le num de departement
def devineNumDep() :
    randNum  = random.randint(0, 99) #numero aleatoire entre 0 et 99
    depName = data[randNum]["dep_name"]
    depNumber = str(data[randNum]["dep_number"])
    
    print("Quel est le numéro du départment", depName, "?")
    userResp = str(input()).lstrip("0") #lstrip pour enlever le zero si l'utilisateur le tape
    
    if userResp == depNumber : 
        print("CORRECT")
        addOnePoint()
    else : 
        print("FAUX !", "La bonne réponse était", depNumber)
        stopCounts()

#fonction pour deviner le departement selon le numero
def devineDepNum() : 
    randNum  = random.randint(0, 99)
    depName = data[randNum]["dep_name"]
    depNumber = str(data[randNum]["dep_number"])
    
    print("Quel départment a le numéro", depNumber, "?")
    print("Attention à bien mettre les tirets et accents si nécessaire")
    userResp = str(input())
    
    if userResp.lower() == depName.lower() : #.lower() pour eliminer les erreurs de majuscules et minuscules
        print("CORRECT")
        addOnePoint()
    else : 
        print("FAUX !", "La bonne réponse était", depName)
        stopCounts()

#fonction pour deviner la prefecture
def devinePref() : 
    randNum = random.randint(0, 99)
    depName = data[randNum]["dep_name"]
    depPref = data[randNum]["dep_pref"]
    
    print("Quelle est la préfecture du département", depName, "?")
    print("Attention à bien mettre les tirets et accents si nécessaire")
    userResp = str(input())
    
    if userResp.lower() == depPref.lower() : 
        print("CORRECT")
        addOnePoint()
    else : 
        print("FAUX !", "La bonne réponse était", depPref)
        stopCounts()

#toutes mes fonctions reunies dans une liste
listQuestions = [devineNumDep, devineDepNum, devinePref] 

#fonction principale
def main(): 

    continueGame = True #flag pour continuer de jouer
    global nbGoods
    global nbRecord

    while continueGame is True :
        cls()
        randNumQuest = random.randint(0, len(listQuestions)-1) #un numero entre zero et le nb de fonctions dans ma liste
        listQuestions[randNumQuest]() #lance la fonction dont l'index est le numero aleatoire

        #rajoute condition que nbGoods superieur a zero pour ne pas afficher le score si premiere reponse mauvaise
        if nbGoods > 0:
            print("nb bonnes réponses à la suite :", nbGoods)
        
        askToContinue = input("Une autre question ? O / N : ")
        if askToContinue.lower() == "n" :
            continueGame = False #change le flag si le joueur a dit non
            stopCounts()
            print("Merci d'avoir joué à mon jeu !")
            time.sleep( 1 )

#a rajouter dans les fichiers python (utile surtout quand on a des modules importes)
if __name__ == "__main__":
    main()
