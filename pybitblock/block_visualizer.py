import os
import json
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from asciimatics.screen import Screen

# Función para ejecutar comandos de bitcoin-cli y obtener resultados
def bitcoin_cli(command):
    result = subprocess.run(['bitcoin-cli'] + command.split(), capture_output=True, text=True)
    return result.stdout.strip()

# Función para obtener los datos del último bloque
def fetch_block_data():
    # Obtener el hash del último bloque
    blockhash = bitcoin_cli('getbestblockhash')
    # Eliminar impresión del hash del bloque
    # print(f"Block Hash: {blockhash}")

    # Obtener los detalles del último bloque con detalles completos de las transacciones
    block_details = bitcoin_cli(f'getblock {blockhash} 2')
    block_data = json.loads(block_details)

    # Extraer weights y fees desde los datos del bloque
    tx_weights = [tx['weight'] for tx in block_data['tx']]
    tx_fees = [tx.get('fee', 0) for tx in block_data['tx']]  # Asignar 0 si no tiene fee

    # Normalizar fees para escalar los colores
    min_fee = min(tx_fees)
    max_fee = max(tx_fees)
    normalized_fees = [(fee - min_fee) / (max_fee - min_fee) if max_fee != min_fee else 0 for fee in tx_fees]

    # Combinar, ordenar y desempaquetar
    transactions = sorted(zip(tx_weights, tx_fees, normalized_fees), key=lambda x: x[1], reverse=True)
    tx_weights, tx_fees, normalized_fees = zip(*transactions)

    return blockhash, tx_weights, tx_fees, normalized_fees

# Función para obtener el color usando un colormap de matplotlib
def get_fee_color(normalized_fee):
    cmap = plt.get_cmap('viridis')
    color = cmap(normalized_fee)
    r, g, b, _ = [int(255 * x) for x in color]
    return r, g, b

# Función para convertir el color a un color en la paleta de asciimatics
def convert_color_to_palette_index(r, g, b):
    return (r // 51) * 36 + (g // 51) * 6 + (b // 51)

# Función principal para dibujar el bloque de transacciones
def visualize_block(screen):
    current_blockhash = None

    while True:
        new_blockhash, tx_weights, tx_fees, normalized_fees = fetch_block_data()

        if new_blockhash != current_blockhash:
            current_blockhash = new_blockhash
            screen.clear()

            max_height, max_width = 28, 70
            height, width = min(screen.dimensions[0], max_height), min(screen.dimensions[1], max_width)

            total_weight = sum(tx_weights)
            scaled_tx_weights = [(weight / total_weight) * (0.7 * width * height) for weight in tx_weights]

            offset_x = (screen.width - width) // 2
            offset_y = (screen.height - height) // 2

            current_x = offset_x
            current_y = offset_y + height - 1

            for weight, fee, normalized_fee in zip(scaled_tx_weights, tx_fees, normalized_fees):
                area = int(weight)
                r, g, b = get_fee_color(normalized_fee)
                color_index = convert_color_to_palette_index(r, g, b)
                # Eliminar impresión del detalle de cada transacción
                # print(f"Weight: {weight}, Fee: {fee}, Color Index: {color_index}")

                rect_width = max(1, int(np.sqrt(area)))
                rect_height = max(1, int(area / rect_width))

                if current_x + rect_width >= offset_x + width:
                    current_x = offset_x
                    current_y -= rect_height
                    if current_y <= offset_y:
                        break

                rect_width = min(rect_width, offset_x + width - current_x)
                rect_height = min(rect_height, current_y - offset_y)

                for x in range(current_x, current_x + rect_width):
                    for y in range(current_y - rect_height, current_y):
                        screen.print_at(' ', x, y, bg=color_index)

                current_x += rect_width

            screen.refresh()

def run_visualizer():
    Screen.wrapper(visualize_block)

if __name__ == "__main__":
    run_visualizer()
