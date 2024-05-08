import pyautogui
import time
#pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis
print('Clique para obtert a Posicione o MOUSE')
time.sleep(5)
x, y = pyautogui.position()
resu = x, y
print ("Posicao atual do mouse:")
print ("x = "+str(x)+" y = "+str(y))

#retorna Truee se x & y estiverem dentro da tela
print ("\nEsta dentro da tela?")
resp = pyautogui.onScreen(x, y)
print (str(resp))
print (resu)
time.sleep(10)

#Posicao Aluno AcadWeb - mouse:
#x = 55 y = 148

#Posicao observação AcadWeb - mouse:
#x = 286 y = 152

#Posicao Inserir Observação - mouse:
# x = 1156 y = 814

#Posicao Observações botão Salvar mouse:
#x = 828 y = 617