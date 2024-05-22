with open ("estudiante.txt", "r") as file:
   content = file.readlines()
print(content[1])


def read(filename, num_lines):
    with open(filename, "r") as file:
        for _ in range(num_lines):
            line = file.readline()
            if not line:
                break
            print(line.strip())

read('estudiantes.txt', 1)


