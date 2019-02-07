# Code by: Martin Calderon Sanchez 
# Team:
# Melannie Torres
# Martín Calderón
# Gerardo Saldaña


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:50:32 2019

@author: martin
"""
import fileinput




def Create_tableu(key):
    Letter = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = Letter
    

    for test in key:
    	table = table.replace(test,'')
	
    Char_Tableu = key + table
    
    Cont = 0
    #Create a matrix
    Int_Tableu = [[0 for x in range (5)] for y in range (5)]	
    for i in range (5):
        for j in range (5):
            Int_Tableu [i][j] = Char_Tableu[Cont]
            Cont += 1
	       
    return Int_Tableu


def Fill(phrase,Basic_Tableu,Selection):
    Enc_array1 = []
    Enc_array2 = []
    Dec_array1 = []
    
    for word in phrase:
        if (' ' in word):
            Selection = True
        word = word.replace(' ','')
        
        for letter in word:
            i, j = Find_Position(letter, Basic_Tableu)
        
            if (i == -1):
                return Enc_array1, Enc_array2, Dec_array1, Selection
            else:
                Enc_array1.append(i)
                Enc_array2.append(j)
                Dec_array1.append(i)
                Dec_array1.append(j)
    return Enc_array1, Enc_array2, Dec_array1, Selection
        
def Find_Position(letter, Basic_Tableu):
     i = 0
     j = 0
     
     if (letter == ' '):
         return -1,-1
     
     while (letter != Basic_Tableu[i][j]):
         i += 1
         if (i == 5):
             i = 0
             j += 1
         if (j==5):
             return -1,-1
     return i,j

def Encrypt(Enc_array1,Enc_array2,Basic_Tableu):
    
    List = Enc_array1 + Enc_array2
    Result = ''
    
    Pairs = int(len(List)/2)
    for shift in range(Pairs):
        i = List.pop(0)
        j = List.pop(0)
        letter = Basic_Tableu [i][j]
        Result += letter
    return Result
    
def Decrypt(Dec_array1,Basic_Tableu):
    Result = ''
    half = int(len(Dec_array1)/2)
    
    for Shift in range(half):
        i = Dec_array1[Shift]
        j = Dec_array1[Shift + half]
        
        String = Basic_Tableu[i][j]
        Result += String
    return Result
    
 
        
def main():

    file_input = fileinput.input()
    key = file_input[0]
    
    key = key.replace('\n','')
    
    Basic_Tableu=Create_tableu(key)
    
    Selection = False 
    
    phrase = file_input
    Enc_array1, Enc_array2, Dec_array1, Selection = Fill(phrase, Basic_Tableu, Selection)
    
    if (Selection):
        Result1 = Encrypt(Enc_array1,Enc_array2,Basic_Tableu)
        print (Result1)
        
    else:
        Result2 = Decrypt(Dec_array1,Basic_Tableu)
        print(Result2)
            


if __name__ == "__main__":
	main()
    
