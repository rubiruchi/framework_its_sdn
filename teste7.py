#!/usr/bin/python

'VANETs...'

import os
import time

from mininet.node import Controller, OVSKernelSwitch, RemoteController
#from mininet.node import Controller, OVSKernelSwitch
from mininet.log import setLogLevel, info
from mininet.wifi.cli import CLI_wifi
from mininet.wifi.net import Mininet_wifi
from mininet.wifi.link import wmediumd
from mininet.wifi.wmediumdConnector import interference
#from mininet.link import TCLink


def topology():

    "Create a network."
    net = Mininet_wifi(controller=None, switch=OVSKernelSwitch,
                       link=wmediumd, wmediumd_mode=interference)

    # c1 = net.addController( 'c1', controller=RemoteController, ip='127.0.0.1', port=6633 )

    info("*** Creating nodes\n")
    cars = []
    for x in range(0, 10):
        cars.append(x)

    for x in range(0, 10):
        cars[x] = net.addCar('car%s' % (x + 1), wlans=1,
                             ip='10.0.0.%s/8'% (x + 1), range='50')

    rsu1 = net.addAccessPoint('RSU11', ssid='RSU11', mode='g',
                               channel='1', range='250', position='1100,1000,0', protocols='OpenFlow13')
    rsu2 = net.addAccessPoint('RSU12', ssid='RSU12', mode='g',
                               channel='6', range='250', position='1600,1000,0', protocols='OpenFlow13')
    rsu3 = net.addAccessPoint('RSU13', ssid='RSU13', mode='g',
                               channel='11', range='250', position='2100,1000,0', protocols='OpenFlow13')

    c1 = net.addController('c1', controller=Controller)

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
    net.addLink(sw1, sw2, 1, 4)
    net.addLink(rsu1, sw1, 3, 2)
    net.addLink(rsu2, sw1, 4, 3)
    net.addLink(rsu3, sw1, 3, 4)
    # link1 = net.addLink(sw1, sw2, 1, 4, cls=TCLink )
    # link2 = net.addLink(rsu1, sw1, 3, 2, cls=TCLink)
    # link3 = net.addLink(rsu2, sw1, 4, 3, cls=TCLink)
    # link4 = net.addLink(rsu3, sw1, 3, 4, cls=TCLink)

    # print( "*** Configuring links bandwidth" )
    # link1.intf1.config( bw=93 )
    # link2.intf1.config( bw=31 )
    # link3.intf1.config( bw=31 )
    # link4.intf1.config( bw=31 )

    net.plotGraph(max_x=2000, max_y=2000)

    # net.roads(10)

    net.startMobility( time=0 )
    net.mobility( cars[0], 'start', time=1, position='120,1000,0' )
    net.mobility( cars[0], 'stop', time=179, position='2101,1000,0' )
    net.mobility( cars[1], 'start', time=1, position='130,1000,0' )
    net.mobility( cars[1], 'stop', time=179, position='2095,999,0' )
    net.mobility( cars[2], 'start', time=1, position='135,1000,0' )
    net.mobility( cars[2], 'stop', time=59, position='2097,997,0' )
    net.mobility( cars[3], 'start', time=1, position='140,1000,0' )
    net.mobility( cars[3], 'stop', time=59, position='1601,998,0' )
    net.mobility( cars[4], 'start', time=1, position='145,1000,0' )
    net.mobility( cars[4], 'stop', time=59, position='1599,999,0' )
    net.mobility( cars[5], 'start', time=1, position='150,1000,0' )
    net.mobility( cars[5], 'stop', time=179, position='1595,997,0' )
    net.mobility( cars[6], 'start', time=1, position='155,1000,0' )
    net.mobility( cars[6], 'stop', time=179, position='1101,997,0' )
    net.mobility( cars[7], 'start', time=1, position='160,1000,0' )
    net.mobility( cars[7], 'stop', time=179, position='1098,998,0' )
    net.mobility( cars[8], 'start', time=1, position='165,1000,0' )
    net.mobility( cars[8], 'stop', time=179, position='1095,999,0' )
    net.stopMobility( time=180 )

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

    time.sleep(1)

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