#!/usr/bin/python

'VANETs...'

import os
import time
# import random

from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from mininet.link import TCLink

def topology():

    "Create a network."
    net = Mininet_wifi(controller=None, switch=OVSKernelSwitch,
                       link=wmediumd, wmediumd_mode=interference)

    c1 = net.addController( 'c1', controller=RemoteController, ip='127.0.0.1', port=6633 )

    info("*** Creating nodes\n")
    cars = []
    for x in range(0, 20):
        cars.append(x)

    cars[0] = net.addCar('car0',  wlans=1, range='50', ip='200.0.10.110/8', mac='00:00:00:00:00:01', position='2117,243,0')
    cars[1] = net.addCar('car1',  wlans=1, range='50', ip='200.0.10.111/8', mac='00:00:00:00:00:02', position='2117,245,0')
    cars[2] = net.addCar('car2',  wlans=1, range='50', ip='200.0.10.112/8', mac='00:00:00:00:00:03', position='2114,243,0')
    cars[3] = net.addCar('car3',  wlans=1, range='50', ip='200.0.10.113/8', mac='00:00:00:00:00:04', position='2114,245,0')
    cars[4] = net.addCar('car4',  wlans=1, range='50', ip='200.0.10.114/8', mac='00:00:00:00:00:05', position='2111,243,0')

    cars[5] = net.addCar('car5',  wlans=1, range='50', ip='200.0.10.115/8', mac='00:00:00:00:00:06', position='1617,243,0')
    cars[6] = net.addCar('car6',  wlans=1, range='50', ip='200.0.10.116/8', mac='00:00:00:00:00:07', position='1617,245,0')
    cars[7] = net.addCar('car7',  wlans=1, range='50', ip='200.0.10.117/8', mac='00:00:00:00:00:08', position='1614,243,0')
    cars[8] = net.addCar('car8',  wlans=1, range='50', ip='200.0.10.118/8', mac='00:00:00:00:00:09', position='1611,243,0')

    cars[9] = net.addCar('car9',  wlans=1, range='50', ip='200.0.10.119/8', mac='00:00:00:00:00:10', position='1117,243,0')
    cars[10] = net.addCar('car10',  wlans=1, range='50', ip='200.0.10.120/8', mac='00:00:00:00:00:11', position='1114,243,0')
    cars[11] = net.addCar('car11',  wlans=1, range='50', ip='200.0.10.121/8', mac='00:00:00:00:00:12', position='1111,243,0')

    cars[12] = net.addCar('car12',  wlans=1, range='50', ip='200.0.10.122/8', mac='00:00:00:00:00:13', position='400,243,0')
    cars[13] = net.addCar('car13',  wlans=1, range='50', ip='200.0.10.123/8', mac='00:00:00:00:00:14', position='450,243,0')
    cars[14] = net.addCar('car14',  wlans=1, range='50', ip='200.0.10.124/8', mac='00:00:00:00:00:15', position='500,243,0')
    cars[15] = net.addCar('car15',  wlans=1, range='50', ip='200.0.10.125/8', mac='00:00:00:00:00:16', position='550,245,0')
    cars[16] = net.addCar('car16',  wlans=1, range='50', ip='200.0.10.126/8', mac='00:00:00:00:00:17', position='600,245,0')
    cars[17] = net.addCar('car17',  wlans=1, range='50', ip='200.0.10.127/8', mac='00:00:00:00:00:18', position='650,245,0')
    cars[18] = net.addCar('car18',  wlans=1, range='50', ip='200.0.10.128/8', mac='00:00:00:00:00:19', position='700,247,0')
    cars[19] = net.addCar('car19',  wlans=1, range='50', ip='200.0.10.129/8', mac='00:00:00:00:00:20', position='750,247,0')

    # cars[20] = net.addCar('car20',  wlans=1, range='50', ip='200.0.10.130/8', mac='00:00:00:00:00:21', position='10,243,0')
    # cars[21] = net.addCar('car21',  wlans=1, range='50', ip='200.0.10.131/8', mac='00:00:00:00:00:22', position='15,243,0')
    # cars[22] = net.addCar('car22',  wlans=1, range='50', ip='200.0.10.132/8', mac='00:00:00:00:00:23', position='20,243,0')
    # cars[23] = net.addCar('car23',  wlans=1, range='50', ip='200.0.10.133/8', mac='00:00:00:00:00:24', position='25,243,0')
    # cars[24] = net.addCar('car24',  wlans=1, range='50', ip='200.0.10.134/8', mac='00:00:00:00:00:25', position='10,245,0')
    # cars[25] = net.addCar('car25',  wlans=1, range='50', ip='200.0.10.135/8', mac='00:00:00:00:00:26', position='15,245,0')
    # cars[26] = net.addCar('car26',  wlans=1, range='50', ip='200.0.10.136/8', mac='00:00:00:00:00:27', position='20,245,0')
    # cars[27] = net.addCar('car27',  wlans=1, range='50', ip='200.0.10.137/8', mac='00:00:00:00:00:28', position='25,245,0')
    # cars[28] = net.addCar('car28',  wlans=1, range='50', ip='200.0.10.138/8', mac='00:00:00:00:00:29', position='10,247,0')
    # cars[29] = net.addCar('car29',  wlans=1, range='50', ip='200.0.10.139/8', mac='00:00:00:00:00:30', position='15,247,0')

    rsu1 = net.addAccessPoint('rsu1', ssid='rsu1', mode='g',
                               channel='1', range='250', position='1100,250,0', protocols='OpenFlow13')
    rsu2 = net.addAccessPoint('rsu2', ssid='rsu2', mode='g',
                               channel='6', range='250', position='1600,250,0', protocols='OpenFlow13')
    rsu3 = net.addAccessPoint('rsu3', ssid='rsu3', mode='g',
                               channel='11', range='250', position='2100,250,0', protocols='OpenFlow13')

    sw1 = net.addSwitch ('sw1', dpid='9', protocols='OpenFlow13')
    sw2 = net.addSwitch ('sw2', dpid='10', protocols='OpenFlow13')

    server_s1 = net.addHost ('server_s1', ip='200.0.10.2/8')
    server_s2 = net.addHost ('server_s2', ip='200.0.10.2/8')
    server_s3 = net.addHost ('server_s3', ip='200.0.10.2/8')
    server_e = net.addHost ('server_e', ip='200.0.10.3/8')
    server_e2 = net.addHost ('server_e2', ip='200.0.10.4/8')
    server_g = net.addHost ('server_g', ip='200.0.10.5/8')

    info("*** Configuring Propagation Model\n")
    net.propagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    print("*** Creating links")
    net.addLink(rsu1, rsu2, 2, 2)
    net.addLink(rsu2, rsu3, 3, 2)
    net.addLink(server_s1, rsu1, 0, 5)
    net.addLink(server_s2, rsu2, 0, 5)
    net.addLink(server_s3, rsu3, 0, 5)
    net.addLink(server_e, sw2, 0, 1)
    net.addLink(server_e2, sw2, 0, 2)
    net.addLink(server_g, sw2, 0, 3)
    link1 = net.addLink(sw1, sw2, 1, 4, cls=TCLink )
    link2 = net.addLink(rsu1, sw1, 3, 2, cls=TCLink)
    link3 = net.addLink(rsu2, sw1, 4, 3, cls=TCLink)
    link4 = net.addLink(rsu3, sw1, 3, 4, cls=TCLink)

    print( "*** Configuring links bandwidth" )
    link1.intf1.config( bw=80 )
    link2.intf1.config( bw=26 )
    link3.intf1.config( bw=26 )
    link4.intf1.config( bw=26 )

    net.plotGraph(max_x=2400, max_y=500)
    
    print("*** Starting network")
    net.build()
    c1.start()
    rsu1.start([c1])
    rsu2.start([c1])
    rsu3.start([c1])
    sw1.start([c1])
    sw2.start([c1])

    server_s1.cmd('iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP')
    server_s2.cmd('iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP')
    server_s3.cmd('iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP')
    server_e.cmd('iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP')
    server_e2.cmd('iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP')
    server_g.cmd('iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP')

    time.sleep(1)

    os.system('ovs-vsctl set bridge rsu1 other-config:datapath-id=0000000000000006')
    os.system('ovs-vsctl set bridge rsu2 other-config:datapath-id=0000000000000007')
    os.system('ovs-vsctl set bridge rsu3 other-config:datapath-id=0000000000000008')
    
    os.system('ovs-vsctl --all destroy QoS; ovs-vsctl --all destroy Queue')

    os.system('ovs-vsctl set-manager ptcp:6632')
    
    time.sleep(1)

    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000006/ovsdb_addr')
    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000007/ovsdb_addr')
    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000008/ovsdb_addr')
    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000009/ovsdb_addr')
    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000010/ovsdb_addr')

    print( "*** Shutting ports" )
    time.sleep(1)

    #Filtra trafego nas portas entre switches (evitar L2 loop)
    os.system('curl -X POST -d \'{ "dpid": 6, "cookie": 0, "cookie_mask": 1, "table_id": 1, "priority": 1, "flags": 2, "match":{ "in_port":2}, "actions":[{ "type":"CLEAR_ACTIONS"}]}\' http://localhost:8080/stats/flowentry/add')
    os.system('curl -X POST -d \'{ "dpid": 7, "cookie": 0, "cookie_mask": 1, "table_id": 1, "priority": 1, "flags": 2, "match":{ "in_port":2}, "actions":[{ "type":"CLEAR_ACTIONS"}]}\' http://localhost:8080/stats/flowentry/add')
    os.system('curl -X POST -d \'{ "dpid": 7, "cookie": 0, "cookie_mask": 1, "table_id": 1, "priority": 1, "flags": 2, "match":{ "in_port":3}, "actions":[{ "type":"CLEAR_ACTIONS"}]}\' http://localhost:8080/stats/flowentry/add')
    os.system('curl -X POST -d \'{ "dpid": 8, "cookie": 0, "cookie_mask": 1, "table_id": 1, "priority": 1, "flags": 2, "match":{ "in_port":2}, "actions":[{ "type":"CLEAR_ACTIONS"}]}\' http://localhost:8080/stats/flowentry/add')
    
    time.sleep(1)

    os.system('ovs-ofctl del-flows sw1 -O Openflow13; ovs-ofctl add-flow sw1 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl del-flows sw2 -O Openflow13; ovs-ofctl add-flow sw2 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow sw2 "table=1, priority=0, actions=CONTROLLER:65535" -O Openflow13; ovs-ofctl add-flow sw2 "table=1, priority=0, in_port=1 actions=4" -O Openflow13; ovs-ofctl add-flow sw2 "table=1, priority=0, in_port=2 actions=4" -O Openflow13; ovs-ofctl add-flow sw2 "table=1, priority=0, in_port=3 actions=4" -O Openflow13; ovs-ofctl del-flows rsu1 -O Openflow13; ovs-ofctl del-flows rsu2 -O Openflow13; ovs-ofctl del-flows rsu3 -O Openflow13; ovs-ofctl add-flow rsu1 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow rsu2 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow rsu3 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=0, in_port=1, actions=3" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=0, in_port=3, actions=1" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=0, in_port=1, actions=4" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=0, in_port=4, actions=1" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=0, in_port=1, actions=3" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=0, in_port=3, actions=1" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,icmp actions=5" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=1, cookie=0x28,in_port=5, actions=1" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=1, cookie=0x28, in_port=1, arp actions=3,5" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,icmp actions=5" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=1, cookie=0x28,in_port=5, actions=1" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=1, cookie=0x28, in_port=1, arp actions=4,5" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,icmp actions=5" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=1, cookie=0x28,in_port=5, actions=1" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=1, cookie=0x28, in_port=1, arp actions=3,5" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,udp,tp_dst=5002 actions=5" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,udp,tp_dst=5002 actions=5" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,udp,tp_dst=5002 actions=5" -O Openflow13; mysql -u root -pwifi -e "delete from redirect;" framework 2> /dev/null')

    time.sleep(2)

    os.system('mysql -u root -pwifi < ./framework_its_sdn/initialdb.sql -fv &')
    os.system('./framework_its_sdn/lc_mob.sh > j2.txt &')
    time.sleep(3)
    os.system('./framework_its_sdn/central_controller2.sh > j1.txt &')
    os.system('./framework_its_sdn/local_controllers.sh > j3.txt &')

    time.sleep(2)

#     net.startMobility( time=0 )
#     net.mobility( cars[0], 'start', time=1, position='120,1000,0' )
#     net.mobility( cars[0], 'stop', time=179, position='2101,1000,0' )
#     net.mobility( cars[1], 'start', time=1, position='130,999,0' )
#     net.mobility( cars[1], 'stop', time=179, position='2095,999,0' )
#     net.mobility( cars[2], 'start', time=1, position='135,247,0' )
#     net.mobility( cars[2], 'stop', time=59, position='2097,247,0' )
#     net.mobility( cars[3], 'start', time=1, position='140,1000,0' )
#     net.mobility( cars[3], 'stop', time=59, position='1601,1000,0' )
#     net.mobility( cars[4], 'start', time=1, position='145,999,0' )
#     net.mobility( cars[4], 'stop', time=59, position='1599,999,0' )
#     net.mobility( cars[5], 'start', time=1, position='150,247,0' )
#     net.mobility( cars[5], 'stop', time=179, position='1595,247,0' )
#     net.mobility( cars[6], 'start', time=1, position='155,1000,0' )
#     net.mobility( cars[6], 'stop', time=179, position='1101,1000,0' )
#     net.mobility( cars[7], 'start', time=1, position='160,1000,0' )
#     net.mobility( cars[7], 'stop', time=179, position='1098,1000,0' )
#     net.mobility( cars[8], 'start', time=1, position='165,999,0' )
#     net.mobility( cars[8], 'stop', time=179, position='1095,999,0' )
#     net.stopMobility( time=180 )

    server_s1.cmd('tcpdump udp port 5002 -i server_s1-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s1.txt &')
    server_s2.cmd('tcpdump udp port 5002 -i server_s2-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s2.txt &')
    server_s3.cmd('tcpdump udp port 5002 -i server_s3-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s3.txt &')
    server_e.cmd('tcpdump udp port 5003 -i server_e-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_e.txt &')
    server_e2.cmd('tcpdump udp port 5004 -i server_e2-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_e2.txt &')
    server_g.cmd('tcpdump udp port 5005 -i server_g-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_g.txt &')

########## T1

    
    print( "*** Iniciando geracao de trafego" )

    time.sleep(2)

    for x in xrange(0,12):

        cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

        print("*** Car[%d] connect to server_s at 1Mbps" %x)
        cars[x].cmdPrint("timeout 305 hping3 --udp -p 5002 -i u10200 -d 1470 200.0.10.2 -q &")
        cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)
        
        print("*** Car[%d] connect to server_e at 1Mbps" %x)
        cars[x].cmdPrint("timeout 305 hping3 --udp -p 5003 -i u10200 -d 1470 200.0.10.3 -q &")
        cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

        print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
        cars[x].cmdPrint("timeout 305 hping3 --udp -p 5004 -i u6800 -d 1470 200.0.10.4 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

        print("*** Car[%d] connect to server_g at 1Mbps" %x)
        cars[x].cmdPrint("timeout 305 hping3 --udp -p 5005 -i u10200 -d 1470 200.0.10.5 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x)   
    
#     for x in xrange(12,19):

#         cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

#         print("*** Car[%d] connect to server_s at 1Mbps" %x)
#         cars[x].cmdPrint("hping3 --udp -p 5002 -i u10200 -d 1470 -c 1 200.0.10.2 -q &")
#         cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)

#         print("*** Car[%d] connect to server_e at 1Mbps" %x)
#         cars[x].cmdPrint("hping3 --udp -p 5003 -i u10200 -d 1470 -c 1 200.0.10.3 -q &")
#         cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

#         print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
#         cars[x].cmdPrint("hping3 --udp -p 5004 -i u6800 -d 1470 -c 1 200.0.10.4 -q &")
#         cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

#         print("*** Car[%d] connect to server_g at 1Mbps" %x)
#         cars[x].cmdPrint("hping3 --udp -p 5005 -i u10200 -d 1470 -c 1 200.0.10.5 -q &")
#         cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x) 
    
#     time.sleep(2)
#     os.system('echo T1 > rsuocp.txt; echo RSU3 >> rsuocp.txt; hostapd_cli -i rsu3-wlan1 all_sta | grep : >> rsuocp.txt; echo RSU2 >> rsuocp.txt; hostapd_cli -i rsu2-wlan1 all_sta | grep : >> rsuocp.txt;  echo RSU1 >> rsuocp.txt; hostapd_cli -i rsu1-wlan1 all_sta | grep : >> rsuocp.txt; ')

#     ######### T2
    time.sleep(305)
#     ############################
    
#     # RSU3
#     #car0-4
#     cars[5].setPosition('2117,247,0') #chegou
#     cars[6].setPosition('2114,247,0') #chegou
#     cars[7].setPosition('2111,247,0') #chegou
#     cars[8].setPosition('2111,245,0') #chegou

    
    
#     # RSU 2
#     cars[9].setPosition('1617,243,0') #chegou
#     cars[10].setPosition('1614,243,0') #chegou


#     # RSU 1
#     #car11

        
#     #Out    
#     #car12-19


#     time.sleep(2)
#     os.system('echo T2 >> rsuocp.txt; echo RSU3 >> rsuocp.txt; hostapd_cli -i rsu3-wlan1 all_sta | grep : >> rsuocp.txt; echo RSU2 >> rsuocp.txt; hostapd_cli -i rsu2-wlan1 all_sta | grep : >> rsuocp.txt;  echo RSU1 >> rsuocp.txt; hostapd_cli -i rsu1-wlan1 all_sta | grep : >> rsuocp.txt; ')

#     ########## T3
#     time.sleep(75)
#     #############################
    
#     # RSU3
#     #car0-8
    
    
#     # RSU 2
#     #car9-10
#     cars[11].setPosition('1611,243,0') #chegou
#     cars[12].setPosition('1617,245,0') #chegou
#     cars[15].setPosition('1614,245,0') #chegou
#     cars[18].setPosition('1611,245,0') #chegou

    

#     # RSU 1
#     cars[13].setPosition('1117,243,0') #chegou

      
#     #Out    
#     #car16,17,14,19

#     for x in (12, 13, 15, 18):

#         cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

#         print("*** Car[%d] connect to server_s at 1Mbps" %x)
#         cars[x].cmdPrint("timeout 160 hping3 --udp -p 5002 -i u10200 -d 1470 200.0.10.2 -q &")
#         cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)
        
#         print("*** Car[%d] connect to server_e at 1Mbps" %x)
#         cars[x].cmdPrint("timeout 160 hping3 --udp -p 5003 -i u10200 -d 1470 200.0.10.3 -q &")
#         cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

#         print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
#         cars[x].cmdPrint("timeout 160 hping3 --udp -p 5004 -i u6800 -d 1470 200.0.10.4 -q &")
#         cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

#         print("*** Car[%d] connect to server_g at 1Mbps" %x)
#         cars[x].cmdPrint("timeout 160 hping3 --udp -p 5005 -i u10200 -d 1470 200.0.10.5 -q &")
#         cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x)
    
#     time.sleep(2)
#     os.system('echo T3 >> rsuocp.txt; echo RSU3 >> rsuocp.txt; hostapd_cli -i rsu3-wlan1 all_sta | grep : >> rsuocp.txt; echo RSU2 >> rsuocp.txt; hostapd_cli -i rsu2-wlan1 all_sta | grep : >> rsuocp.txt;  echo RSU1 >> rsuocp.txt; hostapd_cli -i rsu1-wlan1 all_sta | grep : >> rsuocp.txt; ')

#     ########## T4
#     time.sleep(75)
#     #############################
    
#     # RSU3
#     #car0-8
    
    
#     # RSU 2
# #     #car9-12,15,18
    

#     # RSU 1
# #     #car13
#     cars[14].setPosition('1114,243,0') #chegou
#     cars[16].setPosition('1111,243,0') #chegou
#     cars[17].setPosition('1117,245,0') #chegou
#     cars[19].setPosition('1114,245,0') #chegou
    
#     for x in (14, 16, 17, 19):

#         cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

#         print("*** Car[%d] connect to server_s at 1Mbps" %x)
#         cars[x].cmdPrint("timeout 80 hping3 --udp -p 5002 -i u10200 -d 1470 200.0.10.2 -q &")
#         cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)

#         print("*** Car[%d] connect to server_e at 1Mbps" %x)
#         cars[x].cmdPrint("timeout 80 hping3 --udp -p 5003 -i u10200 -d 1470 200.0.10.3 -q &")
#         cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

#         print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
#         cars[x].cmdPrint("timeout 80 hping3 --udp -p 5004 -i u6800 -d 1470 200.0.10.4 -q &")
#         cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

#         print("*** Car[%d] connect to server_g at 1Mbps" %x)
#         cars[x].cmdPrint("timeout 80 hping3 --udp -p 5005 -i u10200 -d 1470 200.0.10.5 -q &")
#         cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x)  
    
#     time.sleep(2)
#     os.system('echo T4 >> rsuocp.txt; echo RSU3 >> rsuocp.txt; hostapd_cli -i rsu3-wlan1 all_sta | grep : >> rsuocp.txt; echo RSU2 >> rsuocp.txt; hostapd_cli -i rsu2-wlan1 all_sta | grep : >> rsuocp.txt;  echo RSU1 >> rsuocp.txt; hostapd_cli -i rsu1-wlan1 all_sta | grep : >> rsuocp.txt; ')

#     time.sleep(76)

#     os.system('fuser -k ./framework_its_sdn/central_controller2.sh')
#     os.system('fuser -k ./framework_its_sdn/lc_mob.sh')  
#     os.system('fuser -k ./framework_its_sdn/local_controllers.sh')

    os.system('pkill tcpdump')
    os.system('pkill hping3')
    os.system('pkill ping')

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()

    server_s1.cmd('iptables -D OUTPUT 1')
    server_s2.cmd('iptables -D OUTPUT 1')
    server_s3.cmd('iptables -D OUTPUT 1')
    server_e.cmd('iptables -D OUTPUT 1')
    server_e2.cmd('iptables -D OUTPUT 1')
    server_g.cmd('iptables -D OUTPUT 1')


if __name__ == '__main__':
    setLogLevel('info')
    topology()
