# # atv.1
# import tkinter as tk 
# janela= tk.Tk()

# def imprime_lista():
#     lista=["vinih","tiaguh","erikson","erika"]
    
#     for nome in lista:
#         lb_nome=tk.Label(text=nome,font=60)
        
#         lb_nome.pack()
    
# imprime_lista()

# janela. mainloop()

# atv.2

# import tkinter as tk 

# janela= tk.Tk()

# def cadasrar():
# numero_digitado=

# lb_entrada=tk.Label(text=" digite 5 numeros    ")
# lb_entrada.grid(row=1,column=2,pady=20,padx=20)

# entrada_user = tk.Entry()

# numeros=int(input("digite 5 numeros é dscubra a média deles juntos !!! "))


# janela.mainloop()


# atv.3

import tkinter as tk
janela  = tk.Tk( bg=' dark blue ')
janela.title=("escreva suas palavras e veja as organizadas !" )
janela.confing(bg='')

lista_palavras = []

def palavras ():
insert_palavra =

insert_palavra = nova_palavra
insert_palavra(comand= lista_palavras)


def cadastrar_palavra():
nova_palavra = enrty_palavra.get()
lista_palavras.append(nova_palavra)




# entrada do usuario

lb_instrucao=tk.Label(text=' forme 5 palavras ')

enrty_palavra= tk.Entry()

enrty_palavra.pack()

# botao para inserir palavras na lista 

bt_enviar=tk.Button(text=' enviar ', command = lista_palavras, bg=' blue  ' , fg= 'black ' )

bt_enviar.pack()


janela.mainloop()





# # atv.4 


# def ex4():
#     janela = tk.Toplevel()
#     janela.title("Exercício 4")
#     numeros = []
    
#     def adicionar():
#         try:
#             num = int(entrada.get())  
#             numeros.append(num)
#             entrada.delete(0, tk.END)
            
#             if len(numeros) == 10:  # Aguarda 10 números
#                 pares = [n for n in numeros if n % 2 == 0]  # Filtra pares
#                 tk.Label(janela, text="Números pares:").pack()
#                 for p in pares:
#                     tk.Label(janela, text=p).pack()
#                 btn.config(state=tk.DISABLED)
#         except ValueError:
#             messagebox.showerror("Erro", "Digite um número inteiro!")
    
#     # Interface
#     tk.Label(janela, text="Digite 10 números:").pack()
#     entrada = tk.Entry(janela)
#     entrada.pack()
#     btn = tk.Button(janela, text="Adicionar", command=adicionar)
#     btn.pack()














































# atv.3






# titulo= tk.Label(text='lista de nomes  ', fg='white',bg='black')

# LB = tk.Label(text=" insira 5 nomes  : ", font=30 )
# LB.pack()






# nomes= ["tiaguh "," vinih", " erika ", " sherman ", "erik" ]

# for nome in nomes (nome,+1):
#     print( )