import matplotlib.pyplot as plt


# Read data from the text file
with open('pings_results_p.txt', 'r') as file:
    lines = file.readlines()

# Extract the x and y values from the lines
x_values = []  # time
y_values = []  # number of packets
timer = 0
counter = 0
for line in lines:
    counter += 1
    data = line.split("\t")
    time = float(data[1])
    x_values .append(time)
    y_values .append(data[0])

fig, ax = plt.subplots()
ax.plot(x_values, y_values)

plt.xlabel('Packets RTT (ms)')
plt.ylabel('Packet number')
plt.title('DDOS using python - 4 PING  packets')

# Make the y axis as logarithmic scale
ax.set_yscale('log')

fig.savefig("Pings_p.png")
