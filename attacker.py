import time
from scapy.all import IP, TCP, send, sniff
from random import randint

# initialize global variables:
TARGET_IP = "127.0.0.1"
TARGET_PORT = 9000
FILE_NAME = "syns_result_p.txt"


def randomIP():
    ip = ".".join(map(str, (randint(0, 255)for _ in range(4))))
    return ip


def randInt():
    x = randint(1000, 8999)
    return x


def create_syn_packet():
    file = open(FILE_NAME, 'w')
    print("Packets are sending ...")

    for index in range(0, 10):
        # timer.start
        start = time.time()*1000
        print("for")
        s_port = randInt()
        s_eq = randInt()
        w_indow = randInt()

        IP_Packet = IP()
        IP_Packet.src = randomIP()
        IP_Packet.dst = TARGET_IP

        TCP_Packet = TCP()
        TCP_Packet.sport = 8000
        TCP_Packet.dport = TARGET_PORT
        TCP_Packet.flags = "S"
        TCP_Packet.seq = s_eq
        TCP_Packet.window = w_indow

        # send(IP_Packet/TCP_Packet, verbose=0)
        send(IP_Packet/TCP_Packet)
        print("send")
        # sniff(prn = handle_packet, filter="tcp")
        print("sniff")
        # timer.done
        end = time.time()*1000

        rtt = start - end

        textToFile = "packet number: " + str(index) + "rtt: " + str(rtt) + "(ms)"
        file.write(textToFile)


create_syn_packet()
