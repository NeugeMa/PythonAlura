# Jogo de Adivinhação - Criação de um jogo
""""
A ideia do nosso jogo é termos que acertar um número secreto. 
Quando o programa estiver rodando, teremos que digitar um número e o programa dirá se acertamos ou 
erramos o número, com várias tentativas e níveis.

"""
print("Bem-vindo no jogo de Adivinhação!")

numero_secreto = 42         
chute_str = input("Digite seu número: ")     # Função que é usada para mostrar o que aparecerá no console

print("Você digitou ", chute_str)
chute = int (chute_str)

if (numero_secreto == chute_str):            # if: comparação verdadeira
    print("Você acertou!")
else:                                        # else: comparação falsa
    print("Você errou!")
    
print('Fim de jogo')