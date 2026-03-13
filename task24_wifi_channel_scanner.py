import CoreWLAN

iface = CoreWLAN.CWInterface.interface()

networks, err = iface.scanForNetworksWithName_error_(None, None)

for net in networks:
    print(net.ssid(), net.rssiValue(), net.wlanChannel().channelNumber())
