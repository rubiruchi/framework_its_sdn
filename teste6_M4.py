#!/usr/bin/python

'An SDN Framework to Application Driven Vehicular Ad Hoc Networks - VANETs'

import os
import random
import time

from mininet.node import RemoteController, OVSKernelSwitch
from mn_wifi.node import OVSKernelAP
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from mininet.link import TCLink


def topology():

    "Create a network."
    # net = Mininet_wifi(controller=None, switch=OVSKernelSwitch, link=wmediumd, wmediumd_mode=interference)
    net = Mininet_wifi(controller=None, autoStaticArp=True, switch=OVSKernelSwitch, accessPoint=OVSKernelAP)

    c1 = net.addController( 'c1', controller=RemoteController, ip='127.0.0.1', port=6633 )

    info("*** Creating nodes\n")
    cars = []
    for x in range(0, 10):
        cars.append(x)

    cars[0] = net.addCar('car0', wlans=1, range='50', ip='200.0.10.110/8', mac='00:00:00:00:00:01', position='1105,975,0')
    cars[1] = net.addCar('car1', wlans=1, range='50', ip='200.0.10.111/8', mac='00:00:00:00:00:02', position='1110,975,0')
    cars[2] = net.addCar('car2', wlans=1, range='50', ip='200.0.10.112/8', mac='00:00:00:00:00:03', position='1605,975,0')
    cars[3] = net.addCar('car3', wlans=1, range='50', ip='200.0.10.113/8', mac='00:00:00:00:00:04', position='2105,975,0')
    cars[4] = net.addCar('car4', wlans=1, range='50', ip='200.0.10.114/8', mac='00:00:00:00:00:05', position='2100,975,0')
    cars[5] = net.addCar('car5', wlans=1, range='50', ip='200.0.10.115/8', mac='00:00:00:00:00:06', position='2110,975,0')
    cars[6] = net.addCar('car6', wlans=1, range='50', ip='200.0.10.116/8', mac='00:00:00:00:00:07', position='2095,975,0')
    cars[7] = net.addCar('car7', wlans=1, range='50', ip='200.0.10.117/8', mac='00:00:00:00:00:08', position='1560,975,0')
    cars[8] = net.addCar('car8', wlans=1, range='50', ip='200.0.10.118/8', mac='00:00:00:00:00:09', position='1570,975,0')
    cars[9] = net.addCar('car9', wlans=1, range='50', ip='200.0.10.119/8', mac='00:00:00:00:00:10', position='1580,975,0')

    # rsu1 = net.addAccessPoint('rsu1', ssid='rsu1', dpid='6', mode='g', channel='11',range=250, position='1100,1000,0', protocols='OpenFlow13')
    # rsu2 = net.addAccessPoint('rsu2', ssid='rsu2', dpid='7', mode='g', channel='11', range=250, position='1600,1000,0', protocols='OpenFlow13')
    # rsu3 = net.addAccessPoint('rsu3', ssid='rsu3', dpid='8', mode='g', channel='11', range=250, position='2100,1000,0', protocols='OpenFlow13')

    rsu1 = net.addAccessPoint('rsu1', ssid='rsu1', mode='g', channel='11',range=250, position='1100,1000,0', protocols='OpenFlow13')
    rsu2 = net.addAccessPoint('rsu2', ssid='rsu2', mode='g', channel='11', range=250, position='1600,1000,0', protocols='OpenFlow13')
    rsu3 = net.addAccessPoint('rsu3', ssid='rsu3', mode='g', channel='11', range=250, position='2100,1000,0', protocols='OpenFlow13')

    sw1 = net.addSwitch ('sw1', dpid='9', protocols='OpenFlow13', position='1600,1750,0')
    sw2 = net.addSwitch ('sw2', dpid='10', protocols='OpenFlow13', position='1800,1750,0')

    server_s1 = net.addHost ('server_s1', ip='200.0.10.2/8', position='1000,1150,0')
    server_s2 = net.addHost ('server_s2', ip='200.0.10.2/8', position='1500,1150,0')
    server_s3 = net.addHost ('server_s3', ip='200.0.10.2/8', position='2150,1150,0')
    server_e = net.addHost ('server_e', ip='200.0.10.3/8', position='2000,1700,0')
    server_e2 = net.addHost ('server_e2', ip='200.0.10.4/8', position='2000,1900,0')
    server_g = net.addHost ('server_g', ip='200.0.10.5/8', position='2000,2100,0')
    
    info("*** Configuring Propagation Model\n")
    net.propagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating and Creating links\n")
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
    link1.intf1.config( bw=18 )
    link2.intf1.config( bw=6 )
    link3.intf1.config( bw=6 )
    link4.intf1.config( bw=6 )

    # print( "*** Ploting Graph" )
    # net.plotGraph(max_x=2500, max_y=2500)

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


    os.system('ovs-vsctl set bridge rsu1 other-config:datapath-id=0000000000000006')
    os.system('ovs-vsctl set bridge rsu2 other-config:datapath-id=0000000000000007')
    os.system('ovs-vsctl set bridge rsu3 other-config:datapath-id=0000000000000008')

    
    os.system('ovs-vsctl --all destroy QoS; ovs-vsctl --all destroy Queue')

    os.system('ovs-vsctl set-manager ptcp:6632')

    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000006/ovsdb_addr')
    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000007/ovsdb_addr')
    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000008/ovsdb_addr')
    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000009/ovsdb_addr')
    os.system('curl -X PUT -d \'"tcp:127.0.0.1:6632"\' http://localhost:8080/v1.0/conf/switches/0000000000000010/ovsdb_addr')


    print( "*** Shutting ports" )
    #time.sleep(3)


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
    time.sleep(1)
    os.system('./framework_its_sdn/central_controller2.sh > j1.txt &')
    os.system('./framework_its_sdn/local_controllers.sh > j3.txt &')

    # time.sleep(1)

    server_s1.cmd('tcpdump udp port 5002 -i server_s1-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s1.txt &')
    server_s2.cmd('tcpdump udp port 5002 -i server_s2-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s2.txt &')
    server_s3.cmd('tcpdump udp port 5002 -i server_s3-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s3.txt &')
    server_e.cmd('tcpdump udp port 5003 -i server_e-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_e.txt &')
    server_e2.cmd('tcpdump udp port 5004 -i server_e2-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_e2.txt &')
    server_g.cmd('tcpdump udp port 5005 -i server_g-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_g.txt &')


    print( "*** Iniciando geracao de trafego" )

    time.sleep(2)

    for x in xrange(0,10):

        cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

        print("*** Car[%d] connect to server_s at 1Mbps" %x)
        cars[x].cmdPrint("timeout 205 hping3 --udp -p 5002 -i u10200 -d 1470 200.0.10.2 -q &")
        cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 205  > ping%d_ss.txt &" %x)
        
        print("*** Car[%d] connect to server_e at 1Mbps" %x)
        cars[x].cmdPrint("timeout 205 hping3 --udp -p 5003 -i u10200 -d 1470 200.0.10.3 -q &")
        cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 205  > ping%d_se.txt &" %x)

        print("*** Car[%d] connect to server_e2 at 2Mbps" %x)
        cars[x].cmdPrint("timeout 205 hping3 --udp -p 5004 -i u6800 -d 1470 200.0.10.4 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_se2.txt &" %x)

        print("*** Car[%d] connect to server_g at 1Mbps" %x)
        cars[x].cmdPrint("timeout 205 hping3 --udp -p 5005 -i u10200 -d 1470 200.0.10.5 -q &")
        cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 205  > ping%d_sg.txt &" %x)   


    time.sleep(33)

    print("Moving Car0 to RSU2")
    cars[0].setPosition('1605,975,0')

    time.sleep(33)

    print("Moving Car0 to RSU3")
    cars[0].setPosition('2105,975,0')

    time.sleep(33)

    print("Moving Car1 to RSU2")
    cars[1].setPosition('1605,975,0')

    time.sleep(33)

    print("Moving Car2 to RSU3")
    cars[2].setPosition('2105,975,0')

    time.sleep(33)

    print("Moving Car1 to RSU3")
    cars[1].setPosition('2105,975,0')

    time.sleep(33)

    os.system('fuser -k ./framework_its_sdn/central_controller2.sh')
    os.system('fuser -k ./framework_its_sdn/lc_mob.sh')  
    os.system('fuser -k ./framework_its_sdn/local_controllers.sh')


    os.system('pkill tcpdump')
    os.system('pkill hping3')
    os.system('pkill ping')

    print("*** Running CLI")
    CLI_wifi(net)

    #os.system('rm *.vanetdata')

    server_s1.cmd('iptables -D OUTPUT 1')
    server_s2.cmd('iptables -D OUTPUT 1')
    server_s3.cmd('iptables -D OUTPUT 1')
    server_e.cmd('iptables -D OUTPUT 1')
    server_e2.cmd('iptables -D OUTPUT 1')
    server_g.cmd('iptables -D OUTPUT 1')


    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
topology()