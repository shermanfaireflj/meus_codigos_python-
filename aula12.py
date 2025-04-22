from tkinter import *

def encontrar_maior_palavra():
    # Coleta todas as palavras das entradas usando loop
    palavras = [entry.get() for entry in entradas]
    if (palavras):  # Verifica se todos os campos estão preenchidos
        maior = max(palavras, key=lambda x: len(x))
        resultado.config(text=f"Maior palavra: {maior} ({len(maior)} letras)", fg="green")
    else:
        resultado.config(text="Preencha todos os campos!", fg="red") 
# Configuração da janela
janela = Tk()
janela.title("Maior Palavra")

# Lista para armazenar as entradas
entradas = []

# Cria 5 entradas com loop
Label(janela, text="Digite 5 palavras:").grid(row=0, column=0, pady=10)

for i in range(5):
    entry = Entry(janela, width=20)
    entry.grid(row=i+1, column=0, padx=10, pady=2)
    entradas.append(entry)  # Adiciona cada entrada à lista

# Botão e resultado
Button(janela, text="Calcular", command=encontrar_maior_palavra).grid(row=6, column=0, pady=10)
resultado = Label(janela, text="", font=('Arial', 10))
resultado.grid(row=7, column=0)

janela.mainloop()
