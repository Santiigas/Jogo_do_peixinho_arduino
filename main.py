from tkinter import *
from tkinter import ttk
import string
from game import game_do_peixinho

lista_comorbidades = ['Comorbidade1', 'Comorbidade2', 'Comorbidade3']
lista_tempos = ['1:00','1:30','2:30', '4:00', '5:00']
lista_dificuldade = ['Facil', 'Medio', 'Dificil']
lista_forca = ['100', '200', '300']
portas_arduino = ['COM1','COM2', 'COM3','COM4','COM5','COM6']


def pegarDadosParaJogo():
    nome = entrada_nome_paciente.get()
    idade = int(entrada_idade_paciente.get())
    comorbidade = entrada_comorbidade_paciente.get()

    tempo = str(entrada_tempo_do_jogo.get())
    dificuldade = str(entrada_dificuldade_do_jogo.get())
    forca = int(entrada_forca_do_jogo.get())

    porta = porta_arduino.get()
    frequencia = int(frequencia_arduino.get())



#criação da janela
janela = Tk()
janela.title("Jogo do peixinho com arduino")
janela.geometry("1040x700+155+70")
janela.wm_resizable(width=False, height=False)

#importação da imagem de fundo
fundo_imagem = PhotoImage(file="imagens/template.png")

#Label
labelfundo = Label(janela, image=fundo_imagem)
labelfundo.place(x=0, y=0)

#Entradas -- Paciente
entrada_nome_paciente = ttk.Entry(janela, justify=LEFT)
entrada_nome_paciente.place(width=228, height=25, x=145, y=154)

entrada_idade_paciente = ttk.Entry(janela, justify=LEFT)
entrada_idade_paciente.place(width=228, height=25, x=145, y=190)

entrada_comorbidade_paciente = ttk.Combobox(janela, justify=LEFT, values=lista_comorbidades)
entrada_comorbidade_paciente.place(width=132, height=25, x=240, y=230)

#Entradas -- Jogo

entrada_tempo_do_jogo = ttk.Combobox(janela, justify=LEFT, values=lista_tempos)
entrada_tempo_do_jogo .place(width=180, height=25, x=155, y=327)

entrada_dificuldade_do_jogo = ttk.Combobox(janela, justify=LEFT, values=lista_dificuldade)
entrada_dificuldade_do_jogo .place(width=122, height=25, x=212, y=369)

entrada_forca_do_jogo = ttk.Combobox(janela, justify=LEFT, values=lista_forca)
entrada_forca_do_jogo.place(width=195, height=25, x=138, y=407)

#Entradas -- Jogo

porta_arduino = ttk.Combobox(janela, justify=LEFT, values=portas_arduino)
porta_arduino.place(width=175, height=25, x=138, y=519)

frequencia_arduino = ttk.Combobox(janela, justify=LEFT)
frequencia_arduino.place(width=103, height=25, x=210, y=562)

#Botão

botao1 = Button(janela, text="Salvar", relief='raised', command=lambda:pegarDadosParaJogo())
botao1.place(width=100, height=33, x=780, y=562)

botao2 = Button(janela, text="Jogar", relief='raised', command=lambda:game_do_peixinho())
botao2.place(width=100, height=33, x=900, y=562)



janela.mainloop()