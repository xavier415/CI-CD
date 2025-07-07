from src.maquina_cafe import MaquinaDeCafe

def mostrar_menu():
    print("\n=== Bienvenido a la Máquina de Café ☕ ===")
    print("1. Pequeño (3 oz)\n2. Mediano (5 oz)\n3. Grande  (7 oz)")

def seleccionar_tipo_vaso(opcion):
    return {"1": "pequeno", "2": "mediano", "3": "grande"}.get(opcion)

if __name__ == "__main__":
    maquina = MaquinaDeCafe()
    while True:
        mostrar_menu()
        tam = input("Seleccione el tamaño (1-3) o 'q' para salir: ")
        if tam.lower() == 'q':
            print("¡Gracias por usar la máquina!")
            break

        tipo_vaso = seleccionar_tipo_vaso(tam)
        if not tipo_vaso:
            print("❌ Opción inválida.")
            continue

        try:
            azucar = int(input("¿Cuántas cucharadas de azúcar desea? "))
        except ValueError:
            print("❌ Ingrese un número válido.")
            continue

        resultado = maquina.get_vaso_de_cafe(tipo_vaso, 1, azucar)
        print("🧾 Resultado:", resultado)