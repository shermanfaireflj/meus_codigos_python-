import tkinter as tk 




janela=tk.Tk()

janela.geometry("1200x900")
janela.config(bg='yellow')


tupla=['carambola','cereja','abacate','uva','maçã']

def mostrar ():
    
    lb_saida.config(text=tupla)


lb_entrada=tk.Label(text='sua lista de frutas ')
lb_entrada.pack()
# botao
btn_verificador=tk.Button(text='verificar', bg='grey', command= mostrar)
btn_verificador.pack()

lb_saida=tk.Label(text=f'sua lista de frutas tem: {tupla}')
lb_saida.pack()
janela.mainloop()

