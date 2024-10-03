string = input("Digite a string: ")

quantidade_de_As = 0

for letra in string:

    if letra.lower() == 'a':

        quantidade_de_As += 1

print(f"Na string: {string} existem {quantidade_de_As} as")