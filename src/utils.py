import os

def ensure_directory_exists(directory):
    """
    Asegura que un directorio exista, creándolo si es necesario.

    Args:
        directory (str): Ruta del directorio.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directorio creado: {directory}")

# Asegurar que las carpetas de datos y modelos existan
def initialize_project_structure():
    """
    Crea las carpetas necesarias para el proyecto si no existen.
    """
    ensure_directory_exists("data")
    ensure_directory_exists("models")
    print("Estructura del proyecto inicializada.")
