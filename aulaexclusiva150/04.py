# import tkinter as tk 

    
# def mais():
#     n1=int( lb_entrada.get())
#     n2=int( lb_entrada2.get())
#     resultado=n1+n2
#     lb_saida.config(text= resultado )
    

    
# def menos():
#     n1=int( lb_entrada.get())
#     n2=int( lb_entrada2.get())
#     resultado=n1-n2
#     lb_saida.config(text= resultado )
    
    
    
    
# def multiplicacao():
#     n1=int( lb_entrada.get())
#     n2=int( lb_entrada2.get())
#     resultado=n1*n2
#     lb_saida.config(text= resultado )
    
    
    
# def divisao():
#     n1=int( lb_entrada.get())
#     n2=int( lb_entrada2.get())
#     resultado=n1/n2
#     lb_saida.config(text= resultado )
    
    
    
# # janela
# janela= tk.Tk()
# janela.title( ' janela ' )
# janela.config(bg='#EA4335')
# # janela.geometry('930x700')

# # texto

# lb_ent =tk.Label(text='calculadora' )
# lb_ent.pack()

# # entrada

# lb_entrada=tk.Entry()
# lb_entrada.pack()




# # entrada2 
# lb_entrada2=tk.Entry()
# lb_entrada2.pack()




# # botao_mais
# botaoMais=tk.Button(text='+',command = mais)
# botaoMais.pack(side='left',pady= 4 ,padx= 6)



# # botao_Menos
# botaoMenos=tk.Button(text='-',command = menos)
# botaoMenos.pack(side='left',pady= 4,padx= 6)


# # divisao
# botaoDividir=tk.Button(text='/',command = divisao)
# botaoDividir.pack(side='left',pady= 4 ,padx= 6)

# # multiplicação

# botaomultiplicar=tk.Button(text='*',command = multiplicacao )
# botaomultiplicar.pack(side='left',pady= 4,padx=6)


# # text 
# lb_saida=tk.Label(text= ' ')
# lb_saida.pack(side='bottom')



# janela.mainloop()

import tkinter as tk 

janela=tk.Tk()


pilha=[ ]

contador= 0

while contador <5 :
    tk.Label(text='informe um numero : ').pack()
    pilha_entrada  = tk.Entry()
    pilha_entrada .pack()
    pilha.append(pilha_entrada.get())
    contador += 1
    
janela.mainloop()
