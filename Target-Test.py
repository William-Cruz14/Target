# Questão 2

fibonacci = [0, 1,]

num = int(input("Digite qualquer número inteiro: "))
count = 1

while (count < num): # Como a sequência de Fibonacci tende ao infinito, coloquei o número informado como o limite.
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
    count += 1

print(fibonacci)

if num in fibonacci:
    print(f"O número {num} pertence a sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence a sequência de Fibonacci.")


# Questão 5
    
palavra = input("Digite uma palavra qualquer: ")
palavra_inversa = ""

for letra in palavra[::-1]: # Usei slice para iniciar o for da ultima letra.
    palavra_inversa += letra

print(f"Palavra inversa: {palavra_inversa}")