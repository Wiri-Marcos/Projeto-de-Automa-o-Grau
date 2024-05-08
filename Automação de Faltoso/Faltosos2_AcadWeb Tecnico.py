# Instalar IDE (Vscode) e o Python
# Instalar a biblioteca pyautogui
# pip install pyautogui
# Instalar a biblioteca pyperclip
# pip install pyperclip

import pyautogui
import time
import pyperclip

a = int() # Variavel do Conometro e função

print("____________________________________________________________________________________________________________________________________")
print("1° Abra o Acad Web, Faço o Login e selecione todos os alunos.")
print("2° Crie uma planilha com todos os nomes dos alunos que faltaram e clique no primeiro nome da ordem.")
print("3° Após definir o número de alunos que faltaram, Clique sobre o campo Observações e depois novamente ")
print("no primeiro nome da lista.")
print("____________________________________________________________________________________________________________________________________")
print(" ")

codigoobs =  int(input ('Digite o Codigo da Observação desejada: ' )) 
print(" ")

print("Coloque a menssagem de Faltoso: ")
textofaltosos = input(''' ''')
print("____________________________________________________________________________________________________________________________________")
print(" ")

numero = 1 + int(input('Digite a quantidade de alunos que faltou: '))
print("20 segundos para iniciar")


for a in range(0, 20):  # Conometro de iniciação do Processo
    time.sleep(1)
    print(a)

for i in range(1, numero):
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c')  # Processo de Copiar a informação
    time.sleep(2) 
    pyautogui.press(['down'])  # Seleciona a proxima celula da planilha
    time.sleep(2) 
    pyautogui.hotkey('alt', 'tab') # Alterna entre janelas do sistema
    time.sleep(2)
    pyautogui.click(14, 146)  # Clacar na guia ALUNOS
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v') # Cola a informação
    time.sleep(2)
    pyautogui.hotkey('enter') # Selecionar o nome da busca
    time.sleep(2)
    pyautogui.click(343, 144)  # Clcar na guia OBSERVAÇÕES
    time.sleep(2)
    pyautogui.click(1057, 698)  # Clcar na guia INSERIR 
    time.sleep(1)
    pyautogui.hotkey('tab')
   
    pyperclip.copy(codigoobs)

    time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.hotkey('tab')

    pyperclip.copy(textofaltosos) # Aplicando informação na Area de Aransferencia

    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(3)
    pyautogui.click(796, 533)  # Clcar no botão salvar
    time.sleep(3)
    pyautogui.hotkey('alt','tab')

    if i == 1:  
        time.sleep(2)
        pyautogui.click(454, 152)  # Clcar na guia OBSERVAÇÕES

pyautogui.alert('Processo Finalizado com Sucesso!')

print("Finalizado com Sucesso")