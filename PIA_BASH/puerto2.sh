ports() {
read -p "Introduce la IP: " dirip
read -p "Introduce un rango de puertos a escanear: " ranport
IFS="-" read -r port_in port_fin <<< "$ranport"
echo "Se estan analizando los puertos de $dirip del $port_in al $port_fin, espere un momento"

for ((port=$port_in; port<=$port_fin; port++))
do
	timeout 1 bash -c "</dev/tcp/$dirip/$port" &> /dev/null && echo "El puerto $port esta abierto" || echo "El puerto $port esta cerrado"
done
echo "El escaneo ha terminado" 
}
