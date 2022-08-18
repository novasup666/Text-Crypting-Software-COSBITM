alphabet = "abcdefghijklmnopqrstuvwxyzéè&à@ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'. /*-+=[](){}#:!\n"
def engine(mode,string,using_key):
    result = ""

    for i in range(len(string)) :
        letter = string[i]
        if letter != ','and letter != '?' :
            new_index = alphabet.find(letter)
            key_letter = using_key[i]
            key_letter_index = alphabet.find(key_letter)
            if mode == 2: key_letter_index*=-1
            new_index += key_letter_index
            new_index %= 85
            new_letter = alphabet[new_index]
            
            result+=new_letter
        else:
            result+=letter
    return result       
def convkey (in_key, in_string):
    while len(in_key) < len(in_string)+1:
        for i in range(len(in_key)):
            in_key+=in_key[i]
    return in_key
choice =int(input(('### Bienvenue dans votre utilitaire de cryptage et de déchiffrage ###\n'
       'tapez 1 pour crypter un texte; tapez 2 pour en déchiffrer un autre crypté en COSBITM26\n')))
in_string = input("Entrez la chaine de caractère (au moins 10 carachtères): \n")
key = ""
while len(key)<=7:
    key = input("Entrez votre clée (au moins 7 caractères tous différents entre eux):\n ")
using_key = convkey(key,in_string)
print(engine(choice,in_string, using_key))

