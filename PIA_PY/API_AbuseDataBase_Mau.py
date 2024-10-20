import requests

def check_ip(ip_address):
    API_KEY = input("Por favor, ingresa tu clave de API: ")
    BASE_URL = 'https://api.abuseipdb.com/api/v2/'
    url = f'{BASE_URL}check'
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    
    try:
        respuesta = requests.get(url, headers=headers, params=params)
        respuesta.raise_for_status()
        resultado = respuesta.json()
        
        #Formato
        print("\n--- Resultado de la Verificacion de IP ---")
        print(f"Direccion IP: {resultado.get('data', {}).get('ipAddress', 'No disponible')}")
        print(f"Estado: {resultado.get('data', {}).get('abuseConfidenceScore', 'No disponible')}% de confianza en abuso")
        print(f"Total de reportes: {resultado.get('data', {}).get('totalReports', 'No disponible')}")
        
        if 'reports' in resultado['data']:
            print("\nDetalles de los reportes:")
            for reporte in resultado['data']['reports']:
                print(f"- Fecha: {reporte['date']} | Comentario: {reporte['comment']} | Categoria: {reporte['category']}")
        
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

def report_ip(ip_address, comentario, categorias):
    """Reporta una direccion IP abusiva."""
    url = f'{BASE_URL}report'
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    datos = {
        'ip': ip_address,
        'comment': comentario,
        'categories': categorias.split(',')  # lista
    }
    
    try:
        respuesta = requests.post(url, headers=headers, json=datos)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

def main_menu():
    while True:
        print("\nMenu de la Base de Datos de Abuso de IP:")
        print("1. Verificar IP")
        print("2. Reportar IP")
        print("3. Salir")
        
        opcion = input("Selecciona una opcion (1-3): ")
        
        if opcion == '1':
            ip_address = input("Ingresa la direccion IP a verificar: ")
            check_ip(ip_address)  # Llamamos a la funcion que ya tiene formato
            
        elif opcion == '2':
            ip_address = input("Ingresa la direccion IP a reportar: ")
            comentario = input("Ingresa un comentario para el reporte: ")
            categorias = input("Ingresa categorias (separadas por comas): ")
            resultado = report_ip(ip_address, comentario, categorias)
            if resultado:
                print(resultado)
        
        elif opcion == '3':
            confirmar_salida = input("¿Estas seguro de que deseas salir? (y/n): ").lower()
            if confirmar_salida == 'y':
                print("Saliendo...")
                break
            elif confirmar_salida == 'n':
                print("Regresando al menu principal...")
            else:
                print("Por favor responde con 'y' o 'n'.")
        
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu_data()
