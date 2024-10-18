import shodan

#Obtener informacion de la API
def info_API(ShodanApi):
    try:
        info = ShodanApi.info() 
        for i in info:
            print('%s: %s ' % (i, info[i]))
    except shodan.APIError as e:
        print('Error al obtener informacion de la API: %s' % e)

#Limitar la busqueda de dispositivos
def busq_dis(ShodanApi, query, limit=10):
    try:
        resultados = ShodanApi.search(query)
        print(f"Resultados encontrados: {resultados['total']}")

        for idx, resultado in enumerate(resultados['matches']):
            if idx >= limit:
                break 
            ip = resultado['ip_str']
            print(f"{idx + 1}. IP: {ip} - {resultado['data']}")
    except shodan.APIError as e:
        print(f"Error al buscar dispositivos: {e}")

#Buscar vulnerabilidades en un host
def busc_v(ShodanApi, ip):
    try:
        host = ShodanApi.host(ip)
        print(f"Informacion del host: {host['ip_str']}")
        print(f"Organizacion: {host.get('org', 'N/A')}")
        print(f"Sistema operativo: {host.get('os', 'N/A')}")
        print("Vulnerabilidades:")
        for vuln in host.get('vulns', []):
            print(f" - {vuln}")
    except shodan.APIError as e:
        print(f"Error al buscar vulnerabilidades para {ip}: {e}")

#Funcion principal
def rec_shodan():
    try:
        mi_ApiKey = input("Escribe tu API key: ")
        api = shodan.Shodan(mi_ApiKey)

        print("Esta es la informacion de la API:")
        info_API(api)

        query = input("Escribe el termino de busqueda para los dispositivos: ")
        limit = int(input("¿Cuántos resultados deseas ver?: ")) 
        busq_dis(api, query, limit)

        ip = input("Escribe la IP para buscar vulnerabilidades: ")
        busc_v(api, ip)

    except shodan.APIError as e:
        print(f"Error con la API: {e}")

# Llamada principal
if __name__ == "__main__":
    rec_shodan()
