# Aprendendo Python
    # Função print: imprime mensagens 
print("Hello Word!")

    # Função input: apresentação de textos, quando é executada 
num = input("Digite um número: ")
print(num)

    # Variáveis: definimos uma variável e atribuímos a ela um valor. 
lugar = "Brasil"       # Definimos um valor fora da função print, após definirmos uma váriavel para o nome lugar
print(lugar)

    # Função while: Executa a função enquanto ela continuar sendo verdadeira

# Jogo de Adivinhação - Criação de um jogo
""""
A ideia do nosso jogo é termos que acertar um número secreto. 
Quando o programa estiver rodando, teremos que digitar um número e o programa dirá se acertamos ou 
erramos o número, com várias tentativas e níveis.

"""
print("Bem-vindo no jogo de Adivinhação!")

numero_secreto = 42         
tentativas = 3                              # Pode tentar o código 3 vezes 
rodada = 1

# Enquanto ainda há tentativas o código irá rodar
while (rodada <= tentativas):
    print("Tentativa {} de {}" .format(rodada, tentativas)) 
    chute_str = input("Digite seu número: ")     # Função que é usada para mostrar o que aparecerá no console
    print("Você digitou ", chute_str)
    chute = int (chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto
if(acertou):                                 # if: condição verdadeira
    print("Você acertou!")
    
else:                                        # else: condição falsa
    if(maior):             # Sinal > usado para comparação de maior
        print("Você errou! O seu número foi maior do que o número secreto.")
        
    elif(menor):           # Sinal < usado para comparação de menor
            print("Você errou! O seu número foi menor do que o número secreto.")

rodada = rodada + 1 

print('Fim de jogo')

