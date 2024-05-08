# Instalar IDE(Vscode) e o Python
# Instalar a biblioteca pyautogui
# pip install pyautogui
# Instalar a biblioteca pyperclip
# pip install pyperclip

import pyautogui
import time

a = int()

print("_______________________________________________________________________________________________________________")
print("1º Posisione as janelas: No Excel cliando na primeira celula A1 da Plan1") 
print("2º - No SCA 4 clique no primeiro nome dos faltosos, deixando selecionado!")
print("_______________________________________________________________________________________________________________")
print(" ")
numero = 1 + int(input('Digite a quantidade de alunos que faltou: '))
print("20 segundos para iniciar.")

for a in range(0, 20):
    time.sleep(1)
    print(a)

for i in range(1, numero): 
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c') 
    time.sleep(1) 
    pyautogui.press(['down'])
    time.sleep(2) 
    # No Windows 7 foi necesssario dar dois Alt + Tab para dar certo como se fosse um
    pyautogui.keyDown('alt') 
    pyautogui.hotkey('tab', 'tab')
    pyautogui.keyUp('alt')
    time.sleep(2) 
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1) 
    pyautogui.press(['down'])
    time.sleep(2)
    # No Windows 7 foi necesssario dar dois Alt + Tab para dar certo como se fosse um
    pyautogui.hotkey('alt', 'tab')

pyautogui.alert('Processo Finalizado com Sucesso')