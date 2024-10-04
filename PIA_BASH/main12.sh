# Importar funciones
source mainredes.sh
source puerto2.sh
# Mostrar el menu 
main() {
    echo ""
    echo "          MENU          "
    echo "------------------------"
    echo "Seleccione una opcion:"
    echo "1) Monitoreo de Red"
    echo "2) Monitoreo de Puertos"
    echo "3) Salir"
}

while true; do
    main
    read -p "Opcion: " option

    case $option in
        1)
            main_network
            ;;
        2)
            ports  
            ;;
        3)
            break
            ;;
        *)
            echo "Opcion Invalida"
            ;;
    esac

    echo ""
done

