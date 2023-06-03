#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def multiControllerNet():
    net = Mininet( controller=RemoteController, switch=OVSSwitch,
                   waitConnected=True )

    info( "*** Creating (reference) controllers\n" )
    c1 = net.addController( 'c1', ip='127.0.0.1', port=6633 )
    c2 = net.addController( 'c2', ip='127.0.0.1', port=6655 )

    info( "*** Creating switches\n" )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    info( "*** Creating hosts\n" )
    hosts1 = net.addHost('h1', ip='10.0.2.10', mac='00:00:00:00:00:01')
    hosts2 = net.addHost('h2', ip='10.0.2.20', mac='00:00:00:00:00:02')
    hosts3 = net.addHost('h3', ip='192.168.2.30', mac='00:00:00:00:00:03')
    hosts4 = net.addHost('h4', ip='192.168.2.40', mac='00:00:00:00:00:04')
    info( "*** Creating links\n" )
    net.addLink(s1, hosts1)
    net.addLink(s1, hosts2)
    net.addLink(s2, hosts3)
    net.addLink(s2, hosts4)
    net.addLink(s2, hosts1, ip='192.168.2.10/8')

    info( "*** Starting network\n" )
    net.build()
    c1.start()
    c2.start()
    s1.start( [ c1 ] )
    s2.start( [ c2 ] )

    info( "*** Testing network\n" )
    #net.ping([s1, hosts2])

    info( "*** Running CLI\n" )
    CLI( net )

    info( "*** Stopping network\n" )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    multiControllerNet()
