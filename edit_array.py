tareas_pendientes = []

def mostrar_menu():
    print("\nOpciones del menú:")
    print("1. Mostrar lista de tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

def mostrar_tareas():
    if not tareas_pendientes:
        print("\nNo hay tareas pendientes.")
    else:
        print("\nLista de tareas pendientes:")
        for i, tarea in enumerate(tareas_pendientes, 1):
            print(f"{i}. {tarea}")

def agregar_tarea():
    tarea = input("Escribe la tarea que deseas agregar: ")
    tareas_pendientes.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea():
    mostrar_tareas()
    if tareas_pendientes:
        try:
            indice = int(input("\nIntroduce el número de la tarea que deseas eliminar: "))
            if 1 <= indice <= len(tareas_pendientes):
                tarea_eliminada = tareas_pendientes.pop(indice - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Número inválido. Por favor, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

while True:
    mostrar_menu()
    opcion = input("\nSelecciona una opción (1-4): ")
    if opcion == '1':
        mostrar_tareas()
    elif opcion == '2':
        agregar_tarea()
    elif opcion == '3':
        eliminar_tarea()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción del 1 al 4.")
