import time
from colorama import init, Fore, Style
from inputimeout import inputimeout, TimeoutOccurred

init(autoreset=True)

def mostrar_bienvenida():
    print(Fore.CYAN + Style.BRIGHT + "**********************************************")
    print(Fore.CYAN + Style.BRIGHT + "**** Juego de Preguntas: Expresión Génica ****")
    print(Fore.CYAN + Style.BRIGHT + "**********************************************\n")
    print(Fore.YELLOW + "Se premia la rápidez de tu respuesta ☝ 🤓")
    print(Fore.YELLOW + "Tenes un máximo de 10 segundos para responder\n")
    print(Fore.YELLOW + "¡Presiona Enter para comenzar!\n")
    input(">> ")

def obtener_preguntas():
    preguntas = [
        {
            "pregunta": "¿Qué proceso sigue a la transcripción en la expresión génica?",
            "opciones": ["a) Traducción", "b) Replicación", "c) Transducción", "d) Traducción inversa"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Cuál es el principal producto de la transcripción?",
            "opciones": ["a) ADN", "b) ARN mensajero (ARNm)", "c) Proteína", "d) Ribosoma"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Dónde ocurre la traducción en una célula eucariota?",
            "opciones": ["a) Núcleo", "b) Mitocondria", "c) Ribosoma", "d) Lisosoma"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué enzima es responsable de la síntesis de ARN durante la transcripción?",
            "opciones": ["a) ADN polimerasa", "b) ARN polimerasa", "c) Helicasa", "d) Ligasa"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué proceso regula la expresión génica al bloquear la traducción del ARNm?",
            "opciones": ["a) Activación génica", "b) Represión génica", "c) Interferencia de ARN (ARNi)", "d) Metilación del ADN"],
            "respuesta": "c"
        }
    ]
    return preguntas

def calcular_puntaje(tiempo_respuesta, tiempo_max=30, puntaje_max=10):
    """
    Calcula el puntaje basado en el tiempo de respuesta.
    - tiempo_max: tiempo máximo permitido para obtener puntaje.
    - puntaje_max: puntaje máximo por pregunta.
    """
    if tiempo_respuesta > tiempo_max:
        return 0  # Sin puntaje si excede el tiempo máximo
    else:
        # Puntaje decrece linealmente con el tiempo
        puntaje = puntaje_max - (puntaje_max * tiempo_respuesta / tiempo_max)
        return round(puntaje, 2)

def jugar(preguntas):
    puntaje_total = 0
    tiempo_max_por_pregunta = 10  # segundos
    puntaje_max_por_pregunta = 20

    for idx, pregunta in enumerate(preguntas, 1):
        print(Fore.MAGENTA + f"\nPregunta {idx}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(Fore.MAGENTA + opcion)

        # Iniciar el temporizador
        inicio = time.time()
        print(inicio)

        try:
            respuesta_usuario = inputimeout(prompt=Fore.WHITE + "Tu respuesta (a/b/c/d): ", timeout=tiempo_max_por_pregunta).lower().strip()
        except TimeoutOccurred:
            print(Fore.RED + "\nTiempo excedido. Pasando a la siguiente pregunta.")
            print(Fore.BLUE + f"Puntaje Total: {round(puntaje_total, 2)} / {puntaje_max_por_pregunta * len(preguntas)}")
            continue

        fin = time.time()

        tiempo_respuesta = fin - inicio
        tiempo_respuesta = round(tiempo_respuesta, 2)

        # Verificar si el tiempo de respuesta excede el tiempo máximo permitido
        if tiempo_respuesta > tiempo_max_por_pregunta:
            print(Fore.RED + f"\nTiempo excedido por  ({tiempo_respuesta - tiempo_max_por_pregunta} segundos). Pasando a la siguiente pregunta.")
            print(Fore.BLUE + f"Puntaje Total: {round(puntaje_total, 2)} / {puntaje_max_por_pregunta * len(preguntas)}")
            continue

        # Validar la entrada del usuario
        if respuesta_usuario not in ['a', 'b', 'c', 'd']:
            if not respuesta_usuario:
                print(Fore.RED + "\nRespuesta vacía. Puntaje: 0")
            else:
                print(Fore.RED + "\nRespuesta inválida. Puntaje: 0")
            print(Fore.BLUE + f"Puntaje Total: {round(puntaje_total, 2)} / {puntaje_max_por_pregunta * len(preguntas)}")
            continue

        # Evaluar la respuesta del usuario
        if respuesta_usuario == pregunta['respuesta']:
            puntaje_obtenido = calcular_puntaje(
                tiempo_respuesta,
                tiempo_max=tiempo_max_por_pregunta,
                puntaje_max=puntaje_max_por_pregunta
            )
            print(Fore.GREEN + f"\n¡Correcto! Tiempo de respuesta: {tiempo_respuesta} segundos. Puntaje: {puntaje_obtenido}")
            puntaje_total += puntaje_obtenido
        else:
            print(Fore.RED + f"\nIncorrecto. La respuesta correcta era '{pregunta['respuesta']}'.")
            print(Fore.RED + f"Tiempo de respuesta: {tiempo_respuesta} segundos. Puntaje: 0")

        # Mostrar puntaje acumulado hasta el momento
        print(Fore.BLUE + f"Puntaje Total: {round(puntaje_total, 2)} / {puntaje_max_por_pregunta * len(preguntas)}")

    print(Fore.CYAN + "\n**************************************************")
    print(Fore.CYAN + f"Terminó el juego 😁. Tu puntaje total es {round(puntaje_total, 2)} de {puntaje_max_por_pregunta * len(preguntas)}.")
    print(Fore.CYAN + "**************************************************")

def main():
    mostrar_bienvenida()
    preguntas = obtener_preguntas()
    jugar(preguntas)

if __name__ == "__main__":
    main()
