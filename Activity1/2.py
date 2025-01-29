import matplotlib.pyplot as plt

def graphSnowfall(t):
    #reading the data from the file
    with open(t, "r") as file:
        data = [int(line.strip()) for line in file if line.strip().isdigit()]

    #determining the maximum value and number of intervals
    maxValue = max(data)
    maxIntervals = (maxValue // 10) + 1

    #initialize the list with the number of aggregations
    intervals = [0] * maxIntervals

    for i in data:
        dataIndex = min(i // 10, maxIntervals - 1)
        intervals[dataIndex] += 1

    #generate range labels for the plot
    ranges = [f"{i * 10 + 1}-{(i + 1) * 10}" if i > 0 else f"{i * 10}-{(i + 1) * 10}" for i in range(len(intervals))]

    #plotting the graph
    plt.figure(figsize=(12, 6))
    plt.bar(ranges, intervals, color='skyblue', edgecolor='navy')

    plt.xlabel('Snowfall Range (cms)', fontweight='bold')
    plt.ylabel('Number of Occurrences', fontweight='bold')
    plt.title('Distribution of Snowfall in Intervals', fontsize=16, fontweight='bold')
    plt.show()


