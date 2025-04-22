import tkinter as tk 
# funcão
def verificar_placa():
    
    
    
    res=' '
    
    numero_digitado=lb_entrada.get()
    numero=int(numero_digitado)
    
    if(numero == 0 or numero == 1 ):
        res="nâo pode circular na segunda-feira"
        
    elif numero == 2 or numero == 3 :
        res="não pode circular na terça- feira "
    
    elif numero== 4 or  numero == 5 :  
        res = " Não pode circular na quarta- feira "
    
    elif numero == 6 or numero == 7 :
        res = "Não pode circular na quirta-feira "
        
    elif numero == 8 or numero ==  9 :
        res= "Não pode circular na sexta-feira "
        
    else:
        res = "Não pode circular "
        
        
        
    resultado.config(text=res)






# janela


janela= tk.Tk()
janela.config( bg = '#E37400')
janela.geometry ("900x600")
# janela.config (resultado)


# declação da  imagem

logo =tk.PhotoImage(file='imagem\placa.png' )
logo=logo.subsample(10,10 )
lb_logo=tk.Label(janela , image= logo , bg='#E37400' )
lb_logo.grid(row = 0 , column = 0  )

# titulo

titulo= tk.Label(text= "informe a numeração da placa ", bg= '#E37400')
titulo.grid()

# entrada

lb_entrada= tk.Entry()
lb_entrada.grid()


# botao 
botao = tk.Button (text='verificar ', command=verificar_placa , font=('1942 repot', 15 ) , bg = 'green' )
botao.grid()

resultado= tk.Label(text=' ', )
resultado.grid()

janela.mainloop()


