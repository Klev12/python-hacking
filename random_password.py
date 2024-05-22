import random
import string

def generate_password (lenght):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = '' .join(random.choice(characters) for i in range(lenght))

    return password

while True:
    try:
        lenght = int(input("Introduce la longitud que deseas que sea la contraseña."))
        if lenght <=0:
            print("Colocar un numero que no sea 0")
        else:
            break
    except ValueError:
        print("Entrada invalida, coloca un numero entero")

generated_password = generate_password(lenght)
print(f"Tu contraseña generada es:{generated_password}")
