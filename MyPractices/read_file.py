with open ("estudiante.txt", "r") as file:
   content = file.readlines()
print(content[1])


def read (filename, num_lines):
    with open (filename, "r") as file:
        for _ in range (num_lines) :
            line = line.readline ()
            if not line:
                break
            print(line.strip())

read('estudiante.txt', 3)

