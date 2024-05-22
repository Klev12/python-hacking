import argparse
parse = argparse.ArgumentParser(description="Holaaaaaa como estan")
parser.add_argument('archivo',type=str, help='estudiantes.txt')
parser.add_argumnet("--modo",choices=["lectura","escritura"], default="lectura", help="Modo de operacion")

print(f"Arhivo: {args.archivo}")
print(f"Modo: {args.modo}")