
# atv.1
import tkinter as tk 
janela= tk.Tk()

pilha=[]

nova_pilha=[' ',' ',' ',' ',' ']
def add_numero():
    numero_novo= usuario_enrty.get
    pilha.append(numero_novo)
tirar o text e colocar uma variavel , dps add a variavel ali 
    if len(pilha) == len(nova_pilha):
        lb_verificador.config(text=f'A pilha é : {pilha}').pack()
        



janela_title =tk.Label(text= " sua pilha  ")
janela.config(background='green')
janela_title.pack()
janela.geometry("1200x900")
# botao

usuario_enrty= tk.Entry ()
usuario_enrty.pack()

btn=tk.Button(text= "ADICIONAR ", command=add_numero)
btn.pack()
btn.config(bg='blue' , fg= 'white') 
lb_verificador=tk.Label(text=' ')
lb_verificador.pack()
janela.mainloop()


# atv2

# import tkinter as tk 
# janela_principal= 