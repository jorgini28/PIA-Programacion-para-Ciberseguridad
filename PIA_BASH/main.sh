
main() {
    while true; do
        clear
        echo "              MENU                " 
        echo "----------------------------------"
        echo "1) Monitoreo de red"
        echo "2) Monitoreo de puertos"
        echo "3) Salir"
        read -p "Seleccione una opcion: " option
        
        case $option in
            1)
                mainredes.sh
                ;;
            2)
                
                ;;
            3)
                read -p "¿Está seguro que desea salir? (s/n): " confirm
                if [[ $confirm == "s" ]]; then
                    break
                fi
                ;;
            *)
                echo "OPCION INVALIDA"
                ;;
        esac
        read -p "Presione [Enter] para continuar"
    done
}

main
