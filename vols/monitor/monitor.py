import os
from time import sleep
import time

# initialize global variables:
SERVER_IP = "127.0.0.1"
FILE_NAME = "monitors_ping.txt"

#open a file in write mode in order to save the packet's data
file = open(FILE_NAME, "a")

#define a times array - for calculating the avg time
times = []

index =1

while True:
    
    # start the timer - in order to calculate the build packet time
    start = time.time()*1000
    
    # Pinging to the server 4 times
    response = os.popen(f"ping -c 4 {SERVER_IP} ").read()
    
    # after getting an answer - close the the timer
    end = time.time()*1000

    print(response)
    
    # saving some ping output details to output file
    if ("Request timed out." or "unreachable") in response:
        file.write("the server didn't answer"+'\n')
    else:
        # calculate the sent packet time
        rtt = end - start

        # add the sent time to the array
        times.append(rtt)

        # add the packet data to the file
        textToFile = "packet number: " + str(index) + " rtt: " + str(rtt) + "(ms)\n"
        file.write(textToFile)
    
    sleep(5)
    index+=1

file.close()