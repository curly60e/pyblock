import shutil
import os
from PIL import Image as PILImage
from term_image.image import from_file

def set_terminal_background(color="black"):
    if color == "black":
        os.system('printf "\033[40m"')  # Secuencia de escape ANSI para fondo negro
    elif color == "reset":
        os.system('printf "\033[49m"')  # Secuencia de escape ANSI para restaurar el fondo


def createimagebitaxe():
    # Ruta al archivo de imagen
    image_path = "bitaxe.jpg"

    # Cargar la imagen usando PIL y redimensionarla
    pil_image = PILImage.open(image_path)

    # Obtener el tamaño de la terminal
    terminal_size = shutil.get_terminal_size()

    # Ajustar el tamaño de la imagen según el tamaño de la terminal
    # Restar algunos caracteres para asegurarse de que encaje bien
    max_width = (terminal_size.columns - 4) * 2  # Ajustar el factor según sea necesario
    max_height = (terminal_size.lines - 4) * 4  # Ajustar el factor según sea necesario

    # Redimensionar la imagen manteniendo la proporción
    pil_image.thumbnail((max_width, max_height))

    # Guardar la imagen redimensionada temporalmente
    temp_image_path = "resized_image.png"
    pil_image.save(temp_image_path)

    # Cargar la imagen redimensionada usando term-image
    image = from_file(temp_image_path)
    # Envolver el comando draw en secuencias de escape para mantener el fondo negro
    image.draw()
