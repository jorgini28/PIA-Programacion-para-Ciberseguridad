New-ModuleManifest -Path "C:\Users\raulg\Documents\GitHub\desktop-tutorial\PIA_PC\ApiCalis.psd1" -RootModule "C:\Users\raulg\Documents\GitHub\desktop-tutorial\PIA_PC\ApiCalis.psm1"
Import-Module "C:\Users\raulg\Documents\GitHub\desktop-tutorial\PIA_PC\ApiCalis.psm1"
Get-Module Get-VirusTotalReport

New-ModuleManifest -Path "C:\Users\raulg\Documents\GitHub\desktop-tutorial\PIA_PC\Arch_Oc.psd1" -RootModule "C:\Users\raulg\Documents\GitHub\desktop-tutorial\PIA_PC\Arch_Oc.psm1"
Import-Module "C:\Users\raulg\Documents\GitHub\desktop-tutorial\PIA_PC\Arch_Oc.psm1" 
Get-Module archivos_ocultos 

do {
    Write-Host "1) Elija una opcion"
    Write-Host "2) Revision de archivos hashes"
    Write-Host "3) Revision de uso de recursos del sistema"
    Write-Host "4)Tarea adicional"
    Write-Host "5) Salir"

    $opcion = Read-Host

    switch ($opcion) {
        1 {Get-VirusTotalReport}
        2{archivos_ocultos}
        5 {exit}
    }
} while ($opcion -ne 5)
