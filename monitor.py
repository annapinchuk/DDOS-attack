import os
from time import sleep
import time

SERVER_IP = "127.0.0.1"

file = open("ip_output.txt", "a")

index =0

while True:
    index+=1
    # Pinging each IP address 4 times
    
    start = time.time()*1000
    response = os.popen(f"ping -c 4 {SERVER_IP} ").read()
    end = time.time()*1000

    print(response)
    # saving some ping output details to output file
    if ("Request timed out." or "unreachable") in response:
        file.write("the server didn't answer"+'\n')
    else:
        rtt = end - start

        textToFile = "packet number: " + str(index) + " rtt: " + str(rtt) + "(ms)"
        file.write(textToFile)

        file.write(str(SERVER_IP) + ' is up '+'\n')
    sleep(5)

# print output file to screen
with open("ip_output.txt") as file:
    output = file.read()
    f.close()
    print(output)
with open("ip_output.txt", "w") as file:
    pass

file.close()