import caesar as ca
import vigenere as vi
import afin as af
from afin import afinCypher
import numpy as np
import nltk
import re

alpha = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
afin_key = [7, 15]
afincypher = afinCypher(alpha)
#Tengo mis dudas sobre si dejar esta función aqui o si meterla en las funciones 
#encrypt para que limpie cada cosa, si tienen ideas son bienvenidas

def cleanTxt(tx):
    t = tx.upper()
    t = t.replace('Á','A')
    t = t.replace('É','E')
    t = t.replace('Í','I')
    t = t.replace('Ó','O')
    t = t.replace('Ú','U')
    t = t.replace('Ü','U')
    remover = [' ','.',',','(',')','1','2','3','4','5','6','7','8','9','0']
    
    for w in remover:
        t = t.replace(w, '')
    return t

#Funciones para llamar al metodo de encriptacion que querramos, la idea es que por cada vez que el usuario elija
#encriptar o decriptar borre lo que esta en el .txt y lo reescriba para asegurarnos que funciona
#tambien hay que hacer lo de las distribuciuones de frecuencias y probabilidades

def caesarInit():

    mensaje = input("Ingrese el mensaje que desea encriptar: ")
    paso = int(input("Ingrese la cantidad de letras trasladar: "))

    print("\nMENSAJE ENCRIPTADO EN CAESAR: \n")

    mensaje=cleanTxt(mensaje)
    mCifrado = ca.encryptC(mensaje, paso)
    print(mCifrado, "\n") 

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    mDes=ca.decryptC(mCifrado, paso)
    print(mDes, "\n")
    
    
def afinInit():

    mensaje = input("Ingrese el mensaje que desea encriptar: ")

    print("\nMENSAJE ENCRIPTADO EN AFIN: \n")

    mensaje=cleanTxt(mensaje)
    mCifrado = afincypher.encryptA(afin_key[0], afin_key[1], mensaje)
    print(mCifrado, "\n") 

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    mDes=afincypher.decryptA(afin_key[0], afin_key[1], mCifrado)
    print(mDes, "\n")
    

def vigenereInit():
    
    text = input("Ingrese el mensaje que desea encriptar: ")
    clave = input("Ingrese la cantidad de letras trasladar: ")
    print("\nMENSAJE ENCRIPTADO EN AFIN: \n")
    text=cleanTxt(text)
    mCifrado = vi.encryptV(text, clave)
    print(mCifrado) 
    #encryptV()

    input("PRESIONA ENTER PARA DECRIPTAR\n")
    mDes= vi.decryptV(mCifrado, clave)
    print(mDes)
    print("")
    #decryptV()
    
def distribucion():
    mensaje = input("Ingrese un texto Cifrado o descrifrado: ")
    mensaje = cleanTxt(mensaje)
    dist = {
        'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'Ñ':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0
    }
    for i in mensaje:
        for j in alpha:
            if i==j:
                dist[i]=dist.get(i) + 1
    
    for i in dist:
        dist[i]= float(dist.get(i)/len(mensaje))

    return dist

def BrutoC():
    cryptictext1 = "WDSFSDALALIHKXKWUNWFUASLISKSVWLUAXKSKUKAIMHYKSESLLWTSLSWFWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFDHLVALMAFMHLLAETHDHLWFNFDWFYNSBWVWMWKEAFSVHQDNWYHWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFWFDHLUKAIMHYKSESLQVWWLMSESFWKSWLMSTDWUWKNFSKWDSUAHFQHTMWFWKWDMWPMHIDSFHDSAVWSXNFVSEWFMSDWLJNWFHMHVSLDSLDWMKSLSISKWUWFUHFDSEALESXKWUNWFUASWFDHLMWPMHLLAFHJNWSDYNFSLSISKWUWFESLSEWFNVHJNWHMKSLUHFMSFVHDSLLAYFHLVWDMWPMHUAXKSVHQHKVWFSFVHDHLVWESQHKSEWFHKXKWUNWFUASIHVWEHLWLMSTDWUWKUHFBWMNKSLSUWKUSVWJNWDWMKSUHKKWLIHFVWSUSVSLAYFHWDSFSDALALLWUHEIDWMSUHFDSTNLJNWVSVWISDSTKSLXKWUNWFMWLUHEHSKMAUNDHLQIKWIHLAUAHFWLLASVWESLUHFHUWEHLHLHLIWUZSEHLVWSDYNFSISDSTKSJNWVWTSSISKWUWKWFWDEWFLSBWEWBHKJNWEWBHKWDKWLMHWLUNWLMAHFVWAFMNAUAHFLWYNFNFWLMNVAHLHTKWMWPMHLVWDVASKAHWDISALVWWFKAJNWXHFMSFADDHDSENWLMKSMHESVSVLHFDHLWBWEIDSKWLVWVAUZHVASKAHINTDAUSVHLVNKSFMWNFSLWESFSUAFUNWFMSQVHLEADLWALUAWFMHLVAWUAFNWÑWDWMKSLWFMHMSDDSXKWUNWFUASVWDSLDWMKSLWFUSLMWDDSFHWLSIKHPAESVSEWFMWDSJNWLAYNW"
    cryptictext= cryptictext1.lower()
    for i in range(0,26):
        plain_text = ca.decryptC(cryptictext, i)
        if i == 19:
            print("La clave resultante es {}, el mensaje desencriptado es: {}".format(i, plain_text))
            print("")
