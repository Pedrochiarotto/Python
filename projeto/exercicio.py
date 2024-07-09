import pyautogui
import time

#pyautogui.click - clicar com o mouse
#pyautogui.write - Escrever um texto
#pyautogui.press - Pressionar uma tecla
#pyautogui.hotkey - Combinacao de teclas
#pyautogui.scroll - Rolar a tela para cima ou para baixo 

# É necessario ter pause entre os comandos para que a linguagem nao seja mais rapida que o processo 
pyautogui.PAUSE = 0.5

# Passo 1 - entrar no sistema
#abrir navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2 - Fazer login
pyautogui.click(x=678, y=374)
pyautogui.write("phchiarotto@gmail.com")
pyautogui.press("tab")
pyautogui.write("MinhaSenha")
pyautogui.press("enter")

time.sleep(3)

# Passo 3 - importar a base de dados

import pandas as pd

tabela = pd.read_csv("produtos.csv")

#Passo 4 - Cadastrar o produto
for linha in tabela.index: 

    pyautogui.click(x=562, y=256)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha,'tipo'])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(1000) 

# Passo 5 - Repetir para todos os produtos

