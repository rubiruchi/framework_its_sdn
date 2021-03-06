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
    for x in range(0, 30):
        cars.append(x)

    cars[0] = net.addCar('car0',  wlans=1, range='50', ip='200.0.10.110/8', mac='00:00:00:00:00:01')
    cars[1] = net.addCar('car1',  wlans=1, range='50', ip='200.0.10.111/8', mac='00:00:00:00:00:02')
    cars[2] = net.addCar('car2',  wlans=1, range='50', ip='200.0.10.112/8', mac='00:00:00:00:00:03')
    cars[3] = net.addCar('car3',  wlans=1, range='50', ip='200.0.10.113/8', mac='00:00:00:00:00:04')
    cars[4] = net.addCar('car4',  wlans=1, range='50', ip='200.0.10.114/8', mac='00:00:00:00:00:05')
    cars[5] = net.addCar('car5',  wlans=1, range='50', ip='200.0.10.115/8', mac='00:00:00:00:00:06')
    cars[6] = net.addCar('car6',  wlans=1, range='50', ip='200.0.10.116/8', mac='00:00:00:00:00:07')

    cars[7] = net.addCar('car7',  wlans=1, range='50', ip='200.0.10.117/8', mac='00:00:00:00:00:08')
    cars[8] = net.addCar('car8',  wlans=1, range='50', ip='200.0.10.118/8', mac='00:00:00:00:00:09')
    cars[9] = net.addCar('car9',  wlans=1, range='50', ip='200.0.10.119/8', mac='00:00:00:00:00:10')
    cars[10] = net.addCar('car10',  wlans=1, range='50', ip='200.0.10.120/8', mac='00:00:00:00:00:11')
    cars[11] = net.addCar('car11',  wlans=1, range='50', ip='200.0.10.121/8', mac='00:00:00:00:00:12')
    cars[12] = net.addCar('car12',  wlans=1, range='50', ip='200.0.10.122/8', mac='00:00:00:00:00:13')

    cars[13] = net.addCar('car13',  wlans=1, range='50', ip='200.0.10.123/8', mac='00:00:00:00:00:14')
    cars[14] = net.addCar('car14',  wlans=1, range='50', ip='200.0.10.124/8', mac='00:00:00:00:00:15')
    cars[15] = net.addCar('car15',  wlans=1, range='50', ip='200.0.10.125/8', mac='00:00:00:00:00:16')
    cars[16] = net.addCar('car16',  wlans=1, range='50', ip='200.0.10.126/8', mac='00:00:00:00:00:17')
    cars[17] = net.addCar('car17',  wlans=1, range='50', ip='200.0.10.127/8', mac='00:00:00:00:00:18')
    cars[18] = net.addCar('car18',  wlans=1, range='50', ip='200.0.10.128/8', mac='00:00:00:00:00:19')
    cars[19] = net.addCar('car19',  wlans=1, range='50', ip='200.0.10.129/8', mac='00:00:00:00:00:20')

    cars[20] = net.addCar('car20',  wlans=1, range='50', ip='200.0.10.130/8', mac='00:00:00:00:00:21')
    cars[21] = net.addCar('car21',  wlans=1, range='50', ip='200.0.10.131/8', mac='00:00:00:00:00:22')
    cars[22] = net.addCar('car22',  wlans=1, range='50', ip='200.0.10.132/8', mac='00:00:00:00:00:23')
    cars[23] = net.addCar('car23',  wlans=1, range='50', ip='200.0.10.133/8', mac='00:00:00:00:00:24')
    cars[24] = net.addCar('car24',  wlans=1, range='50', ip='200.0.10.134/8', mac='00:00:00:00:00:25')
    cars[25] = net.addCar('car25',  wlans=1, range='50', ip='200.0.10.135/8', mac='00:00:00:00:00:26')
    cars[26] = net.addCar('car26',  wlans=1, range='50', ip='200.0.10.136/8', mac='00:00:00:00:00:27')
    cars[27] = net.addCar('car27',  wlans=1, range='50', ip='200.0.10.137/8', mac='00:00:00:00:00:28')
    cars[28] = net.addCar('car28',  wlans=1, range='50', ip='200.0.10.138/8', mac='00:00:00:00:00:29')
    cars[29] = net.addCar('car29',  wlans=1, range='50', ip='200.0.10.139/8', mac='00:00:00:00:00:30')

    rsu1 = net.addAccessPoint('rsu1', ssid='rsu1', mode='g',
                               channel='1', range='250', position='1100,1000,0', protocols='OpenFlow13')
    rsu2 = net.addAccessPoint('rsu2', ssid='rsu2', mode='g',
                               channel='6', range='250', position='1600,1000,0', protocols='OpenFlow13')
    rsu3 = net.addAccessPoint('rsu3', ssid='rsu3', mode='g',
                               channel='11', range='250', position='2100,1000,0', protocols='OpenFlow13')

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

    net.plotGraph(max_x=3000, max_y=3000)
    
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

    server_s1.cmd('tcpdump udp port 5002 -i server_s1-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s1.txt &')
    server_s2.cmd('tcpdump udp port 5002 -i server_s2-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s2.txt &')
    server_s3.cmd('tcpdump udp port 5002 -i server_s3-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s3.txt &')
    server_e.cmd('tcpdump udp port 5003 -i server_e-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_e.txt &')
    server_e2.cmd('tcpdump udp port 5004 -i server_e2-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_e2.txt &')
    server_g.cmd('tcpdump udp port 5005 -i server_g-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_g.txt &')

########## T1
    # RSU3
    cars[0].setPosition('2115,993,0')
    cars[1].setPosition('2112,993,0')
    cars[2].setPosition('2115,995,0')
    cars[3].setPosition('2112,995,0')
    cars[4].setPosition('2115,997,0')
    cars[5].setPosition('2112,997,0')
    cars[6].setPosition('2109,997,0')
    
    # RSU 2
    cars[7].setPosition('1615,993,0')
    cars[8].setPosition('1612,993,0')
    cars[9].setPosition('1615,995,0')
    cars[10].setPosition('1612,995,0')
    cars[11].setPosition('1609,995,0')
    cars[12].setPosition('1606,995,0')

    # RSU 1
    cars[13].setPosition('1115,993,0')
    cars[14].setPosition('1112,993,0')
    cars[15].setPosition('1115,995,0')
    cars[16].setPosition('1112,995,0')
    cars[17].setPosition('1115,997,0')
    cars[18].setPosition('1112,997,0')
    cars[19].setPosition('1109,997,0')

    #Out
    cars[20].setPosition('10,993,0')
    cars[21].setPosition('15,993,0')
    cars[22].setPosition('20,993,0')
    cars[23].setPosition('25,993,0')
    cars[24].setPosition('10,995,0')
    cars[25].setPosition('15,995,0')
    cars[26].setPosition('20,995,0')
    cars[27].setPosition('25,995,0')
    cars[28].setPosition('10,997,0')
    cars[29].setPosition('15,997,0')
    
    print( "*** Iniciando geracao de trafego" )

    time.sleep(2)

    for x in xrange(0,20):

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
    
    for x in xrange(20,30):

        cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

        print("*** Car[%d] connect to server_s at 1Mbps" %x)
        cars[x].cmdPrint("hping3 --udp -p 5002 -i u10200 -d 1470 -c 1 200.0.10.2 -q &")
        cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)
        
        print("*** Car[%d] connect to server_e at 1Mbps" %x)
        cars[x].cmdPrint("hping3 --udp -p 5003 -i u10200 -d 1470 -c 1 200.0.10.3 -q &")
        cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

        print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
        cars[x].cmdPrint("hping3 --udp -p 5004 -i u6800 -d 1470 -c 1 200.0.10.4 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

        print("*** Car[%d] connect to server_g at 1Mbps" %x)
        cars[x].cmdPrint("hping3 --udp -p 5005 -i u10200 -d 1470 -c 1 200.0.10.5 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x) 
        
    net.startMobility( time=0 )
    net.mobility( cars[7], 'start', time=1, position='1615,993,0' )
    net.mobility( cars[7], 'stop', time=74, position='2109,993,0' )
    net.mobility( cars[9], 'start', time=1, position='1615,995,0' )
    net.mobility( cars[9], 'stop', time=74, position='2109,995,0' )
    net.mobility( cars[11], 'start', time=1, position='1609,995,0' )
    net.mobility( cars[11], 'stop', time=74, position='2106,995,0' )

    net.mobility( cars[13], 'start', time=1, position='1115,993,0' )
    net.mobility( cars[13], 'stop', time=74, position='1609,993,0' )
    net.mobility( cars[15], 'start', time=1, position='1115,995,0' )
    net.mobility( cars[15], 'stop', time=74, position='1609,995,0' )
    net.mobility( cars[17], 'start', time=1, position='1115,997,0' )
    net.mobility( cars[17], 'stop', time=74, position='1603,997,0' )

    net.mobility( cars[20], 'start', time=1, position='10,993,0' )
    net.mobility( cars[20], 'stop', time=74, position='1109,993,0' )
    net.mobility( cars[24], 'start', time=1, position='10,995,0' )
    net.mobility( cars[24], 'stop', time=74, position='1109,995,0' )
    net.mobility( cars[25], 'start', time=1, position='15,995,0' )
    net.mobility( cars[25], 'stop', time=74, position='1106,995,0' )
    net.mobility( cars[28], 'start', time=1, position='10,997,0' )
    net.mobility( cars[28], 'stop', time=74, position='1106,997,0' )
    net.stopMobility( time=75 )
    
    for x in (20, 24, 25, 28):

        cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

        print("*** Car[%d] connect to server_s at 1Mbps" %x)
        cars[x].cmdPrint("timeout 235 hping3 --udp -p 5002 -i u10200 -d 1470 200.0.10.2 -q &")
        cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)
        
        print("*** Car[%d] connect to server_e at 1Mbps" %x)
        cars[x].cmdPrint("timeout 235 hping3 --udp -p 5003 -i u10200 -d 1470 200.0.10.3 -q &")
        cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

        print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
        cars[x].cmdPrint("timeout 235 hping3 --udp -p 5004 -i u6800 -d 1470 200.0.10.4 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

        print("*** Car[%d] connect to server_g at 1Mbps" %x)
        cars[x].cmdPrint("timeout 235 hping3 --udp -p 5005 -i u10200 -d 1470 200.0.10.5 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x) 
    
    net.startMobility( time=76 )
    net.mobility( cars[14], 'start', time=77, position='1112,993,0' )
    net.mobility( cars[14], 'stop', time=149, position='1606,993,0' )
    net.mobility( cars[16], 'start', time=77, position='1112,995,0' )
    net.mobility( cars[16], 'stop', time=149, position='1606,995,0' )
    net.mobility( cars[18], 'start', time=77, position='1112,997,0' )
    net.mobility( cars[18], 'stop', time=149, position='1600,997,0' )
    net.mobility( cars[19], 'start', time=77, position='1109,997,0' )
    net.mobility( cars[19], 'stop', time=149, position='1597,997,0' )

    net.mobility( cars[21], 'start', time=77, position='15,993,0' )
    net.mobility( cars[21], 'stop', time=149, position='1106,993,0' )
    net.mobility( cars[29], 'start', time=77, position='15,997,0' )
    net.mobility( cars[29], 'stop', time=149, position='1103,997,0' )
    net.stopMobility( time=150 )

    for x in (21, 29):

        cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

        print("*** Car[%d] connect to server_s at 1Mbps" %x)
        cars[x].cmdPrint("timeout 160 hping3 --udp -p 5002 -i u10200 -d 1470 200.0.10.2 -q &")
        cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)
        
        print("*** Car[%d] connect to server_e at 1Mbps" %x)
        cars[x].cmdPrint("timeout 160 hping3 --udp -p 5003 -i u10200 -d 1470 200.0.10.3 -q &")
        cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

        print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
        cars[x].cmdPrint("timeout 160 hping3 --udp -p 5004 -i u6800 -d 1470 200.0.10.4 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

        print("*** Car[%d] connect to server_g at 1Mbps" %x)
        cars[x].cmdPrint("timeout 160 hping3 --udp -p 5005 -i u10200 -d 1470 200.0.10.5 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x)
    
    net.startMobility( time=151 )
    net.mobility( cars[22], 'start', time=152, position='20,993,0' )
    net.mobility( cars[22], 'stop', time=222, position='1103,993,0' )
    net.mobility( cars[23], 'start', time=152, position='25,993,0' )
    net.mobility( cars[23], 'stop', time=222, position='1100,993,0' )
    net.mobility( cars[26], 'start', time=152, position='20,995,0' )
    net.mobility( cars[26], 'stop', time=222, position='1103,995,0' )
    net.mobility( cars[27], 'start', time=152, position='25,995,0' )
    net.mobility( cars[27], 'stop', time=222, position='1100,995,0' )
    net.stopMobility( time=75 )
    
    for x in (22, 23, 26, 27):

        cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

        print("*** Car[%d] connect to server_s at 1Mbps" %x)
        cars[x].cmdPrint("timeout 80 hping3 --udp -p 5002 -i u10200 -d 1470 200.0.10.2 -q &")
        cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)

        print("*** Car[%d] connect to server_e at 1Mbps" %x)
        cars[x].cmdPrint("timeout 80 hping3 --udp -p 5003 -i u10200 -d 1470 200.0.10.3 -q &")
        cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

        print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
        cars[x].cmdPrint("timeout 80 hping3 --udp -p 5004 -i u6800 -d 1470 200.0.10.4 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

        print("*** Car[%d] connect to server_g at 1Mbps" %x)
        cars[x].cmdPrint("timeout 80 hping3 --udp -p 5005 -i u10200 -d 1470 200.0.10.5 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x)  
    
    time.sleep(76)

    os.system('fuser -k ./framework_its_sdn/central_controller2.sh')
    os.system('fuser -k ./framework_its_sdn/lc_mob.sh')  
    os.system('fuser -k ./framework_its_sdn/local_controllers.sh')

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
    setLogLevel('debug')
    topology()
