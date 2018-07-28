#!/bin/bash

# mysql -u root -p$pass -e "select sum(data_rate) from appkpi where id IN (select app_id from vehicle where mac = \"00:00:00:00:00:01\")" framework

# x=$(mysql -u root -p$pass -e "select sum(data_rate) from appkpi where id IN (select app_id from vehicle where mac = \"00:00:00:00:00:03\")" framework | tail -1)

# os.system('ovs-ofctl del-flows sw1 -O Openflow13; ovs-ofctl add-flow sw1 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow sw1 "table=1, priority=0, actions=CONTROLLER:65535" -O Openflow13')

# for i in $x; do echo $i; mysql -u root -pwifi -e "select sum(data_rate) from appkpi where id IN (select app_id from vehicle where mac = '"$i"')" framework 2> /dev/null; done

#define capacidade dos links de upload em mbps
up=10000000

#Define a periodicidade em segundos, na qual os controladores verificam o status da rede local
t=2

while true;
do
	#Para cada interface wlan de RSU identificada
	for j in $(ifconfig | grep wlan | cut -d' ' -f1);
	do
		#Identifica veiculos na RSU, buscando pelo MAC
		x=$(hostapd_cli -i $j all_sta | grep :)

		#Busca na base de dados e salva em $y a soma dos valores de requisitos de banda dos veiculos na RSU
		y=$(
		for i in $x;
		do
			mysql -u root -pwifi -e "select sum(data_rate) from appkpi where id IN (select app_id from vehicle where mac = '"$i"')" framework 2> /dev/null |tail -1
		done | paste -s | expand | sed 's/ /+/g' | bc)

		#se a soma dos requisitos é maior que zero, calcula o saldo da RSU, armazena em $sd e imprime na tela resultados
		if [[ $y -gt 0 ]]; then
			sd=$(echo $up-$y|bc)
			echo -e "\n " $(echo $j | cut -d'-' -f1) " tem ocupado " $(echo $y|bc) " e saldo de " $sd ". " $(echo $x| wc -w) " veiculos"
		fi

		#Se o saldo da RSU é menor que zero informa redirecionamento
		if [[ $sd -lt 0 ]]; then
			echo -e "\n Redirecionando"
		fi

	done

	sleep $t
done