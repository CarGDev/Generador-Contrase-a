# -*- coding: utf-8 -*-
import random
from math import ceil
import sys

CHARACTERS = ['""',
              '!',
              '#',
              '$',
              '%',
              '&',
              '(',
              ')',
              '*',
              '+',
              ',',
              '-',
              '.',
              '/',
              '0',
              '1',
              '2',
              '3',
              '4',
              '5',
              '6',
              '7',
              '8',
              '9',
              ':',
              ';',
              '<',
              '=',
              '>',
              '?',
              '@',
              'A',
              'B',
              'C',
              'D',
              'E',
              'F',
              'G',
              'H',
              'I',
              'J',
              'K',
              'L',
              'M',
              'N',
              'O',
              'P',
              'Q',
              'R',
              'S',
              'T',
              'U',
              'V',
              'W',
              'X',
              'Y',
              'Z',
              '[',
              #'\',
              ']',
              '^',
              '_',
              'a',
              'b',
              'c',
              'd',
              'e',
              'f',
              'g',
              'h',
              'i',
              'j',
              'k',
              'l',
              'm',
              'n',
              'o',
              'p',
              'q',
              'r',
              's',
              't',
              'u',
              'v',
              'w',
              'x',
              'y',
              'z',
              '{',
              '}']

def randomListArray(n):
      arrayList = [0]  * n
      for i in range(n):
        arrayList[i] = random.randint(0, len(CHARACTERS))
      return arrayList

def selectionCharacter(A):
  for i in range (len(A)):
    numTemp = A[i]
    A[i] = CHARACTERS[numTemp]
  return A

def run():
  l = int(raw_input("Lomgitud de tu contraseña: "))
  numberArray = randomListArray(l)
  numbers = selectionCharacter(numberArray)
  passwordGenerated = ""
  for i in range (len(numbers)):
      temp = numbers[i]
      passwordGenerated = passwordGenerated + temp
  print("---------------------o---------------------")
  print("Contraseña generada: " + passwordGenerated)
  print("---------------------o---------------------")

if __name__ == '__main__':
    print('G E N E R A D O R  D E  C O N T R A S E Ñ A')
    run()