import matplotlib.pyplot as plt

# Read data from the text file
with open('syns_results_py.txt', 'r') as file:
    lines = file.readlines()

# Extract the x and y values from the lines
x_values = []
y_values = []
for line in lines[1:]:
    data = line.strip().split('\t')
    x_values.append(float(data[1]))
    y_values.append(int(data[0]))
    print(int(data[0]))

# Plot the data
plt.xlim(14,21792320)
plt.ylim(0,1000000)
plt.plot(x_values, y_values, marker='o', label='Sine wave')
plt.xlabel('Time')
plt.ylabel('Number')
plt.title('DDOS using python')

# Display the graph
plt.show()
