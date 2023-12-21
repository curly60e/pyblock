import hashlib
import random
import string
import time
from termcolor import colored

def sha512_hash(input_data):
    """Calcula el hash SHA-512 de la entrada dada."""
    sha512 = hashlib.sha512()
    sha512.update(input_data.encode())
    return sha512.hexdigest()

def generar_cadena_aleatoria(longitud=6):
    """Genera una cadena aleatoria de la longitud especificada."""
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for i in range(longitud))

def generar_elemento_transaccion(hash_resultado, longitud):
    """Genera un elemento de transacción Bitcoin basado en el hash."""
    return hash_resultado[:longitud]

def sha256_visual_demo_sha512_bitcoin_indefinido():
    input_data = generar_cadena_aleatoria()
    ciclo = 1

    while True:
        print(colored(f"\nProceso de hashing {ciclo} con input: {input_data}", "green"))

        # Convertir input a ASCII y luego a binario
        valores_ascii = [ord(c) for c in input_data]
        valores_binarios = [bin(v)[2:].zfill(8) for v in valores_ascii]
        mensaje_binario = ''.join(valores_binarios)

        # Mostrar conversiones
        print(colored("Valores ASCII:", "yellow"))
        print(valores_ascii)
        print(colored("Mensaje en binario:", "cyan"))
        for valor in valores_binarios:
            print(colored(valor, "blue"))

        # Padding
        required_padding = 512 - len(mensaje_binario) - 64
        padding = '0' * required_padding + bin(len(mensaje_binario))[2:].zfill(64)
        mensaje_padded = mensaje_binario + padding

        # Mostrar mensaje con padding más lentamente
        print(colored("Mensaje con padding:", "magenta"))
        for j in range(0, len(mensaje_padded), 64):
            print(colored(mensaje_padded[j:j+64], "magenta"))
            time.sleep(0.5)

        # Calcular hash SHA-512 del mensaje
        hash_resultado = sha512_hash(input_data)
        print(colored("Hash SHA-512 del mensaje:", "cyan"))
        print(colored(hash_resultado, "yellow"))

        # Generar elementos de transacción Bitcoin basados en el hash
        script_pubkey = generar_elemento_transaccion(hash_resultado, 64)
        script_sig = generar_elemento_transaccion(hash_resultado, 128)
        n_secuencia = generar_elemento_transaccion(hash_resultado, 8)
        print(colored(f"ScriptPubKey: {script_pubkey}", "cyan"))
        print(colored(f"ScriptSig: {script_sig}", "cyan"))
        print(colored(f"nSecuencia: {n_secuencia}", "cyan"))

        # Usar el hash completo como input para el siguiente ciclo
        input_data = hash_resultado

        ciclo += 1
        time.sleep(1)

# Ejecutar el proceso de hashing indefinidamente
sha256_visual_demo_sha512_bitcoin_indefinido()
