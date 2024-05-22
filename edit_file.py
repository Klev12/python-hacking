# Función para mostrar colaboradores
def show_collaborators(filename, num_collaborators=5):
    with open(filename, "r") as archivo:  
        contador = 0
        for line in archivo:
            if contador < num_collaborators:
                print(line.strip())
                contador += 1
            else:
                break


def add_collaborator(filename, new_collaborator):
    with open(filename, "a+") as archivo:  
        archivo.seek(0)  
        lines = [line.strip() for line in archivo.readlines() if line.strip()]
        if len(lines) < 15:
            archivo.write(new_collaborator + "\n")  
            print("Nuevo colaborador agregado con éxito.")
        else:
            print("Ya hay 15 colaboradores, no se pueden agregar más.")

filename = "colaboradores.txt"


show_collaborators(filename)
new_collaborator = input("Ingrese el nombre del nuevo colaborador: ")
add_collaborator(filename, new_collaborator)
