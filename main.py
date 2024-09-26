# parte 1 - Ir ao terminal e escrever pip install pillow, para baixar e instalar a biblioteca

from tkinter import*
from PIL import Image, ImageTk

# Parte 2 - Ir ao terminal e escrever pip install pygame, para baixar e instalar a biblioteca

import pygame
from pygame import mixer

# Parte 3

import os



# Cores

co0 = "#f0f3f5" # cizenta/ grey
co1 = "#feffff" # branca 
c02 = "#3fb5a3" # verde
co3 = "#ED8B16" # Laranja
co4 = "#403d3d" # preto
co5 = "#4a88e8" # Azul

# Janelas

janela = Tk ()
janela.title("")
janela.geometry('352x255')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Frames

frame_esquerdo = Frame(janela,width=150, height=150, bg=co3)
frame_esquerdo.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direito = Frame(janela,width=250, height=150, bg=co3)
frame_direito.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=404, height=100, bg=co3)
frame_baixo.grid(row=1, column=0,columnspan=3, pady=1, padx=0, sticky=NSEW)

# Frame esquerdo

img_1= Image.open('icon 1.png')
img_1 = img_1.resize((110,110))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerdo, height=130, image=img_1, compound=LEFT, padx=10, anchor='nw', font=('ivy 16 bold'), bg=co3, fg=co3)
l_logo.place(x=30, y=15)

# Play no som

def play_musica():
    rodando = Listbox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()

# Pausar musica

def pausar_musica():
    mixer.music.pause()

# Continuar musica

def continuar_musica():
    mixer.music.unpause()

# Parar musica

def Parar_musica():
    mixer.music.stop()

# Proxima musica

def proxima_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index + 1 
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    
# Deletando elementos da playlist

    Listbox.delete(0,END)
    visualizar()
    Listbox.select_set(novo_index)
    Listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando

# Musica anterior

def musica_anterior():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index - 1 
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    
# Deletando elementos da playlist

    Listbox.delete(0,END)
    visualizar()
    Listbox.select_set(novo_index)
    Listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando

# Frame direito

lista= ['Joao', 'Carlos', 'Marina','Joao', 'Carlos', 'Marina','Joao', 'Carlos', 'Marina','Joao', 'Carlos', 'Marina','Joao', 'Carlos', 'Marina']

Listbox = Listbox(frame_direito, width=22, height=10, selectmode=SINGLE, font=('arial 9 bold'), bg=co3, fg=co1)
Listbox.grid(row=0, column=0)

s = Scrollbar(frame_direito)
s.grid(row=0, column=1, sticky=NSEW)

Listbox.config(yscrollcommand=s.set)
s.config(command=Listbox.yview)


# Frame Baixo

l_rodando = Label(frame_baixo,text='Escolha uma música na lista', width=44,justify=LEFT, anchor='nw', font=('ivy 10'), bg=co1, fg=co4)
l_rodando.place(x=0, y=1)

# Botões
img_2= Image.open('icon2.png')
img_2= img_2.resize((30,30))
img_2= ImageTk.PhotoImage(img_2)
b_anterior = Button(frame_baixo, command=musica_anterior, width=40, height=40, image=img_2,  font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co1, fg=co4)
b_anterior.place(x=38, y=35)

img_3= Image.open('icon3.png')
img_3= img_3.resize((30,30))
img_3= ImageTk.PhotoImage(img_3)
b_play = Button(frame_baixo,command=play_musica, width=40, height=40, image=img_3,  font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co1, fg=co4)
b_play.place(x=84, y=35)

img_4= Image.open('icon4.png')
img_4= img_4.resize((30,30))
img_4= ImageTk.PhotoImage(img_4)
b_proximo = Button(frame_baixo, command=proxima_musica, width=40, height=40, image=img_4,  font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co1, fg=co4)
b_proximo.place(x=130, y=35)

img_5= Image.open('icon5.png')
img_5= img_5.resize((30,30))
img_5= ImageTk.PhotoImage(img_5)
b_continuar = Button(frame_baixo, command=continuar_musica, width=40, height=40, image=img_5,  font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co1, fg=co4)
b_continuar.place(x=176, y=35)

img_6= Image.open('icon6.png')
img_6= img_6.resize((30,30))
img_6= ImageTk.PhotoImage(img_6)
b_pausar = Button(frame_baixo,command=pausar_musica, width=40, height=40, image=img_6,  font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co1, fg=co4)
b_pausar.place(x=222, y=35)

img_7= Image.open('icon7.png')
img_7= img_7.resize((30,30))
img_7= ImageTk.PhotoImage(img_7)
b_stop = Button(frame_baixo, command=pausar_musica, width=40, height=40, image=img_7,  font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co1, fg=co4)
b_stop.place(x=268, y=35)


# Dentro do parenteses colocar o diretorio da pasta onde estão as musicas

os.chdir(r'')
os.chdir(r'')
musicas = os.listdir()


def visualizar():
    for i in musicas:
        Listbox.insert(END,i)

visualizar()
mixer.init()
janela.mainloop ()

