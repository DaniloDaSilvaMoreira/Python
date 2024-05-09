# Passo a passo Projeto

# 1. Abrir o sistem da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login


 # instalar dependencia python (automatização): pip install pyautogui

import pyautogui 
import time

pyautogui.PAUSE = 0.5

    # pyautogui.click -> clicar com mouse
    # pyautogui.write -> escrever um texto
    # pyautogui.press -> pressionar uma tecla do teclado
    # pyautogui.hotkey -> apertar um conjunto de teclas

 #abrir o navegador
pyautogui.press("win")
time.sleep(1)
pyautogui.write("Chrome")

pyautogui.press("enter")
time.sleep(1)

pyautogui.click(x=419, y=309)
time.sleep(2)

 # Entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que demore açguns segundos para carregar o site
pyautogui.click(x=621, y=30)

time.sleep(2)
pyautogui.click(x=880, y=369)

pyautogui.write("danilo@gmail.com")
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write("123")

time.sleep(1)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela) 

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])

    pyautogui.click(x=567, y=256)

    time.sleep(1)

    pyautogui.write(codigo)

    pyautogui.press("tab")

    time.sleep(1)
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    time.sleep(1)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)    
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)


# 2. Fazer login
# 3. abrir/importar a base de dados de produtos para cadastrar
# 4. cadastrar um produto
# 5. Repetir para todos os produtos