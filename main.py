def mostrar_menu():
    print("\n=== PYTHON SECURITY TOOLKIT ===")
    print("1. Consultar informacion del proyecto")
    print("2. Consultar conceptos de Python")
    print("3. Verificar fortaleza de una contrasena")
    print("4. Salir")


def consultar_proyecto():
    print("\nProyecto educativo para aprender Python, Git y GitHub.")
    print("Enfocado en herramientas educativas de ciberseguridad.")


def consultar_conceptos():
    print("\nPython permite crear programas mediante funciones,")
    print("estructuras de control, modulos y otras herramientas.")


def verificar_contrasena():
    contrasena = input("\nIntroduce una contrasena de prueba: ")

    puntuacion = 0

    if len(contrasena) >= 12:
        puntuacion += 1

    if any(caracter.islower() for caracter in contrasena):
        puntuacion += 1

    if any(caracter.isupper() for caracter in contrasena):
        puntuacion += 1

    if any(caracter.isdigit() for caracter in contrasena):
        puntuacion += 1

    if any(not caracter.isalnum() for caracter in contrasena):
        puntuacion += 1

    if puntuacion <= 2:
        nivel = "Debil"
    elif puntuacion <= 4:
        nivel = "Moderada"
    else:
        nivel = "Fuerte"

    print(f"Fortaleza estimada: {nivel}")
    print("Esta evaluacion es orientativa y no garantiza la seguridad.")


def main():
    while True:
        mostrar_menu()

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            consultar_proyecto()

        elif opcion == "2":
            consultar_conceptos()

        elif opcion == "3":
            verificar_contrasena()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida. Intentalo nuevamente.")


if __name__ == "__main__":
    main()