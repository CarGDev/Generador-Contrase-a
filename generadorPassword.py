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
  for i in range (0,len(A)):
    try:
      numTemp = A[i]
      A[i] = CHARACTERS[numTemp]
    except:
      numTemp = numTemp -1
      A[i] = CHARACTERS[numTemp]
  return A

def run():
  valor = False
  valor2 = False
  while (valor2 != True):
    while (valor != True):
      l = int(input("Longitud de tu contraseña: "))
      if (l < 6):
        print("------Error----")
        print("Elige un numero entre 6 y 50")
      elif (l > 50):
        print("------Error----")
        print("Elige un numero entre 6 y 50")
      else:
        valor = True
    numberArray = randomListArray(l)
    numbers = selectionCharacter(numberArray)
    passwordGenerated = ""
    for i in range (len(numbers)):
      temp = numbers[i]
      passwordGenerated = passwordGenerated + temp
    print("---------------------o---------------------")
    print("Contraseña generada: " + passwordGenerated)
    print("---------------------o---------------------")
    answer = False
    while (answer != True):
      try:
        l2 = int(input("Quieres generar otra contraseña? (1 = YES, 0 = NO): "))
        if (l2 == 1):
          valor2 = False
          answer = True
          valor = False
        elif (l2 == 0):
          valor2 = True
          answer = True
        else:
          print("Elige entre 1 y 0---(1 = YES, 0 = NO)")
      except:
        print("Solo puedes seleccionar numeros")
        answer = False

  input('Press ENTER to exit')

if __name__ == '__main__':
    print('G E N E R A D O R  D E  C O N T R A S E Ñ A')
    run()