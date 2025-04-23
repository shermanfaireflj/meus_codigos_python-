import tkinter as tk 




janela=tk.Tk()

janela.geometry("1200x900")
janela.config(bg='yellow')


tupla=['carambola','cereja','abacate','uva','maçã']

def mostrar ():
    lb_saida.config(text=tupla(3))


lb_entrada=tk.Label(text=' lista de frutas ')
lb_entrada.grid(row= 1, column=36)

btn_verificador=tk.Button(text='verificar', bg='grey', command= mostrar)
btn_verificador.grid(row=3, column=36)

lb_saida=tk.Label()
lb_saida.grid(row=2, column=36)
# botao
janela.mainloop()

