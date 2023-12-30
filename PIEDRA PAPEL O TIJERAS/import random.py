import random

def jugar_ppt():
    opciones = ["piedra", "papel", "tijeras"]

    while True:
    
        usuario = input("Elige piedra, papel o tijeras (o 'salir' para terminar): ").lower()

        if usuario == 'salir':
            print("Gracias por jugar. ¡Hasta luego!")
            break

        if usuario not in opciones:
            print("Por favor, ingresa una opción válida.")
            continue

        
        computadora = random.choice(opciones)

    
        if usuario == computadora:
            print(f"¡Empate! Ambos eligieron {usuario}.")
        elif (usuario == "piedra" and computadora == "tijeras") or \
            (usuario == "papel" and computadora == "piedra") or \
            (usuario == "tijeras" and computadora == "papel"):
            print(f"¡Ganaste! {usuario} gana a {computadora}.")
        else:
            print(f"¡Perdiste! {computadora} gana a {usuario}.")

if __name__ == "__main__":
    jugar_ppt()