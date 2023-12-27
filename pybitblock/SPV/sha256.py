import hashlib
import random
import string
import time
import curses

def sha256_hash(input_data):
    sha256 = hashlib.sha256()
    sha256.update(input_data.encode())
    return sha256.hexdigest()

def binario_de_hexadecimal(hex_string):
    """Convierte una cadena hexadecimal en una cadena binaria."""
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def binario_a_hex(binario):
    """Convierte una cadena binaria en una cadena hexadecimal."""
    return hex(int(binario, 2))[2:].zfill(64)

def generar_cadena_aleatoria(longitud=6):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for i in range(longitud))

def mainSHA(stdscr):
    curses.curs_set(0)  # Oculta el cursor
    input_data = generar_cadena_aleatoria()
    ciclo = 1

    curses.curs_set(0)  # Oculta el cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)

    while True:
        stdscr.clear()

        # Convertir input a ASCII y luego a binario
        valores_ascii = [ord(c) for c in input_data]
        valores_binarios = [bin(v)[2:].zfill(8) for v in valores_ascii]
        mensaje_binario = ''.join(valores_binarios)

        # Calcular hash SHA-256 del mensaje
        hash_resultado = sha256_hash(input_data)
        hash_binario = bin(int(hash_resultado, 16))[2:].zfill(256)

        #script_sig_binario = binario_de_hexadecimal(hash_resultado[:128])
        n_secuencia_binario = binario_de_hexadecimal(hash_resultado[:8])

        # Crear diferentes "ventanas" para cada parte del proceso
        altura, ancho = stdscr.getmaxyx()

        # Ventana para el resultado
        win_resultado = curses.newwin(altura // 3, ancho, 0, 0)
        win_resultado.box()
        win_resultado.addstr(1, 1, f"Hashing {ciclo}:", curses.color_pair(1))  # Posición de texto ajustada
        win_resultado.addstr(2, 1, f"Hash SHA-256: {hash_resultado}", curses.color_pair(1))
        win_resultado.addstr(3, 1, f"ScriptPubKey: {hash_resultado[:64]}", curses.color_pair(3))
        win_resultado.addstr(4, 1, f"ScriptSig HEX: {hash_resultado[:32]}", curses.color_pair(3))
        win_resultado.addstr(5, 1, f"nSeq BIN: {n_secuencia_binario}", curses.color_pair(4))
        win_resultado.refresh()

        # Ventana para el padding
        win_padding = curses.newwin(altura // 3, ancho, altura // 3, 0)
        win_padding.box()
        win_padding.addstr(1, 1, "Padding:", curses.color_pair(1))
        for i, linea in enumerate(mensaje_binario[j:j+64] for j in range(0, len(mensaje_binario), 64)):
            win_padding.addstr(i + 2, 1, linea, curses.color_pair(4))
            win_padding.refresh()
            time.sleep(0.5)
        win_padding.refresh()

        # Ventana para el hash binario
        win_hash_binario = curses.newwin(altura // 3, ancho, 2 * altura // 3, 0)
        win_hash_binario.box()
        win_hash_binario.addstr(1, 1, "BIN:", curses.color_pair(1))
        for i, linea in enumerate(hash_binario[j:j+64] for j in range(0, len(hash_binario), 64)):
            win_hash_binario.addstr(i + 2, 1, linea, curses.color_pair(5))
        win_hash_binario.refresh()
        time.sleep(1)  # Esperar antes de continuar con el siguiente ciclo

        # Preparar para el siguiente ciclo
        input_data = hash_resultado
        ciclo += 1

def ex():
    # Ejecutar el proceso en un bucle de `curses`
    curses.wrapper(mainSHA)
