import matplotlib.pyplot as plt
if __name__ == '__main__':
    data_1a = open("1a.csv", "r")
    data_1b = open("1b.csv", "r")
    x_1a = []
    x_1b = []
    for row in data_1a:
        x_1a.append(int(row))
    for row in data_1b:
        x_1b.append(int(row))
    #print(str(x_1a))
    #print(str(x_1b))

    # ----line
    plt.plot(x_1a, x_1b)
    plt.title("Line of Random Numbers")
    plt.xlabel("X", size=14)
    plt.ylabel("Y", size=14)
    plt.savefig('number_line.png')
    plt.show()
    
    #----histogram
    #bins = square root of 1000 and round up

    plt.hist(x_1a,bins=32, alpha = 0.5, label = "0-100")
    plt.hist(x_1b,bins=32, alpha = 0.5, label = "3x+6")
    plt.legend(loc='upper right')
    plt.xlabel("Number", size=14)
    plt.ylabel("Count", size=14)
    plt.title("Overlapping Histograms of Random Numbers")
    plt.savefig('number_histogram.png')
    plt.show()
