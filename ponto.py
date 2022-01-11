#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.geometry('1x1')

def horas_result():
    '''
    Análise breve das horas trabalhadas. O argumento 'caminho' diz o nome do arquivo, considerando que ele está salvo na mesma pasta.
    '''
    # Importando dados
    df = pd.read_csv('./pontos_marcados.txt',delimiter=',')

    # Transformando os dados para o tipo correto. De 'string' para 'timedelta'.
    df['horas_trabalhadas'] = pd.DatetimeIndex(df.saida) - pd.DatetimeIndex(df.entrada)
    df['data'] = pd.to_datetime(df.data)
    df['entrada'] = pd.DatetimeIndex(df.entrada).time
    df['saida'] = pd.DatetimeIndex(df.saida).time

    # Criando coluna de horas excedentes ou faltantes.
    df['horas_por_dia'] = timedelta(hours=7)
    df['horas_excedentes_faltantes'] = df.horas_trabalhadas - df.horas_por_dia    

    total = df.horas_excedentes_faltantes.sum()
    b = timedelta()

    # Definindo o texto na janela popup.
    if total < b:
        base = timedelta(days=-1,hours=24)
        resultado = base - total
        msg = 'Faltam {} horas.'.format(str(resultado))
        MsgBox = tk.messagebox.showinfo("Folha", msg)
        if MsgBox == 'ok':
            root.destroy()
        else:
            root.destroy()

    else:
        msg = 'Você excedeu {} horas.'.format(str(total))
        MsgBox = tk.messagebox.showinfo("Folha de pontos", msg)
        if MsgBox == 'ok':
            root.destroy()
        else:
            root.destroy()


# In[2]:


from datetime import datetime,time,timedelta
import os.path

def ponto():
    '''
    Esta função pega a data e hora do sistema e salva em um arquivo .txt na pasta atual.
    '''
    # Pegando data e hora do sistema.
    data = str(datetime.date(datetime.now())) # data atual
    hora = str(datetime.time(datetime.now())) # hora atual
    
    # Verificando se o arquivo ja existe no diretorio.
    if os.path.isfile('./pontos_marcados.txt') == True:
        with open('pontos_marcados.txt', 'r+') as f: 
            conteudo = f.readlines()                 
            check = conteudo[-1]                     
            
            # Caso você esteja marcando o segundo ponto novamente no dia.
            if check[:10] == data and len(check) >= 40:                   
                old_lines = conteudo[:-1]
                new_line = [check[:-16] + ',' + hora]
                lines = old_lines + new_line
                f.truncate(0)
                f.seek(0)
                for i in lines:
                    f.write(i)
                    
            # Caso seja o segundo ponto do dia.        
            elif check[:10] == data:
                f.write(',')                        
                f.write(hora)
            
            # Caso seja o primeiro ponto do dia.
            else:
                f.write('\n')
                f.write(data)
                f.write(',')
                f.write(hora) 
    else:
        # Criando arquivo.
        with open('pontos_marcados.txt', 'x') as f:
            f.write('data,entrada,saida')


# In[4]:


ponto()


# In[5]:


horas_result()

