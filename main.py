from tkinter import *
from tkinter import ttk
from game import game_do_peixinho

lista_comorbidades = ['Comorbidade1', 'Comorbidade2', 'Comorbidade3', 'Comorbidade4']
lista_tempos = ['1:00','1:30','2:30', '4:00', '5:00']
lista_dificuldade = ['Fácil', 'Médio', 'Difícil']
lista_forca = ['50', '100', '150', '200', '250', '300']
portas_arduino = ['COM1','COM2', 'COM3','COM4','COM5','COM6']


def enviar_dados():
    nome = str(entrada_nome_paciente.get())
    idade = int(entrada_idade_paciente.get())
    comorbidade = str(entrada_comorbidade_paciente.get())

    tempo = str(entrada_tempo_do_jogo.get())
    dificuldade = str(entrada_dificuldade_do_jogo.get())
    forca = int(entrada_forca_do_jogo.get())

    porta = porta_arduino.get()
    frequencia = int(frequencia_arduino.get())

    game_do_peixinho(tempo, dificuldade, forca, porta, frequencia)

    janela.destroy()

    return nome, idade, comorbidade, tempo, dificuldade, forca, porta, frequencia


#----------------- Criação da janela -----------------
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
entrada_nome_paciente = ttk.Entry(janela, justify=LEFT,)
entrada_nome_paciente.place(width=228, height=25, x=145, y=154)
nome_paciente_padrao = "Paciente 1"
entrada_nome_paciente.insert(0, nome_paciente_padrao)


entrada_idade_paciente = ttk.Entry(janela, justify=LEFT)
entrada_idade_paciente.place(width=228, height=25, x=145, y=190)
idade_paciente_padrao = "0"
entrada_idade_paciente.insert(0, idade_paciente_padrao)

entrada_comorbidade_paciente = ttk.Combobox(janela, justify=LEFT, values=lista_comorbidades)
entrada_comorbidade_paciente.place(width=132, height=25, x=240, y=230)
entrada_comorbidade_paciente_padrao = "Comorbidade1"
entrada_comorbidade_paciente.insert(0, entrada_comorbidade_paciente_padrao)


#Entradas -- Jogo
entrada_tempo_do_jogo = ttk.Combobox(janela, justify=LEFT, values=lista_tempos)
entrada_tempo_do_jogo .place(width=180, height=25, x=155, y=327)
tempo_de_jogo_padrao = '5:00'
entrada_tempo_do_jogo.insert(0, tempo_de_jogo_padrao)

entrada_dificuldade_do_jogo = ttk.Combobox(janela, justify=LEFT, values=lista_dificuldade)
entrada_dificuldade_do_jogo .place(width=122, height=25, x=212, y=369)
dificuldade_do_jogo_padrao = 'Facil'
entrada_dificuldade_do_jogo.insert(0, dificuldade_do_jogo_padrao)

entrada_forca_do_jogo = ttk.Combobox(janela, justify=LEFT, values=lista_forca)
entrada_forca_do_jogo.place(width=195, height=25, x=138, y=407)
forca_do_jogo_padrao = '200'
entrada_forca_do_jogo.insert(0, forca_do_jogo_padrao )


#Entradas -- Arduino
porta_arduino = ttk.Combobox(janela, justify=LEFT, values=portas_arduino)
porta_arduino.place(width=175, height=25, x=138, y=519)
porta_arduino_padrão = 'COM3'
porta_arduino.insert(0, porta_arduino_padrão)

frequencia_arduino = ttk.Combobox(janela, justify=LEFT)
frequencia_arduino.place(width=103, height=25, x=210, y=562)
frequencia_arduino_padrao = '0872'
frequencia_arduino.insert(0, frequencia_arduino_padrao)

#Botão
botao2 = Button(janela, text="Jogar", relief='raised', command=lambda:enviar_dados())
botao2.place(width=100, height=33, x=900, y=562)

janela.mainloop()