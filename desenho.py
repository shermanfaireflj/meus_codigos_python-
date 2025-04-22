import turtle  # Importando a biblioteca Turtle
print(" ESCOLHA UMA DAS OPÇÕES ")
# Criando a tela do desenho
tela = turtle.Screen()
tela.bgcolor("  darkg_green ")  # Cor do fundo
tela.title("Desenhando com Turtle")  # Título da janela
print(" Figuras plana ")
# Criando o objeto Turtle
desenho = turtle.Turtle()
desenho.speed(2)  # Velocidade do desenho

# Perguntando ao usuário qual forma desenhar
print("Escolha a forma geométrica para desenhar:")
print("1 - Quadrado")
print("2 - Triângulo")
print("3 circulo")

opcao = int(input("Digite o número da opção desejada: "))
tamanho = int(input("Digite o tamanho do lado: "))

# Estrutura condicional para desenhar a forma escolhida
if opcao == 1:
    for _ in range(4):  # Quadrado tem 4 lados
        desenho.forward(tamanho)  # Anda para frente
        desenho.right(90)  # Gira 90 graus para a direita
elif opcao == 2:
    for _ in range(3):  # Triângulo tem 3 lados
        desenho.forward(tamanho)  # Anda para frente
        desenho.right(120)  # Gira 120 graus para a direita
elif opçao == 3:
    for_in range(0):
        desenho.right()
else:
    print("Opção inválida! Escolha 1 ou 2.")
    

# Finaliza o desenho
turtle.done()