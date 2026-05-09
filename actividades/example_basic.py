# example_basic.py
# Ejemplo básico de Python - Verificación de conectividad de red

import socket
import subprocess

def ping_host(host):
    """Función para hacer ping a un host"""
    try:
        # Para Windows
        result = subprocess.run(['ping', '-n', '1', host],
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return f"✓ {host} está accesible"
        else:
            return f"✗ {host} no responde"
    except Exception as e:
        return f"Error al hacer ping a {host}: {e}"

def verificar_conectividad():
    print("=== Verificación de Conectividad de Red ===")

    # Verificar localhost
    print(ping_host("127.0.0.1"))

    # Verificar gateway (asumiendo 192.168.1.1)
    print(ping_host("192.168.1.1"))

    # Verificar DNS de Google
    print(ping_host("8.8.8.8"))

    # Obtener nombre del host
    try:
        hostname = socket.gethostname()
        ip_local = socket.gethostbyname(hostname)
        print(f"\nNombre del host: {hostname}")
        print(f"IP local: {ip_local}")
    except Exception as e:
        print(f"Error obteniendo información del host: {e}")

if __name__ == "__main__":
    verificar_conectividad()