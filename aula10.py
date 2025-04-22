import tkinter as tk

def troca_valor():
    atualizado = novo_texto.get()
lb.confing(text =  atualizado)

# cof.janela
janela = tk.Tk()
janela.config (background="#a7f542")
janela.geometry ("900x600")
janela.maxsize(width = 1200 , height=900)
janela.minsize(width = 400 , height= 200)
# janela.resizable(False,True)

titulo= tk.Label(text='troca de texto ', fg='white',bg='black')
LB = tk.Label(text=" informe seu Email : ", fg ='white', bg = ' green', font=30 )
LB.pack()

botao= tk.Button(text =" saida ")
botao.pack()

janela.mainloop()