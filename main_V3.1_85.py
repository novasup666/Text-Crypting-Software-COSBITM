# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:43:49 2021

@author: Elève
"""

import math as mt

def encrypting(in_string,using_key):
    i = 0
    print('\n####   Encrypting    ###')
    for letter in in_string:
        i+=1
        if letter != ','and letter != '?' :
            N = alphabet[str(letter)]
            
            
            key_letter = using_key[i-1]
            
            key_letter_rank = alphabet[key_letter]
            
            N += key_letter_rank
            
            nbr_26 = mt.floor(N/85)
            
            new_letter_rank = N - (nbr_26*85)
            
            new_letter = alphabet_keys[new_letter_rank-1]
            
            result.append(new_letter)
        else:
            result.append(letter)
            
            
def decrypting(result, using_key):
    i = 0
    print('\n####   Decrypting    ###')
    for letter in result:
        i+=1
        if letter != ',' and letter!='?' :
            letter_rank = alphabet[letter]
            
            key_letter = using_key[i-1]
            
            key_letter_rank = alphabet[key_letter] 
            
            if key_letter_rank > letter_rank:
                letter_rank += 85              
                origin_rank = letter_rank - key_letter_rank
            else:
                origin_rank = letter_rank - key_letter_rank
            origin_letter = alphabet_keys[origin_rank-1]
            decrypte.append(origin_letter)
                                
        else:
            decrypte.append(letter)

def conv(liste):
    mot = ''
    for lettre in liste:
        mot+=lettre
    return mot
            
def convkey (in_key, in_string):
    while len(in_key) < len(in_string)+10:
        for i in range(7):
            in_key.append(in_key[i])
    return in_key

def separation (entrée):
    liste = []
    for lettres in entrée:
        liste.append(lettres)
    return liste

def filemanagement(path, mode):
        Fichier = open(path,mode, encoding=("utf-8"))
        in_string = Fichier.read()
        Fichier.close()
        return in_string
    
def keyverif():
    in_key = input("Entrez votre clé (au moins 7 caractères tous différents entre eux):\n>")
    key = separation(in_key)
    while len(key)<7:
        in_key = input("Entrez votre clé (au moins 7 caractères tous différents entre eux):\n>")
        key = separation(in_key)
    using_key = convkey(key, in_string)
    return using_key
    
alphabet = {'a' : 1,'b' : 2,'c' : 3,'d' : 4,'e' : 5,'f' : 6,'g' : 7,'h' : 8,
            'i' : 9,'j' : 10,'k' : 11,'l' : 12,'m' : 13,'n' : 14,'o' : 15,'p' : 16,
            'q' : 17,'r' : 18,'s' : 19,'t' : 20,'u' : 21,'v' : 22,'w' : 23,'x' : 24,
            'y' : 25,'z' : 26, 'é':27,'è':28,'&':29,'à':30,'@':31,
            'A':32,'B':33,'C':34,'D':35,'E':36,'F':37,'G':38,'H':39,'I':40,
            'J':41,'K':42,'L':43,'M':44,'N':45,'O':46,'P':47,
            'Q':48,'R':49,'S':50,'T':51,'U':52,'V':53,'W':54,'X':55,'Y':56,
            'Z':57,'0':58,'1':59,'2':60,'3':61,'4':62,'5':63,'6':64,'7':65,
            '8':66,'9':67,"'":68,'.':69,' ':70,'/':71,'*':72,'-':73,'+':74,
            '=':75,'[':76,']':77,'(':78,')':79,'{':80,'}':81,'#':82,':':83,'!':84,
            '\n':85}

alphabet_keys=[]
for valeur in alphabet.keys():
    alphabet_keys.append(valeur)

result = []
choice = 0
decrypte = []  #correpond a la sortie de decrypting   
nomDuFichier=""


print("#### COSBITM 85 ####\n"
      "###  Bienvenue dans votre utilitaire de cryptage et de déchiffrage ###\n\n"
      "##   Pour CHIFFRER un fichier veillez à ce qu'il soit encodé en UTF-8\n"
      "#    et qu'i soit placé dans le dossier suivant:\n"
      "#                    files/Encrypting/Input/NOMDUFICHIER.txt\n\n"
      "##   Pour DECRYPTER un fichier chiffré en COSBITM 85 veillez à l'avoir placé a cet endroit:\n"
      "#                    files/Decrypting/Input/NOMDUFICHIER.txt\n\n"
      "###  Vous trouverez le fichier resultat dans le dossier 'Output' de l'action choisie\n\n\n")

while choice != 1 and choice != 2:   
    choice =int(input(('Tapez 1 pour CHIFFRER votre fichier; tapez 2 pour le DECRYPTER:\n>')))
nomDuFichier = input("Entrez le nom avec l'extension de votre fichier:\n>")
nomFichierSortie = input("entrez le nom avec l'extension du fichier resultat:\n>")
if choice == 1:
    in_string = filemanagement(f"files/{nomDuFichier}","r")
    using_key = keyverif()
    encrypting(in_string, using_key)
    OutFichier = open(f'files/{nomFichierSortie}','w',encoding=("utf-8"))
    OutFichier.write(conv(result))    
    
elif choice==2 :
    in_string = filemanagement(f"files/{nomDuFichier}", "r")
    using_key = keyverif()
    decrypting(in_string, using_key)
    OutFichier = open(f'files/{nomFichierSortie}','w',encoding=("utf-8"))
    OutFichier.write(conv(decrypte))

OutFichier.close()






























