# actividad3.2.py
# Script para verificar configuración básica del sistema

import platform
import psutil
import os

def verificar_sistema():
    print("=== Verificación del Sistema ===")
    print(f"Sistema operativo: {platform.system()}")
    print(f"Versión: {platform.version()}")
    print(f"Arquitectura: {platform.architecture()}")
    print(f"Procesador: {platform.processor()}")

    # Memoria
    memoria = psutil.virtual_memory()
    print(f"\nMemoria total: {memoria.total / (1024**3):.2f} GB")
    print(f"Memoria disponible: {memoria.available / (1024**3):.2f} GB")

    # Disco
    disco = psutil.disk_usage('/')
    print(f"\nDisco total: {disco.total / (1024**3):.2f} GB")
    print(f"Disco libre: {disco.free / (1024**3):.2f} GB")

    print("\n=== Configuración completada ===")

if __name__ == "__main__":
    verificar_sistema()