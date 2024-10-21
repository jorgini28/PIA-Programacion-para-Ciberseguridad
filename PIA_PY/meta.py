import os
from mutagen import File

#Carga y muestra metadatos de un archivo
def mostrar_metadatos(ruta_archivo):
    audio = File(ruta_archivo)
    if audio is not None:
        print(f"\nMetadatos de {ruta_archivo}:")
        for clave, valor in audio.items():
            print(f"{clave}: {valor}")
    else:
        print(f"No se pudieron leer los metadatos de {ruta_archivo}")

#Busca archivos en un directorio por sus extensiones
def listar_archivos(ruta_directorio, extensiones):
    archivos_encontrados = []
    for archivo in os.listdir(ruta_directorio):
        if archivo.endswith(extensiones):
            archivos_encontrados.append(archivo)
    return archivos_encontrados

#Maneja la interaccion del usuario y la logica del menu
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Mostrar metadatos de archivos .mp3")
        print("2. Mostrar metadatos de archivos .flac")
        print("3. Mostrar metadatos de archivos .ogg")
        print("4. Mostrar metadatos de archivos .wav")
        print("5. Mostrar metadatos de archivos .mp4")
        print("6. Mostrar metadatos de archivos .JPG")
        print("7. Mostrar metadatos de todos los archivos")
        print("8. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion in ['1', '2', '3', '4', '5', '6', '7']:
            ruta_directorio = input("Introduce la ruta del directorio: ")
            if os.path.isdir(ruta_directorio):
                extensiones = {
                    '1': ('.mp3',),
                    '2': ('.flac',),
                    '3': ('.ogg',),
                    '4': ('.wav',),
                    '5': ('.mp4',),
                    '6': ('.JPG',),
                    '7': ('.mp3', '.flac', '.ogg', '.wav', '.mp4')
                }
                archivos = listar_archivos(ruta_directorio, extensiones[opcion])
                if archivos:
                    for archivo in archivos:
                        ruta_archivo = os.path.join(ruta_directorio, archivo)
                        mostrar_metadatos(ruta_archivo)
                else:
                    print("No se encontraron archivos en el directorio.")
            else:
                print("La ruta es invalida")
        
        elif opcion == '8':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()
