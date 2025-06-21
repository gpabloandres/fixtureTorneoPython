import random

# Lista de 8 equipos
equipos = [
    "5º 1º (Alejandro - Camilo)", "5º 2º (Celina - Leandro)", "5º 3º (Juan Guridi - Nahuel Nicolisi)", "6º 1º (Orión - Tomás)",
    "6º 1º (Morena - Lucia)", "6º 2º (Máximo - Valentino)", "7º 1º (Angel - Alexis)", "7º 2º (Geremias - Tomás)"
]

# Verificamos que haya exactamente 8 equipos
if len(equipos) == 8:
    random.shuffle(equipos)  # Mezclamos los equipos

    print("🎲 Cruces sorteados:")
    i = 0
    while i < len(equipos):
        print(f"  • {equipos[i]} vs {equipos[i + 1]}")
        i += 2
else:
    print("⚠️  Debe haber exactamente 8 equipos.")
