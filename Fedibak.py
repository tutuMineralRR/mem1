import random

print("Bem-vindo ao jogo 'Adivinhe o Número'!")
print("Tente adivinhar um número entre 1 e 100.")

secret = random.randint(1, 100)
attempt = 0

while True:
    user_guess = int(input("Digite um número: "))
    attempt += 1

    if user_guess == secret:
        print("Parabéns, você adivinhou o número!!")
        break
    elif user_guess > secret:
        print("Esse número é maior que o número correto.")
    elif user_guess < secret:
        print("Esse número é menor que o número correto.")