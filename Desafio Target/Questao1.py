numero = int(input("Escreva o número que deseja saber se está na sequência em fibonacci ou não: "))

fibonacci = [0,1]

index = 0

while True:


    novoNumeroFibonacci = fibonacci[index] + fibonacci[index+1]

    fibonacci.append(novoNumeroFibonacci)


    if index == numero:
        break

    index+=1

if numero in fibonacci:

    print(f"O número {numero} pertence a sequência de Fibonacci")

else:

    print(f"O número {numero} não pertence a sequência de Fibonacci")