#!/usr/bin/python

'VANETs...'

import os
import time

from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from mininet.link import TCLink

def topology():

    "Create a network."
    net = Mininet_wifi(controller=None, switch=OVSKernelSwitch, link=wmediumd, wmediumd_mode=interference)

    c1 = net.addController( 'c1', controller=RemoteController, ip='127.0.0.1', port=6633 )

    info("*** Creating nodes\n")
    cars = []
    for x in range(0, 15):
        cars.append(x)

    cars[0] = net.addCar('car0',  wlans=1, range='50', ip='200.0.10.110/8', mac='00:00:00:00:00:01', position='2107,250,0')
    cars[1] = net.addCar('car1',  wlans=1, range='50', ip='200.0.10.111/8', mac='00:00:00:00:00:02', position='2107,247,0')
    cars[2] = net.addCar('car2',  wlans=1, range='50', ip='200.0.10.112/8', mac='00:00:00:00:00:03', position='2104,250,0')

    cars[3] = net.addCar('car3',  wlans=1, range='50', ip='200.0.10.113/8', mac='00:00:00:00:00:04', position='1607,247,0')
    cars[4] = net.addCar('car4',  wlans=1, range='50', ip='200.0.10.114/8', mac='00:00:00:00:00:05', position='1604,250,0')

    cars[5] = net.addCar('car5',  wlans=1, range='50', ip='200.0.10.115/8', mac='00:00:00:00:00:06', position='1107,250,0')
    cars[6] = net.addCar('car6',  wlans=1, range='50', ip='200.0.10.116/8', mac='00:00:00:00:00:07', position='1104,247,0')

    cars[7] = net.addCar('car7',  wlans=1, range='50', ip='200.0.10.117/8', mac='00:00:00:00:00:08', position='150,250,0')
    cars[8] = net.addCar('car8',  wlans=1, range='50', ip='200.0.10.118/8', mac='00:00:00:00:00:09', position='200,250,0')
    cars[9] = net.addCar('car9',  wlans=1, range='50', ip='200.0.10.119/8', mac='00:00:00:00:00:10', position='250,250,0')
    cars[10] = net.addCar('car10',  wlans=1, range='50', ip='200.0.10.120/8', mac='00:00:00:00:00:11', position='300,250,0')
    cars[11] = net.addCar('car11',  wlans=1, range='50', ip='200.0.10.121/8', mac='00:00:00:00:00:12', position='350,250,0')
    cars[12] = net.addCar('car12',  wlans=1, range='50', ip='200.0.10.122/8', mac='00:00:00:00:00:13', position='400,243,0')
    cars[13] = net.addCar('car13',  wlans=1, range='50', ip='200.0.10.123/8', mac='00:00:00:00:00:14', position='450,243,0')
    cars[14] = net.addCar('car14',  wlans=1, range='50', ip='200.0.10.124/8', mac='00:00:00:00:00:15', position='500,243,0')

    rsu1 = net.addAccessPoint('rsu1', ssid='rsu1', mode='g',
                                channel='1', range='250', position='1100,250,0', protocols='OpenFlow13')
    rsu2 = net.addAccessPoint('rsu2', ssid='rsu2', mode='g',
                               channel='6', range='250', position='1600,250,0', protocols='OpenFlow13')
    rsu3 = net.addAccessPoint('rsu3', ssid='rsu3', mode='g',
                               channel='11', range='250', position='2100,250,0', protocols='OpenFlow13')

    sw1 = net.addSwitch ('sw1', dpid='9', protocols='OpenFlow13')
    sw2 = net.addSwitch ('sw2', dpid='10', protocols='OpenFlow13')
    sw3 = net.addSwitch ('sw3', dpid='11', protocols='OpenFlow13')
    sw4 = net.addSwitch ('sw4', dpid='12', protocols='OpenFlow13')
    sw5 = net.addSwitch ('sw5', dpid='13', protocols='OpenFlow13')

    server_s1 = net.addHost ('server_s1', ip='200.0.10.2/8', mac='00:00:00:00:00:a2')
    server_s2 = net.addHost ('server_s2', ip='200.0.10.2/8', mac='00:00:00:00:00:a2')
    server_s3 = net.addHost ('server_s3', ip='200.0.10.2/8', mac='00:00:00:00:00:a2')
    server_e = net.addHost ('server_e', ip='200.0.10.3/8', mac='00:00:00:00:00:a3')
    server_e2 = net.addHost ('server_e2', ip='200.0.10.4/8', mac='00:00:00:00:00:a4')
    server_g = net.addHost ('server_g', ip='200.0.10.5/8', mac='00:00:00:00:00:a5')

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
    net.addLink(sw3, rsu1, 1, 3)
    net.addLink(sw4, rsu2, 2, 4)
    net.addLink(sw5, rsu3, 3, 3)
    link1 = net.addLink(sw1, sw2, 1, 4, cls=TCLink )
    link2 = net.addLink(sw3, sw1, 3, 2, cls=TCLink)
    link3 = net.addLink(sw4, sw1, 4, 3, cls=TCLink)
    link4 = net.addLink(sw5, sw1, 5, 4, cls=TCLink)

    print( "*** Configuring links bandwidth" )
    link1.intf1.config( bw=17 )
    link2.intf1.config( bw=5 )
    link3.intf1.config( bw=5 )
    link4.intf1.config( bw=5 )

    net.plotGraph(max_x=2400, max_y=500)
    
    print("*** Starting network")
    net.build()
    c1.start()
    rsu1.start([c1])
    rsu2.start([c1])
    rsu3.start([c1])
    sw1.start([c1])
    sw2.start([c1])
    sw3.start([c1])
    sw4.start([c1])
    sw5.start([c1])

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

    # print( "*** Shutting ports" )
    time.sleep(1)

    os.system('ovs-ofctl del-flows sw1 -O Openflow13; ovs-ofctl add-flow sw1 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl del-flows sw2 -O Openflow13; ovs-ofctl add-flow sw2 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow sw2 "table=1, priority=0, actions=CONTROLLER:65535" -O Openflow13; ovs-ofctl add-flow sw2 "table=1, priority=0, in_port=1 actions=4" -O Openflow13; ovs-ofctl add-flow sw2 "table=1, priority=0, in_port=2 actions=4" -O Openflow13; ovs-ofctl add-flow sw2 "table=1, priority=0, in_port=3 actions=4" -O Openflow13; ovs-ofctl del-flows rsu1 -O Openflow13; ovs-ofctl del-flows rsu2 -O Openflow13; ovs-ofctl del-flows rsu3 -O Openflow13; ovs-ofctl add-flow rsu1 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow rsu2 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow rsu3 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=0, in_port=1, actions=3" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=0, in_port=3, actions=1" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=0, in_port=1, actions=4" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=0, in_port=4, actions=1" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=0, in_port=1, actions=3" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=0, in_port=3, actions=1" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,icmp actions=5" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=1, cookie=0x28,in_port=5, actions=1" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=1, cookie=0x28, in_port=1, arp actions=3,5" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,icmp actions=5" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=1, cookie=0x28,in_port=5, actions=1" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=1, cookie=0x28, in_port=1, arp actions=4,5" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,icmp actions=5" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=1, cookie=0x28,in_port=5, actions=1" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=1, cookie=0x28, in_port=1, arp actions=3,5" -O Openflow13; ovs-ofctl add-flow rsu1 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,udp,tp_dst=5002 actions=5" -O Openflow13; ovs-ofctl add-flow rsu2 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,udp,tp_dst=5002 actions=5" -O Openflow13; ovs-ofctl add-flow rsu3 "table=1, priority=1, cookie=0x28, in_port=1, nw_dst=200.0.10.2,udp,tp_dst=5002 actions=5" -O Openflow13; mysql -u root -pwifi -e "delete from redirect;" framework 2> /dev/null')

    os.system('ovs-ofctl del-flows sw3 -O Openflow13; ovs-ofctl add-flow sw3 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow sw3 "table=1, priority=0, in_port=3 actions=1" -O Openflow13; ovs-ofctl add-flow sw3 "table=1, priority=0, in_port=1 actions=3" -O Openflow13; ovs-ofctl del-flows sw4 -O Openflow13; ovs-ofctl add-flow sw4 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow sw4 "table=1, priority=0, in_port=2 actions=4" -O Openflow13; ovs-ofctl add-flow sw4 "table=1, priority=0, in_port=4 actions=2" -O Openflow13; ovs-ofctl del-flows sw5 -O Openflow13; ovs-ofctl add-flow sw5 "table=0, priority=0, actions=goto_table:1" -O Openflow13; ovs-ofctl add-flow sw5 "table=1, priority=0, in_port=3 actions=5" -O Openflow13; ovs-ofctl add-flow sw5 "table=1, priority=0, in_port=5 actions=3" -O Openflow13;')

    os.system('rm -f car*; rm -f server*; rm -f ping*; rm -f delay*; /etc/init.d/network-manager stop')

    time.sleep(2)

    os.system('mysql -u root -pwifi < ./framework_its_sdn/initialdb.sql -f &')
    #os.system('./framework_its_sdn/lc_mob.sh > j2.txt &')
    time.sleep(4)
    os.system('./framework_its_sdn/central_controller2.sh > j1.txt &')
    #os.system('./framework_its_sdn/local_controllers.sh > j3.txt &')

    server_s1.cmd('tcpdump udp port 5002 -i server_s1-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s1.txt &')
    server_s2.cmd('tcpdump udp port 5002 -i server_s2-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s2.txt &')
    server_s3.cmd('tcpdump udp port 5002 -i server_s3-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_s3.txt &')
    server_e.cmd('tcpdump udp port 5003 -i server_e-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_e.txt &')
    server_e2.cmd('tcpdump udp port 5004 -i server_e2-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_e2.txt &')
    server_g.cmd('tcpdump udp port 5005 -i server_g-eth0 --direction=in -tttttnnvS --immediate-mode -l > server_g.txt &')

    server_s1.cmd('arp -f ./mac2.txt &')
    server_s2.cmd('arp -f ./mac2.txt &')
    server_s3.cmd('arp -f ./mac2.txt &')
    server_e.cmd('arp -f ./mac2.txt &')
    server_e2.cmd('arp -f ./mac2.txt &')
    server_g.cmd('arp -f ./mac2.txt &')

    time.sleep(2)

    for x in xrange(0,15):
        cars[x].cmd('arp -f ./mac.txt &')
        time.sleep(1)


    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=4,dl_src=00:00:00:00:00:01 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:01 actions=4" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=4,dl_src=00:00:00:00:00:02 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:02 actions=4" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=4,dl_src=00:00:00:00:00:03 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:03 actions=4" -O Openflow13')


    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:04 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:04 actions=3" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:05 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:05 actions=3" -O Openflow13')


    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:06 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:06 actions=2" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:07 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:07 actions=2" -O Openflow13')


    os.system('ovs-ofctl add-flow sw2 "table=1, priority=1, cookie=0x0, in_port=1,dl_src=00:00:00:00:00:a3 actions=4" -O Openflow13')
    os.system('ovs-ofctl add-flow sw2 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:a4 actions=4" -O Openflow13')
    os.system('ovs-ofctl add-flow sw2 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:a5 actions=4" -O Openflow13')


    ####################################################Scenario F
    print( "*** Starting F - T1")

    # cars[0].setPosition('2107,250,0')
    # cars[1].setPosition('2107,247,0')
    # cars[2].setPosition('2104,250,0')

    # cars[3].setPosition('1607,247,0')
    # cars[4].setPosition('1604,250,0')

    # cars[5].setPosition('1107,250,0')
    # cars[6].setPosition('1104,247,0')


    # cars[7].setPosition('150,250,0')
    # cars[8].setPosition('200,250,0')
    # cars[9].setPosition('250,250,0')
    # cars[10].setPosition('300,250,0')
    # cars[11].setPosition('350,250,0')
    # cars[12].setPosition('400,243,0')
    # cars[13].setPosition('450,243,0')
    # cars[14].setPosition('500,243,0')

    time.sleep(5)


    # for x in xrange(0,7):
    # # for x in xrange(0,1,2):
    #     cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

    #     print("*** Car[%d] connect to server_s at 500kbps" %x)
    #     # cars[x].cmd('arp -s 200.0.10.2 00:00:00:00:00:a2 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5002 -i u24000 -d 1470 200.0.10.2 -q &")
    #     # cars[x].cmdPrint("rm -f ping%d_s.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_s.txt; done &" %x)
        
    #     print("*** Car[%d] connect to server_e at 500kbps" %x)
    #     # cars[x].cmd('arp -s 200.0.10.3 00:00:00:00:00:a3 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5003 -i u24000 -d 1470 200.0.10.3 -q &")
    #     # cars[x].cmdPrint("rm -f ping%d_e.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_e.txt; done &" %x)

    #     print("*** Car[%d] connect to server_e2 at 1Mbps" %x)
    #     # cars[x].cmd('arp -s 200.0.10.4 00:00:00:00:00:a4 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5004 -i u12000 -d 1470 200.0.10.4 -q &")
    #     # cars[x].cmdPrint("rm -f ping%d_e2.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_e2.txt; done &" %x)

    #     print("*** Car[%d] connect to server_g at 500kbps" %x)
    #     # cars[x].cmd('arp -s 200.0.10.5 00:00:00:00:00:a5 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5005 -i u24000 -d 1470 200.0.10.5 -q &")
    #     # cars[x].cmdPrint("rm -f ping%d_g.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.5 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_g.txt; done &" %x)  

    for x in xrange(0,15):
        cars[x].cmd('./framework_its_sdn/carcon.sh &')
        # time.sleep(1)




    time.sleep(65)

    #########################################################################Scenario C1 (t2)

    #os.system('fuser -k ./framework_its_sdn/local_controllers.sh')

    time.sleep(5)

    print( "*** Starting C1 - T2")
    # cars[0].setPosition('2107,250,0')
    # cars[1].setPosition('2107,247,0')
    # cars[2].setPosition('2104,250,0')
    cars[3].setPosition('2104,247,0')
    cars[4].setPosition('2101,250,0')

    cars[5].setPosition('1607,247,0')

    # cars[6].setPosition('1104,247,0')

    # cars[7].setPosition('150,250,0')
    # cars[8].setPosition('200,250,0')
    # cars[9].setPosition('250,250,0')
    # cars[10].setPosition('300,250,0')
    # cars[11].setPosition('350,250,0')
    # cars[12].setPosition('400,243,0')
    # cars[13].setPosition('450,243,0')
    # cars[14].setPosition('500,243,0')

    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_src=00:00:00:00:00:04 -O Openflow13')
    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_dst=00:00:00:00:00:04 -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=4,dl_src=00:00:00:00:00:04 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:04 actions=4" -O Openflow13')

    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_src=00:00:00:00:00:05 -O Openflow13')
    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_dst=00:00:00:00:00:05 -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=4,dl_src=00:00:00:00:00:05 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:05 actions=4" -O Openflow13')

    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_src=00:00:00:00:00:06 -O Openflow13')
    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_dst=00:00:00:00:00:06 -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:06 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:06 actions=3" -O Openflow13')


    # time.sleep(1)
    # os.system('./framework_its_sdn/lc_mob_2.sh > j7.txt &')

    

    time.sleep(5)

    #os.system('./framework_its_sdn/local_controllers.sh > j3.txt &')

    

    
    time.sleep(65)


    #########################################################################Scenario C2 (t3)
    print( "*** Starting C2 - T3")

    #os.system('fuser -k ./framework_its_sdn/local_controllers.sh')

    time.sleep(5)

    # cars[0].setPosition('2107,250,0')
    # cars[1].setPosition('2107,247,0')
    # cars[2].setPosition('2104,250,0')
    # cars[3].setPosition('2104,247,0')
    # cars[4].setPosition('2101,250,0')

    # cars[5].setPosition('1607,247,0')
    cars[6].setPosition('1604,247,0')
    cars[7].setPosition('1607,250,0')
    cars[8].setPosition('1601,247,0')

    cars[9].setPosition('1107,250,0')
    cars[10].setPosition('1104,247,0')

    # cars[11].setPosition('350,250,0')
    # cars[12].setPosition('400,243,0')
    # cars[13].setPosition('450,243,0')
    # cars[14].setPosition('500,243,0')

    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_src=00:00:00:00:00:07 -O Openflow13')
    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_dst=00:00:00:00:00:07 -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:07 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:07 actions=3" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:08 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:08 actions=3" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:09 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:09 actions=3" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:10 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:10 actions=2" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:11 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:11 actions=2" -O Openflow13')

    # time.sleep(1)
    # os.system('./framework_its_sdn/lc_mob_2.sh > j7.txt &')

    time.sleep(5)

    #os.system('./framework_its_sdn/local_controllers.sh > j3.txt &')

    

    # for x in xrange(7,11):

    #     cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

    #     print("*** Car[%d] connect to server_s at 500kbps" %x)
    #     cars[x].cmd('arp -s 200.0.10.2 00:00:00:00:00:a2 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5002 -i u24000 -d 1470 200.0.10.2 -q &")
    #     cars[x].cmdPrint("rm -f ping%d_s.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_s.txt; done &" %x)
        
    #     print("*** Car[%d] connect to server_e at 500kbps" %x)
    #     cars[x].cmd('arp -s 200.0.10.3 00:00:00:00:00:a3 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5003 -i u24000 -d 1470 200.0.10.3 -q &")
    #     cars[x].cmdPrint("rm -f ping%d_e.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_e.txt; done &" %x)

    #     print("*** Car[%d] connect to server_e2 at 1Mbps" %x)
    #     cars[x].cmd('arp -s 200.0.10.4 00:00:00:00:00:a4 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5004 -i u12000 -d 1470 200.0.10.4 -q &")
    #     cars[x].cmdPrint("rm -f ping%d_e2.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_e2.txt; done &" %x)

    #     print("*** Car[%d] connect to server_g at 500kbps" %x)
    #     cars[x].cmd('arp -s 200.0.10.5 00:00:00:00:00:a5 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5005 -i u24000 -d 1470 200.0.10.5 -q &")
    #     cars[x].cmdPrint("rm -f ping%d_g.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.5 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_g.txt; done &" %x)

    time.sleep(65)

    #########################################################################Scenario C3 (t4)
    print( "*** Starting C3 - T4")

    #os.system('fuser -k ./framework_its_sdn/local_controllers.sh')

    time.sleep(5)

    # cars[0].setPosition('2107,250,0')
    # cars[1].setPosition('2107,247,0')
    # cars[2].setPosition('2104,250,0')
    # cars[3].setPosition('2104,247,0')
    # cars[4].setPosition('2101,250,0')

    # cars[5].setPosition('1607,247,0')
    # cars[6].setPosition('1604,247,0')
    # cars[7].setPosition('1607,250,0')
    # cars[8].setPosition('1601,247,0')
    cars[9].setPosition('1604,250,0')
    cars[10].setPosition('1601,250,0')

    cars[11].setPosition('1107,250,0')
    cars[12].setPosition('1107,247,0')
    cars[13].setPosition('1104,250,0')
    cars[14].setPosition('1104,247,0')

    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_src=00:00:00:00:00:10 -O Openflow13')
    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_dst=00:00:00:00:00:10 -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:10 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:10 actions=3" -O Openflow13')

    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_src=00:00:00:00:00:11 -O Openflow13')
    os.system('ovs-ofctl del-flows sw1 cookie=0x0/-1,dl_dst=00:00:00:00:00:11 -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=3,dl_src=00:00:00:00:00:11 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:11 actions=3" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:12 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:12 actions=2" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:13 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:13 actions=2" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:14 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:14 actions=2" -O Openflow13')

    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=2,dl_src=00:00:00:00:00:15 actions=1" -O Openflow13')
    os.system('ovs-ofctl add-flow sw1 "table=1, priority=1, cookie=0x0, in_port=1,dl_dst=00:00:00:00:00:15 actions=2" -O Openflow13')

    time.sleep(5)

    #os.system('./framework_its_sdn/local_controllers.sh > j3.txt &')

    # time.sleep(1)
    # os.system('./framework_its_sdn/lc_mob_2.sh > j7.txt &')

    


    # for x in xrange(11,15):

    #     cars[x].cmd('tcpdump -i car%d-wlan0 --direction=out -tttttnnvS --immediate-mode -l > car%d.txt &' % (x, x))

    #     print("*** Car[%d] connect to server_s at 500kbps" %x)
    #     cars[x].cmd('arp -s 200.0.10.2 00:00:00:00:00:a2 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5002 -i u24000 -d 1470 200.0.10.2 -q &")
    #     cars[x].cmdPrint("rm -f ping%d_s.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.2 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_s.txt; done &" %x)
        
    #     print("*** Car[%d] connect to server_e at 500kbps" %x)
    #     cars[x].cmd('arp -s 200.0.10.3 00:00:00:00:00:a3 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5003 -i u24000 -d 1470 200.0.10.3 -q &")
    #     cars[x].cmdPrint("rm -f ping%d_e.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.3 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_e.txt; done &" %x)

    #     print("*** Car[%d] connect to server_e2 at 1Mbps" %x)
    #     cars[x].cmd('arp -s 200.0.10.4 00:00:00:00:00:a4 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5004 -i u12000 -d 1470 200.0.10.4 -q &")
    #     cars[x].cmdPrint("rm -f ping%d_e2.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.4 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_e2.txt; done &" %x)

    #     print("*** Car[%d] connect to server_g at 500kbps" %x)
    #     cars[x].cmd('arp -s 200.0.10.5 00:00:00:00:00:a5 &')
    #     cars[x].cmdPrint("timeout 330 hping3 --udp -p 5005 -i u24000 -d 1470 200.0.10.5 -q &")
    #     cars[x].cmdPrint("rm -f ping%d_g.txt" %x)
    #     cars[x].cmdPrint("ping 200.0.10.5 -i 1 -c 330 | while read line; do echo $(date +%%s) - $line >> ping%d_g.txt; done &" %x) 

    time.sleep(75)

    os.system('pkill tcpdump')
    os.system('pkill hping3')
    os.system('pkill ping')
    time.sleep(2)

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()

    os.system('fuser -k ./framework_its_sdn/lc_mob.sh') 
    os.system('fuser -k ./framework_its_sdn/central_controller2.sh')
    os.system('fuser -k ./framework_its_sdn/local_controllers.sh')
    # server_s1.cmd('iptables -D OUTPUT 1')
    # server_s2.cmd('iptables -D OUTPUT 1')
    # server_s3.cmd('iptables -D OUTPUT 1')
    # server_e.cmd('iptables -D OUTPUT 1')
    # server_e2.cmd('iptables -D OUTPUT 1')
    # server_g.cmd('iptables -D OUTPUT 1')


if __name__ == '__main__':
    setLogLevel('debug')
    topology()