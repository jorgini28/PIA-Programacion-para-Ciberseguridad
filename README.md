Proyecto de Ciberseguridad - Módulos de PowerShell
Descripción
Este proyecto consiste en el desarrollo de módulos de PowerShell para tareas de ciberseguridad. Los módulos implementan las siguientes funcionalidades:

Revisión de hashes de archivos y consulta a VirusTotal.
Listado de archivos ocultos en una carpeta específica.
Revisión de uso de recursos del sistema (memoria, disco, procesador, red).
Detección de conexiones de red sospechosas.
Requisitos
PowerShell
API Key de VirusTotal
Módulos
1. Get-VirusTotalReport
Consulta el estado de un archivo en VirusTotal mediante su hash.

function Get-VirusTotalReport {
    param ([string]$ApiKey)

    # Lógica para consultar VirusTotal...
}

2. archivos_ocultos
Busca archivos ocultos en una carpeta especificada.

function archivos_ocultos { 
    param ([string]$ruta)

    # Lógica para buscar archivos ocultos...
}

3. Show-Resources
Revisa el uso de recursos del sistema.

function Show-Resources {
    # Lógica para mostrar uso de CPU, memoria, disco y red...
}

4. Detectar-ConexionesSospechosas
Detecta conexiones TCP establecidas y consulta su reputación en VirusTotal.

function Detectar-ConexionesSospechosas {
    # Lógica para detectar conexiones sospechosas...
}

Uso
Cambiar política de ejecución

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

Ejecutar el menú principal

do {
    Write-Host "Elija una opción"
    Write-Host "1) Revisión de archivos hashes"
    Write-Host "2) Buscar archivos ocultos"
    Write-Host "3) Revisión de uso de recursos del sistema"
    Write-Host "4) Revisar conexiones sospechosas"
    Write-Host "5) Salir"

    $opcion = Read-Host
    switch ($opcion) {
        1 { Get-VirusTotalReport }
        2 { archivos_ocultos }
        3 { Show-Resources }
        4 { Detectar-ConexionesSospechosas }
        5 { exit }
    }
} while ($opcion -ne 5)

Notas
Asegúrate de tener configurada tu API Key de VirusTotal en el módulo correspondiente.
El tiempo de ejecución puede variar dependiendo del número de archivos y el uso de recursos.